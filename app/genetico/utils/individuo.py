import pandas as pd
import random
import time
import logging
from .professor import selecionar_professor
from utils.load_env import get_env

def calcular_fitness(individuo:dict, turmas:pd.DataFrame, professores:pd.DataFrame):
    """
    Calcula a aptidão (fitness) de um indivíduo com base no lucro líquido (receita - custo).

    Args:
        individuo (dict): Dicionário representando a alocação de professores em turmas.
        turmas (DataFrame): Dados das turmas.
        professores (DataFrame): Dados dos professores.

    Returns:
        float: Valor do fitness (lucro líquido).
    """
    
    try:
        fitness = 0
        carga_horaria_por_professor = {}

        for turma_id, professor_id in individuo.items():
            if professor_id == 0:  
                # Se nenhum professor for alocado a Receita da Turma será negativa
                fitness -= turma['RECEITA_SEMANA']
                continue

            turma = turmas[turmas['IDTURMA'] == turma_id].iloc[0]
            professor = professores[professores['IDPROFESSOR'] == professor_id].iloc[0]
            custo = (turma['CH_MINUTOS_SEMANA'] / 60) * professor['VALORHORA']
            fitness += turma['RECEITA_SEMANA'] - custo

            # Acumula a carga horária em minutos
            carga_horaria_por_professor[professor_id] = carga_horaria_por_professor.get(professor_id, 0) + (turma['CH_MINUTOS_SEMANA'])

        # Penaliza professores com carga horária abaixo do mínimo
        
        for professor_id, carga_atual in carga_horaria_por_professor.items():
            professor = professores[professores['IDPROFESSOR'] == professor_id].iloc[0]
            if carga_atual < professor['CHMIN']:
                # Deverá ser cobrado o valor que falta da carga horaria do professor para chega na carga horaria minima
                diferenca = professor['CHMIN'] - carga_atual
                fitness -= (diferenca/60) * professor['VALORHORA']
            elif carga_atual > professor['CHMAX']:
                diferenca = carga_atual - professor['CHMAX']
                # o dobro da hora normal do professor por ser uma hora extra
                fitness -= (diferenca/60) * (professor['VALORHORA']*2) 

        return fitness
    except Exception as e:
        logging.error(f"Ocorreu um erro ao calcular a fitness: {individuo}")
        logging.error(f"Erro Info: {e}")
        raise

def validar_individuo(individuo:dict, turmas:pd.DataFrame, professores:pd.DataFrame, professor_local:pd.DataFrame, professor_curso:pd.DataFrame):
    """
    Valida um indivíduo para garantir que as restrições de carga horária maxima, local e cursos sejam atendidas.

    Args:
        individuo (dict): Dicionário representando a alocação de professores em turmas.
        turmas (DataFrame): Dados das turmas.
        professores (DataFrame): Dados dos professores.
        professor_local (DataFrame): Associação professor-local.
        professor_curso (DataFrame): Associação professor-curso.

    Returns:
        Bool: True or False
    """
    try:
        for x, professor in professores.iterrows():
            carga_atual = sum( 
            turmas[turmas['IDTURMA'] == turma_id]['CH_MINUTOS_SEMANA'].iloc[0] 
            for turma_id, prof_id in individuo["individuo"].items() if prof_id == professor['IDPROFESSOR']
            )

            if carga_atual <= professor['CHMAX']:
                turmas_candidatas = turmas[
                    (turmas['IDLOCAL'].isin(professor_local[professor_local['IDPROFESSOR'] == professor['IDPROFESSOR']]['IDLOCAL'])) & 
                    (turmas['IDCURSO'].isin(professor_curso[professor_curso['IDPROFESSOR'] == professor['IDPROFESSOR']]['IDCURSO']))
                    ]
                # valida se a turma que o professor está alocado é permitida pra ele conforme a regra de negócio
                for turma_id, prof_id in individuo["individuo"].items():
                    if prof_id == professor['IDPROFESSOR']:
                        if turma_id not in turmas_candidatas['IDTURMA'].values:
                            return False
            else:
                return False

        return True
    except Exception as e:
        logging.error(f"Erro ao validar individuo: {individuo}")
        logging.error(f"Erro Info: {e}")
        raise

def selecao_torneio(populacao:list, turmas:pd.DataFrame, professores:pd.DataFrame, k=get_env("TAMANHO_TORNEIO") ):
    """
    Seleciona um indivíduo da população usando o método de torneio.

    Args:
    populacao (list): Lista de indivíduos da população.
    turmas (DataFrame): Dados das turmas.
    professores (DataFrame): Dados dos professores.
    k (int): Tamanho do torneio.

    Returns:
    dict: O indivíduo vencedor do torneio.
    """
    try:
        logging.info(f"#### #### #### Iniciando Torneio")
        torneio = random.sample(populacao, k)
        logging.info(f"### -> Participantes do Torneio: {torneio}...")
        melhor = max(torneio, key=lambda ind: calcular_fitness(ind["individuo"], turmas, professores))
        logging.info(f"### -> Melhor do Torneio: {melhor}...")
        return melhor
    except Exception as e:
        logging.error(f"Erro na seleção por torneio")
        logging.error(f"Erro Info: {e}")
        raise

def mutar(individuo:dict, professores:pd.DataFrame, professor_local:pd.DataFrame, professor_curso:pd.DataFrame, turmas:pd.DataFrame, prob_mutacao=get_env("PROB_MUTACAO")):
    """
    Aplica mutação a um indivíduo, alterando a alocação de professores em algumas turmas.

    Args:
    individuo (dict): O indivíduo a ser mutado.
    professores (DataFrame): Dados dos professores.
    professor_local (DataFrame): Associação professor-local.
    professor_curso (DataFrame): Associação professor-curso.
    turmas (DataFrame): Dados das turmas.
    prob_mutacao (float): Probabilidade de mutação por turma.

    Returns:
    dict: O indivíduo mutado.
    """
    try:
        for turma_id in individuo["individuo"].keys():
            if random.random() < prob_mutacao:
                turma = turmas[turmas['IDTURMA'] == turma_id].iloc[0]
                novo_professor = selecionar_professor(turma, professores, professor_local, professor_curso, individuo["individuo"], turmas)
                individuo["individuo"][turma_id] = novo_professor
        individuo["origem"] = "Mutação"
        return individuo
    except Exception as e:
        logging.error(f"Erro na mutacao: individuo: {individuo}")
        logging.error(f"Erro Info: {e}")
        raise

def cruzar(pai1:dict, pai2:dict):
    """
    Realiza o cruzamento entre dois indivíduos para gerar dois filhos.

    Args:
        pai1 (dict): Primeiro indivíduo.
        pai2 (dict): Segundo indivíduo.

    Returns:
        tuple: Dois novos indivíduos gerados a partir do cruzamento.
    """
    try:
        ponto_corte = random.randint(1, len(pai1["individuo"]) - 1)
        filho1 = dict(list(pai1["individuo"].items())[:ponto_corte] + list(pai2["individuo"].items())[ponto_corte:])
        filho2 = dict(list(pai2["individuo"].items())[:ponto_corte] + list(pai1["individuo"].items())[ponto_corte:])
        return {"individuo": filho1, "origem": "Cruzamento", "tempo_criacao": time.time()}, \
            {"individuo": filho2, "origem": "Cruzamento", "tempo_criacao": time.time()}
    except Exception as e:
        logging.error(f"Erro ao realizar o cruzameto - pai1: {pai1}")
        logging.error(f"Erro ao realizar o cruzameto - pai2: {pai2}")
        logging.error(f"Erro Info: {e}")
        raise

