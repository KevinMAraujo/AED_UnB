
import pandas as pd
from datetime import datetime
import logging


def selecionar_professor(turma:pd.Series, professores:pd.DataFrame, professor_local:pd.DataFrame, professor_curso:pd.DataFrame, individuo:dict, turmas:pd.DataFrame):
    """
    Seleciona um professor para alocar em uma turma com base na regra de negócio.

    Args:
        turma (Series): Dados da turma.
        professores (DataFrame): Dados dos professores.
        professor_local (DataFrame): Associação professor-local.
        professor_curso (DataFrame): Associação professor-curso.
        individuo (dict): Alocação atual dos professores.
        turmas (DataFrame): Dados das turmas.

    Returns:
        int: ID do professor selecionado, ou 0 se nenhum for encontrado.
    """
    try:
        candidatos = professores[(professores['IDPROFESSOR'].isin(professor_local[professor_local['IDLOCAL'] == turma['IDLOCAL']]['IDPROFESSOR'])) &
                                (professores['IDPROFESSOR'].isin(professor_curso[professor_curso['IDCURSO'] == turma['IDCURSO']]['IDPROFESSOR']))
                                ]
        # embaralha os professores para evitar que sempre o primeiro que aparece é selecionado. 
        # Assim a seleção do professor fica de uma forma mais "aleatoria".
        candidatos = candidatos.sample(frac=1, random_state=None)

        for x, professor in candidatos.iterrows():
            if (validar_carga_horaria(individuo, professor['IDPROFESSOR'], turmas, professores) and verificar_disponibilidade_horario(professor['IDPROFESSOR'], turma, individuo, turmas)):
                return professor['IDPROFESSOR']
        return 0 # Nenhum professor adequado encontrado
    except Exception as e:
        logging.error(f"Erro ao selecionar professor para a turma: {turma}")
        logging.error(f"Erro Info: {e}")
        raise

def verificar_disponibilidade_horario(professor_id:int, turma, individuo:dict, turmas:pd.DataFrame):
    """
    Verifica se o professor está disponível no horário e dias da turma sem choques.
    
    Args:
        professor_id (Int): ID do professor
        turma (Series): Dados da turma.
        individuo (dict): Alocação atual dos professores.
        turmas (DataFrame): Dados das turmas.

    Returns:
        True or False (Bool): Retorna se o professor está disponivel ou não para essa turma.
    """
    try:
        dias_turma = set(map(int, turma['DIASEMANA'].split('-')))
        hora_inicio_turma = datetime.strptime(turma['HORAINICIAL'], '%H:%M')
        hora_final_turma = datetime.strptime(turma['HORAFINAL'], '%H:%M')

        for turma_id, prof_alocado in individuo.items():
            if prof_alocado == professor_id:
                turma_alocada = turmas[turmas['IDTURMA'] == turma_id].iloc[0]
                dias_alocada = set(map(int, turma_alocada['DIASEMANA'].split('-')))
                hora_inicio_alocada = datetime.strptime(turma_alocada['HORAINICIAL'], '%H:%M')
                hora_final_alocada = datetime.strptime(turma_alocada['HORAFINAL'], '%H:%M')

                if dias_turma & dias_alocada:
                    if not (hora_final_turma <= hora_inicio_alocada or hora_inicio_turma >= hora_final_alocada):
                        return False  # Há choque de horário
        return True
    except Exception as e:
        logging.error(f"Erro ao verificar disponibilidade do professor: {professor_id}")
        logging.error(f"Erro ao verificar disponibilidade do professor: Turma {turma}")
        logging.error(f"Erro ao verificar disponibilidade do professor: Individuo {individuo}")
        logging.error(f"Erro Info: {e}")
        raise

def validar_carga_horaria(individuo:dict, professor_id:int, turmas:pd.DataFrame, professores:pd.DataFrame):
    """
    Verifica se a carga horária de um professor está dentro dos limites do professor.

    Args:
        individuo (dict): Dicionário representando a alocação de professores em turmas.
        professor_id (int): ID do professor.
        turmas (DataFrame): Dados das turmas.
        professores (DataFrame): Dados dos professores.

    Returns:
        bool: True se a carga horária está dentro dos limites, caso contrário False.
    """
    try:
        professor = professores[professores['IDPROFESSOR'] == professor_id].iloc[0]
        carga_alocada = sum(
            turmas[turmas['IDTURMA'] == turma_id]['CH_MINUTOS_SEMANA'].iloc[0]
            for turma_id, prof_id in individuo.items() if prof_id == professor_id
            )
        return carga_alocada <= professor['CHMAX']
    except Exception as e:
        logging.error(f"Erro ao validar carga horaria do professor: {professor_id}")
        logging.error(f"Erro ao validar carga horaria do professor: Individuo= {individuo}")
        logging.error(f"Erro Info: {e}")
        raise