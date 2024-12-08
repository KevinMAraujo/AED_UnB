import pandas as pd
import time
import logging
import random
from datetime import datetime
from utils.setup import configurar_log, registrar_individuo_no_historico, registrar_no_historico
from utils.setup import salvar_dados_execucao, salvar_evolucao_fitness, salvar_resultado, salvar_tempo_execucao, salvar_configuracao
from utils.populacao import gerar_populacao_inicial
from utils.individuo import calcular_fitness, mutar, cruzar, validar_individuo, selecao_torneio
from utils.load_env import get_env

# Algoritmo Genético
def algoritmo_genetico(professores:pd.DataFrame,  turmas:pd.DataFrame, professor_curso:pd.DataFrame, professor_local:pd.DataFrame, file_name:str=None, geracoes:int=get_env("GERACOES")):
    """
    Executa o algoritmo genético para otimizar a alocação de professores às turmas.

    Args:
        professores (DataFrame): Dados dos professores.
        turmas (DataFrame): Dados das turmas.
        professor_curso (DataFrame): Associação professor-curso.
        professor_local (DataFrame): Associação professor-local.
        geracoes (int): Número de gerações a serem processadas.

    Returns:
        tuple: População final e histórico de fitness das gerações.
    """
    try:
        logging.info("Iniciando o programa...")
        inicio_execucao = time.time()
        
        time_start = datetime.now().strftime('%Y%m%d_%H%M%S')
        arquivo_info = "informacoes_de_execucao_"+str(time_start)+".txt"
        
        nome_arquivo_log = f"algoritmo_genetico_"+str(time_start)+".log"
        file_handler = configurar_log(nome_arquivo_log)

        
        
        logging.info(f"-> Gerando População Inicial ---")
        populacao = gerar_populacao_inicial(turmas, professores, professor_local, professor_curso)
        logging.info(f"---> Calculando Fitness da População Inicial ---")
        for individuo in populacao:
            individuo["fitness"] = calcular_fitness(individuo["individuo"], turmas, professores)

        logging.info(f"-> Gerando Historico Inicial ---")
        historico = registrar_no_historico([], 0, populacao)
        historico_individuos = registrar_individuo_no_historico([], 0, populacao, 'normal')
        logging.info(f"-> Gerações : {geracoes} ---")
        
        for geracao in range(1,geracoes+1):
            logging.info(f"Processando geração {geracao}...")
            novos_individuos = []
            #seleção dos pais aleatória ou por torneio
            #pai1, pai2 = random.sample(populacao, 2)
            # Seleção por Torneio
            pai1 = selecao_torneio(populacao, turmas, professores, int(get_env("TAMANHO_TORNEIO")) )
            pai2 = selecao_torneio(populacao, turmas, professores, int(get_env("TAMANHO_TORNEIO")) )
            contador = 0

            # Caso os pais sejam iguais, vamos repetindo até que seja um pai diferente.
            while pai1['individuo'] == pai2['individuo']:
                logging.info(f"pai1: {pai1}")
                logging.info(f"pai2: {pai2}")
                #selecionando um novo pai2
                pai2 = selecao_torneio(populacao, turmas, professores, int(get_env("TAMANHO_TORNEIO")))
                
                # se após fazer 100 tentativas de selecionar os pais pelo torneio, eles continuarem sendo iguais
                # então selecionar o pai2 de forma aleatoria. Sem a necessidade de ter o melhor fitness
                if contador>=100:
                    logging.info('Selecionando pai2 com random.sample')
                    logging.info(f"-> População: {populacao}")
                    x, pai2 = random.sample(populacao, 2)
                    logging.info(f"-> pai2 random.sample: {pai2}")
                    contador=0
                    break
                contador+=1
            
            filho1, filho2 = cruzar(pai1, pai2)

            if random.random() <= float(get_env("PROB_MUTACAO")):
                logging.info(f"Realizando Mutação na geração {geracao+1}")
                filho1 = mutar(filho1, professores, professor_local, professor_curso, turmas, float(get_env("PROB_MUTACAO")) )
                filho2 = mutar(filho2, professores, professor_local, professor_curso, turmas, float(get_env("PROB_MUTACAO")) )

            filho1["fitness"] = calcular_fitness(filho1["individuo"], turmas, professores)
            filho2["fitness"] = calcular_fitness(filho2["individuo"], turmas, professores)
            novos_individuos.extend([filho1, filho2])

            # Ajustar e inserir os novos indivíduos na população
            for novo_ind in novos_individuos:        
                # Verificando se o filho gerado já existe na população
                duplicado = any(novo_ind['individuo'] == ind["individuo"] for ind in populacao)
                if duplicado:
                    logging.info(f"Indivíduo Duplicado: {novo_ind['individuo']}")
                    historico_individuos = registrar_individuo_no_historico(historico_individuos, geracao, [novo_ind], 'duplicado')
                    continue
                elif validar_individuo(novo_ind, turmas, professores, professor_local, professor_curso) == False:
                    logging.info(f"Indivíduo Invalido: {novo_ind}")
                    historico_individuos = registrar_individuo_no_historico(historico_individuos, geracao, [novo_ind], 'invalido')
                    continue
                else:
                    pior_individuo = min(populacao, key=lambda ind: ind["fitness"])
                    if novo_ind["fitness"] > pior_individuo["fitness"]:
                        populacao.remove(pior_individuo)  # Remove o pior indivíduo
                        populacao.append(novo_ind)  # Adiciona o novo indivíduo
                        historico_individuos = registrar_individuo_no_historico(historico_individuos, geracao, [novo_ind], 'filho')
                        logging.info(f"Novo indivíduo com fitness {novo_ind['fitness']:.2f}")
                        logging.info(f"substituiu um com fitness {pior_individuo['fitness']:.2f}")

            # Atualiza o histórico com a nova geração
            historico = registrar_no_historico(historico, geracao, populacao)

            # Garantir que o tamanho da população permaneça fixo
            if len(populacao) > int(get_env("POPULACAO_INICIAL")):
                populacao.sort(key=lambda ind: calcular_fitness(ind["individuo"], turmas, professores), reverse=True)
                populacao = populacao[:int(get_env("POPULACAO_INICIAL"))]

        # Calcular tempo total de execução
        time_end = datetime.now().strftime('%Y%m%d_%H%M%S')
        tempo_total = time.time() - inicio_execucao
        
        logging.info(f"Tempo total de execução: {(tempo_total/60):.2f} minutos")
        
        if file_name is not None:
            arquivo_info  = "informacoes_de_execucao_"+file_name+".txt"
            arquivo_tempo_execucao = "tempo_execucao_"+file_name+".txt"
            arquivo_historico_execucao = "historico_execucao_"+file_name+".csv"
            arquivo_historico_individuo = "historico_individuos_"+file_name+".csv"
            arquivo_evolucao_fitness = "evolucao_fitness_"+file_name+".csv"
            arquivo_melhor_ind = "resultado_final_melhor_"+file_name+".csv"
            arquivo_pior_ind = "resultado_final_pior_"+file_name+".csv"
        else:
            arquivo_info = "informacoes_de_execucao_"+str(time_start)+".txt"
            arquivo_tempo_execucao = "tempo_execucao_"+str(time_start)+".txt"
            arquivo_historico_execucao = 'historico_execucao_'+str(time_start)+'.csv'
            arquivo_historico_individuo = f'historico_individuos_'+str(time_start)+'.csv'
            arquivo_evolucao_fitness = f'evolucao_fitness_'+str(time_start)+'.csv'
            arquivo_melhor_ind = f"resultado_final_melhor_"+str(time_start)+".csv"
            arquivo_pior_ind = f"resultado_final_pior_"+str(time_start)+".csv"

        salvar_tempo_execucao(arquivo_tempo_execucao, time_end)

        # Salvar os resultados
        print('salvando dados da execução')
        salvar_configuracao(arquivo_info, time_start, tempo_total)
        salvar_dados_execucao(historico,arquivo_historico_execucao)
        salvar_dados_execucao(historico_individuos,arquivo_historico_individuo)

        print('salvar_evolucao_fitness')
        salvar_evolucao_fitness(historico, arquivo_evolucao_fitness)

        melhor_individuo = max(populacao, key=lambda ind: ind["fitness"])
        pior_individuo = min(populacao, key=lambda ind: ind["fitness"])

        print('salvar_resultado')
        salvar_resultado(melhor_individuo["individuo"], arquivo_melhor_ind)
        salvar_resultado(pior_individuo["individuo"], arquivo_pior_ind)

        logging.info("Histórico salvo ao final!")

        file_handler.close()
        logging.getLogger().removeHandler(file_handler)

        return populacao,melhor_individuo, historico
    except Exception as e:
        logging.error(f"Erro na execução do algoritmo")
        logging.error(f"Erro Info: {e}")
        raise
