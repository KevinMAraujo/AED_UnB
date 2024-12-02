import pandas as pd
import time
import logging
import random
from datetime import datetime
from utils.setup import configurar_log, CONFIG, registrar_individuo_no_historico, registrar_no_historico
from utils.setup import salvar_dados_execucao, salvar_evolucao_fitness, salvar_resultado, salvar_tempo_execucao, salvar_configuracao
from utils.populacao import gerar_populacao_inicial
from utils.individuo import calcular_fitness, mutar, cruzar, validar_individuo, selecao_torneio


# Algoritmo Genético
def algoritmo_genetico(professores:pd.DataFrame,  turmas:pd.DataFrame, professor_curso:pd.DataFrame, professor_local:pd.DataFrame, geracoes=CONFIG["geracoes"]):
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
        
        for geracao in range(geracoes):
            logging.info(f"Processando geração {geracao + 1}...")
            novos_individuos = []
            #seleção dos pais aleatória ou por torneio
            #pai1, pai2 = random.sample(populacao, 2)
            # Seleção por Torneio
            pai1 = selecao_torneio(populacao, turmas, professores, CONFIG["tamanho_torneio"])
            pai2 = selecao_torneio(populacao, turmas, professores, CONFIG["tamanho_torneio"])
            contador = 0

            # Caso os pais sejam iguais, vamos repetindo até que seja um pai diferente.
            while pai1['individuo'] == pai2['individuo']:
                logging.info(f"pai1: {pai1}")
                logging.info(f"pai2: {pai2}")
                #selecionando um novo pai2
                pai2 = selecao_torneio(populacao, turmas, professores, CONFIG["tamanho_torneio"])
                
                # se após fazer 100 tentativas de selecionar os pais pelo torneio, eles continuarem sendo iguais
                # então selecionar o pai2 de forma aleatoria. Sem a necessidade de ter o melhor fitness
                if contador>=100:
                    logging.info('Selecionando pai2 com random.sample')
                    logging.info(f"-> População: {populacao}")
                    x, pai2 = random.sample(populacao, 2)
                    logging.info(f"-> pai2 random.sample: {pai2}")
                    contador=0
                contador+=1
            
            filho1, filho2 = cruzar(pai1, pai2)

            if random.random() <= CONFIG["prob_mutacao"]:
                logging.info(f"Realizando Mutação na geração {geracao+1}")
                filho1 = mutar(filho1, professores, professor_local, professor_curso, turmas, CONFIG["prob_mutacao"])
                filho2 = mutar(filho2, professores, professor_local, professor_curso, turmas, CONFIG["prob_mutacao"])

            filho1["fitness"] = calcular_fitness(filho1["individuo"], turmas, professores)
            filho2["fitness"] = calcular_fitness(filho2["individuo"], turmas, professores)
            novos_individuos.extend([filho1, filho2])

            # Ajustar e inserir os novos indivíduos na população
            for novo_ind in novos_individuos:        
                # Verificando se o filho gerado já existe na população
                duplicado = any(novo_ind == ind["individuo"] for ind in populacao)
                if duplicado:
                    logging.info(f"Indivíduo Duplicado: {novo_ind['individuo']:.2f}")
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
            if len(populacao) > CONFIG["populacao_inicial"]:
                populacao.sort(key=lambda ind: calcular_fitness(ind["individuo"], turmas, professores), reverse=True)
                populacao = populacao[:CONFIG["populacao_inicial"]]

        # Calcular tempo total de execução
        time_end = datetime.now().strftime('%Y%m%d_%H%M%S')
        tempo_total = time.time() - inicio_execucao
        
        logging.info(f"Tempo total de execução: {(tempo_total/60):.2f} minutos")
        
        arquivo_info = "informacoes_de_execucao_"+str(time_start)+".txt"

        
        salvar_tempo_execucao(f"tempo_execucao_{time_start}.txt", time_end)
        
        # Salvar os resultados
        print('salvando dados da execução')
        salvar_configuracao(arquivo_info, time_start, tempo_total)
        salvar_dados_execucao(historico,f'historico_execucao_{time_start}.csv')
        salvar_dados_execucao(historico_individuos,f'historico_individuos_{time_start}.csv')
        
        print('salvar_evolucao_fitness')
        salvar_evolucao_fitness(historico, f'evolucao_fitness_{time_start}.csv')

        melhor_individuo = max(populacao, key=lambda ind: ind["fitness"])
        pior_individuo = min(populacao, key=lambda ind: ind["fitness"])
        
        print('salvar_resultado')
        salvar_resultado(melhor_individuo["individuo"], f"resultado_final_melhor_{time_start}.csv")
        salvar_resultado(pior_individuo["individuo"], f"resultado_final_pior_{time_start}.csv")

        logging.info("Histórico salvo ao final!")

        file_handler.close()
        logging.getLogger().removeHandler(file_handler)

        return populacao,melhor_individuo, historico
    except Exception as e:
        logging.error(f"Erro na execução do algoritmo")
        logging.error(f"Erro Info: {e}")
        raise{}
