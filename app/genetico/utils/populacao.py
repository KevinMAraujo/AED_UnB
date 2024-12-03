import pandas as pd
import numpy as np
import logging
import time
from utils.professor import selecionar_professor 
#from utils.setup import CONFIG

CONFIG = {
    "populacao_inicial": 5,
    "geracoes": 2,
    "prob_mutacao": 0.1,
    "tamanho_torneio": 3,
    "max_ajustes": 10,
    "max_tentativas_geracao": 1,
    "max_tentativas": 1, # Limite de tentativas para evitar duplicados
    "LOG_LEVEL": "DEBUG"
}
def calcular_diversidade(populacao:list):
    """
    Calcula a diversidade da população com base na variação de genes.

    Args:
        populacao (list): Lista de indivíduos da população.

    Returns:
        float: Diversidade medida como a média do número de genes diferentes entre pares de indivíduos.
    """
    try:
        individuos = [ind["individuo"] for ind in populacao]
        diversidades = []
        for i in range(len(individuos)):
            for j in range(i + 1, len(individuos)):
                dif = sum(1 for key in individuos[i] if individuos[i][key] != individuos[j][key])
                diversidades.append(dif)
        return np.mean(diversidades) if diversidades else 0
    except Exception as e:
        logging.error(f"Erro ao calcular diversidade: populacao: {populacao}")
        logging.error(f"Erro Info: {e}")
        raise

def gerar_populacao_inicial(turmas:pd.DataFrame, professores:pd.DataFrame, professor_local:pd.DataFrame, professor_curso:pd.DataFrame):
    """
    Gera a população inicial do algoritmo genético com alocações de professores nas turmas,
    garantindo que indivíduos duplicados sejam minimizados.

    Args:
        turmas (DataFrame): Dados das turmas.
        professores (DataFrame): Dados dos professores.
        professor_local (DataFrame): Associação professor-local.
        professor_curso (DataFrame): Associação professor-curso.

    Returns:
        list: Lista de indivíduos representando a população inicial.
    """
    try:
        populacao = []
        tam = CONFIG["populacao_inicial"]
        k_max_tentativas = CONFIG.get("max_tentativas", 10)  # Limite de tentativas para evitar duplicados

        logging.info(f"-> Gerando População Inicial --> Tamanho: {tam}")

        for x in range(tam):
            tentativas = 0
            logging.info(f"-> População Inicial -> Individuo --> {x}")
            while True:
                individuo = {}
                logging.info(f"Tentativa: {tentativas}")
                for y, turma in turmas.iterrows():
                    professor_id = selecionar_professor(turma, professores, professor_local, professor_curso, individuo, turmas)
                    individuo[turma['IDTURMA']] = professor_id

                # Verifica se o indivíduo já existe na população
                duplicado = any(individuo == ind["individuo"] for ind in populacao)

                if not duplicado or tentativas >= k_max_tentativas:
                    # Adiciona o indivíduo, mesmo se duplicado, após k_max_tentativas
                    populacao.append({"individuo": individuo, "origem": "Geração Inicial", "tempo_criacao": time.time()})
                    break
                else:                    
                    logging.info(f"-> Tentativa {tentativas} falhou: Indivíduo duplicado.")
                    tentativas += 1

        
        logging.info(f"-> Gerando População Inicial --> Populacao gerada: {populacao}")
        return populacao
    except Exception as e:
        logging.error(f"Erro ao gerar populacao")
        logging.error(f"Erro Info: {e}")
        raise

