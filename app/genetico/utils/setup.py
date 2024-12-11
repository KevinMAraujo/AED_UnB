import pandas as pd
import logging
from datetime import datetime, timedelta
from utils.populacao import calcular_diversidade
import os
from utils.load_env import get_env

def configurar_log(nome_arquivo:str):
    """
    Configura o sistema de logging para salvar logs em um arquivo e exibi-los no console.

    Args:
        nome_arquivo (str): Nome do arquivo onde os logs serão salvos.

    Return:
        FileHandler
    """
    diretorio = os.path.abspath(os.path.join(os.path.dirname(__file__), '../logs'))
    file_path = os.path.join(diretorio, nome_arquivo)
    
    file_handler = logging.FileHandler(file_path, mode='w')  # Salva no arquivo

    log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(log_format)
    logger = logging.getLogger()

    if get_env("LOG_LEVEL") == "DEBUG":
        logger.setLevel(logging.DEBUG)
    elif get_env("LOG_LEVEL") == "INFO":
        logger.setLevel(logging.INFO)
    elif get_env("LOG_LEVEL") == "ERROR":
        logger.setLevel(logging.ERROR)
    
    logger.addHandler(file_handler)

    return file_handler

# Funções para carregar dados
def carregar_dados():
    """
    Carrega os dados de professores, locais, turmas, cursos  a partir de arquivos CSV.

    Returns:
        tuple: DataFrames contendo os dados de professores, turmas, associações curso-professor e local-professor.
    """
    logging.info("Carregando dados...")
    try:
        diretorio = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data'))

        professores_path = os.path.join(diretorio, 'Professores.csv')
        turmas_path = os.path.join(diretorio, 'Turmas.csv')
        professor_curso_path = os.path.join(diretorio, 'ProfessorCurso.csv')
        professor_local_path = os.path.join(diretorio, 'ProfessorLocal.csv')


        if not os.path.exists(professores_path):
            raise FileNotFoundError(f"O arquivo {professores_path} não foi encontrado no caminho especificado.")
        if not os.path.exists(turmas_path):
            raise FileNotFoundError(f"O arquivo {turmas_path} não foi encontrado no caminho especificado.")
        if not os.path.exists(professor_curso_path):
            raise FileNotFoundError(f"O arquivo {professor_curso_path} não foi encontrado no caminho especificado.")
        if not os.path.exists(professor_local_path):
            raise FileNotFoundError(f"O arquivo {professor_local_path} não foi encontrado no caminho especificado.")
        
        professores = pd.read_csv(professores_path, delimiter=";")
        turmas = pd.read_csv(turmas_path, delimiter=";")
        professor_curso = pd.read_csv(professor_curso_path, delimiter=";")
        professor_local = pd.read_csv(professor_local_path, delimiter=";")

        professores['VALORHORA'] = pd.to_numeric(professores['VALORHORA'], errors='coerce')
        professores['CHMIN'] = pd.to_numeric(professores['CHMIN'], errors='coerce')
        professores['CHMAX'] = pd.to_numeric(professores['CHMAX'], errors='coerce')

        turmas['RECEITA_SEMANA'] = pd.to_numeric(turmas['RECEITA_SEMANA'], errors='coerce')
        turmas['CH_MINUTOS_SEMANA'] = pd.to_numeric(turmas['CH_MINUTOS_SEMANA'], errors='coerce')

        logging.info("Dados carregados com sucesso!")
        return professores, turmas, professor_curso, professor_local
    except Exception as e:
        logging.error(f"Erro ao carregar dados: {e}")
        raise

def registrar_no_historico(historico:list, geracao:int, populacao:list):
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
        diretorio = os.path.abspath(os.path.join(os.path.dirname(__file__), '../logs'))
        file_path = os.path.join(diretorio, nome_file)
        
        with open(file_path, "w") as f:
            f.write(f"Tempo total de execução: {tempo_total:.2f} segundos\n")
        logging.info(f"Dados do tempo de execução salvos")
    except Exception as e:    
        logging.info(f'Não foi possivel salvar o arquivo: {file_path}')

# Salvar dados da execução para análise posterior
def salvar_dados_execucao(historico:list, nome_file):
    """
    Salva o histórico da execução e o tempo total em arquivos CSV e TXT.

    Args:
        historico (list): Lista de dicionários com informações sobre fitness, origem e tempo de criação.
    """
    try:
        diretorio = os.path.abspath(os.path.join(os.path.dirname(__file__), '../output'))
        file_path_historico = os.path.join(diretorio, nome_file)
        df = pd.DataFrame(historico)
        df.to_csv(f"{file_path_historico}", index=False)
        logging.info(f"Dados da execução salvos: {file_path_historico} em CSV")
    except Exception as e:    
        logging.info(f'Não foi possivel salvar o arquivo: {file_path_historico}')


# Função para salvar dados da evolução do fitness
def salvar_evolucao_fitness(historico:list, nome_file:str):
    """
    Gera um arquivo CSV contendo a evolução do fitness por geração para análise posterior.

    Args:
    historico (list): Histórico contendo informações sobre fitness, geração e indivíduos.
    """
    try:
        diretorio = os.path.abspath(os.path.join(os.path.dirname(__file__), '../output'))
        file_path_historico = os.path.join(diretorio, nome_file)

        df_historico = pd.DataFrame(historico)
        # Agrupar por geração e calcular o fitness médio, melhor e pior
        evolucao_fitness = df_historico.groupby('geracao').agg(
            fitness_medio=('fitness', 'mean'), 
            fitness_melhor=('fitness', 'max'), 
            fitness_pior=('fitness', 'min'), 
            diversidade=('diversidade','mean')
            ).reset_index()
        evolucao_fitness.to_csv(file_path_historico, index=False)
        logging.info(f"Evolução do fitness salva em {file_path_historico}")
    
    except Exception as e:    
        logging.info(f'Erro ao salvar a evolução do fitness')

# Salvar resultado em CSV
def salvar_resultado(resultado, nome_arquivo:str):
    """
    Salva o resultado da alocação de professores em um arquivo CSV.

    Args:
        resultado (dict): Dicionário com a alocação final de professores por turma.
        nome_arquivo (str): Nome do arquivo CSV a ser criado.
    """
    diretorio = os.path.abspath(os.path.join(os.path.dirname(__file__), '../output'))
    file_path = os.path.join(diretorio, nome_arquivo)
    
    df = pd.DataFrame(list(resultado.items()), columns=['IDTURMA', 'IDPROFESSOR'])
    df.to_csv(file_path, index=False)
    logging.info(f"Resultado salvo no arquivo: {file_path}")

def salvar_configuracao(nome_file:str, time_start:float, tempo_total:float):
    try:
        diretorio = os.path.abspath(os.path.join(os.path.dirname(__file__), '../output'))
        file_path = os.path.join(diretorio, nome_file)

        with open(file_path, "w") as f:
            f.write(f"POPULACAO_INICIAL: {get_env('POPULACAO_INICIAL')}\n")
            f.write(f"GERACOES: {get_env('GERACOES')}\n")
            f.write(f"PROB_MUTACAO: {get_env('PROB_MUTACAO')}\n")
            f.write(f"TAMANHO_TORNEIO: {get_env('TAMANHO_TORNEIO')}\n")
            f.write(f"MAX_AJUSTES: {get_env('MAX_AJUSTES')}\n")
            f.write(f"MAX_TENTATIVAS: {get_env('MAX_TENTATIVAS')}\n")            
            f.write(f"Inicio execucao: "+str(time_start/60)+" minutos\n")
            f.write(f"Tempo total de execucao: "+str(tempo_total/60)+" minutos\n")
            
        logging.info(f"Dados do tempo de execução salvos")
    except Exception as e:    
        logging.info(f'Não foi possivel salvar o arquivo: {file_path}')

        