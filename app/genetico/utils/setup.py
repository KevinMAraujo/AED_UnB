import pandas as pd
import logging
from datetime import datetime, timedelta
from dotenv import load_dotenv

from populacao import calcular_diversidade


import os
load_dotenv()


### DEPOIS JOGAR PARA O .ENV

CONFIG = {
    "populacao_inicial": 30,
    "geracoes": 70,
    "prob_mutacao": 0.1,
    "tamanho_torneio": 3,
    "max_ajustes": 10,
    "max_tentativas_geracao": 100,
    "max_tentativas": 100, # Limite de tentativas para evitar duplicados
    "LOG_LEVEL": "DEBUG"
}

def configurar_log(nome_arquivo:str):
    """
    Configura o sistema de logging para salvar logs em um arquivo e exibi-los no console.

    Args:
        nome_arquivo (str): Nome do arquivo onde os logs serão salvos.

    Return:
        FileHandler
    """

    file_handler = logging.FileHandler(nome_arquivo, mode='w')  # Salva no arquivo

    log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(log_format)
    logger = logging.getLogger()

    if CONFIG(["LOG_LEVEL"]) == "DEBUG":
        logger.setLevel(logging.DEBUG)
    elif CONFIG(["LOG_LEVEL"]) == "INFO":
        logger.setLevel(logging.INFO)
    elif CONFIG(["LOG_LEVEL"]) == "ERROR":
        logger.setLevel(logging.ERROR)
    
    logger.addHandler(file_handler)

    return file_handler

# Funções para carregar dados
def carregar_dados():
    """
    Carrega os dados de professores, locais, turmas, cursos  a partir de arquivos CSV.

    Returns:
        tuple: DataFrames contendo os dados de professores, locais, turmas, cursos, associações curso-professor e local-professor.
    """
    logging.info("Carregando dados...")
    try:
        professores = pd.read_csv('Professores.csv', delimiter=";")
        locais = pd.read_csv('Locais.csv', delimiter=";")
        turmas = pd.read_csv('Turmas.csv', delimiter=";")
        cursos = pd.read_csv('Cursos.csv', delimiter=";")
        professor_curso = pd.read_csv('ProfessorCurso.csv', delimiter=";")
        professor_local = pd.read_csv('ProfessorLocal.csv', delimiter=";")

        professores['VALORHORA'] = pd.to_numeric(professores['VALORHORA'], errors='coerce')
        professores['CHMIN'] = pd.to_numeric(professores['CHMIN'], errors='coerce')
        professores['CHMAX'] = pd.to_numeric(professores['CHMAX'], errors='coerce')

        turmas['RECEITA_SEMANA'] = pd.to_numeric(turmas['RECEITA_SEMANA'], errors='coerce')
        turmas['CH_MINUTOS_SEMANA'] = pd.to_numeric(turmas['CH_MINUTOS_SEMANA'], errors='coerce')

        logging.info("Dados carregados com sucesso!")
        return professores, locais, turmas, cursos, professor_curso, professor_local
    except Exception as e:
        logging.error(f"Erro ao carregar dados: {e}")
        raise




def armazenar_dados_execucao():
    pass

def registrar_no_historico(historico:list, geracao:int, populacao:list, loggin):
    """
    Essa função insere toda a população no historico sempre que um novo individuo é gerado,
    mesmo que esse individuo seja "invalido".
    O objetivo desse registro é avaliar a evolução do fitness por geração ao final da execução do algoritmo.

    Args:
        historico (list): Lista contendo o histórico de execuções.
        geracao (int): Número da geração atual.
        populacao (list): Lista de indivíduos na população atual.

    Returns:
        list: Histórico atualizado.
    """
    try:
        diversidade = calcular_diversidade(populacao)
        for ind in populacao:
            historico.append({
                "fitness": ind["fitness"],
                "origem": ind["origem"],
                "tempo_criacao": ind["tempo_criacao"],
                "geracao": geracao,
                "individuo": ind["individuo"],
                "diversidade": diversidade,
            })
        return historico
    except Exception as e:
        logging.error(f"Erro ao registrar no historico: geracao {geracao}.")
        logging.error(f"Erro Info: {e}")
        raise

def registrar_individuo_no_historico(historico:list, geracao:int, populacao:list, obs='normal'):
    """
    Atualiza o histórico com os dados da população atual.
    Ela está sendo utilizada para inserir apenas um individuo na população,
    por a diversidade vai ser sempre 0, porque estamos usando apenas para um individuo

    Args:
        historico (list): Lista contendo o histórico de execuções.
        geracao (int): Número da geração atual.
        populacao (list): Lista de indivíduos na população atual.

    Returns:
        list: Histórico atualizado.
    """
    logging.info(f"Registrando Geração {geracao} no historico...")
    try:
        diversidade = calcular_diversidade(populacao)
        for ind in populacao:
            historico.append({
                "fitness": ind["fitness"],
                "origem": ind["origem"],
                "tempo_criacao": ind["tempo_criacao"],
                "geracao": geracao,
                "individuo": ind["individuo"],
                "diversidade": diversidade,
                "obs": obs,
            })
        return historico
    except Exception as e:
        logging.error(f"Erro ao carregar dados: {e}")
        raise


def salvar_tempo_execucao(nome_file, tempo_total:float):
    try:
        with open(nome_file, "w") as f:
            f.write(f"Tempo total de execução: {tempo_total:.2f} segundos\n")
        logging.info(f"Dados do tempo de execução salvos")
    except Exception as e:    
        logging.info(f'Não foi possivel salvar o arquivo: {nome_file}')

# Salvar dados da execução para análise posterior
def salvar_dados_execucao(historico:list, nome_file):
    """
    Salva o histórico da execução e o tempo total em arquivos CSV e TXT.

    Args:
        historico (list): Lista de dicionários com informações sobre fitness, origem e tempo de criação.
    """
    try:
        df = pd.DataFrame(historico)
        df.to_csv(f"{nome_file}", index=False)
        logging.info(f"Dados da execução salvos: {nome_file} em CSV")
    except Exception as e:    
        logging.info(f'Não foi possivel salvar o arquivo: {nome_file}')


# Função para salvar dados da evolução do fitness
def salvar_evolucao_fitness(historico:list, nome_file:str):
    """
    Gera um arquivo CSV contendo a evolução do fitness por geração para análise posterior.

    Args:
    historico (list): Histórico contendo informações sobre fitness, geração e indivíduos.
    """
    try:
        df_historico = pd.DataFrame(historico)
        # Agrupar por geração e calcular o fitness médio, melhor e pior
        evolucao_fitness = df_historico.groupby('geracao').agg(
            fitness_medio=('fitness', 'mean'), 
            fitness_melhor=('fitness', 'max'), 
            fitness_pior=('fitness', 'min'), 
            diversidade=('diversidade','mean')
            ).reset_index()
        evolucao_fitness.to_csv(nome_file, index=False)
        logging.info(f"Evolução do fitness salva em {nome_file}")
    
    except Exception as e:    
        logging.info(f'Erro ao salvar a evolução do fitness')

# Salvar resultado em CSV
def salvar_resultado(resultado, nome_arquivo):
    """
    Salva o resultado da alocação de professores em um arquivo CSV.

    Args:
        resultado (dict): Dicionário com a alocação final de professores por turma.
        nome_arquivo (str): Nome do arquivo CSV a ser criado.
    """
    df = pd.DataFrame(list(resultado.items()), columns=['IDTURMA', 'IDPROFESSOR'])
    df.to_csv(nome_arquivo, index=False)
    logging.info(f"Resultado salvo no arquivo: {nome_arquivo}")

def salvar_configuracao(nome_file, time_start, tempo_total):
    try:
        with open(nome_file, "w") as f:
            f.write(f"populacao_inicial: {CONFIG['populacao_inicial']}\n")
            f.write(f"geracoes: {CONFIG['geracoes']}\n")
            f.write(f"prob_mutacao: {CONFIG['prob_mutacao']}\n")
            f.write(f"tamanho_torneio: {CONFIG['tamanho_torneio']}\n")
            f.write(f"max_ajustes: {CONFIG['max_ajustes']}\n")
            f.write(f"max_tentativas: {CONFIG['max_tentativas']}\n")            
            f.write(f"Inicio execução: {time_start:.2f} segundos\n")
            f.write(f"Tempo total de execução: {tempo_total:.2f} segundos\n")
            
        logging.info(f"Dados do tempo de execução salvos")
    except Exception as e:    
        logging.info(f'Não foi possivel salvar o arquivo: {nome_file}')