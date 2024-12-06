import csv
import copy
from datetime import timedelta


def parse_time(time_str):
    """Converte uma string de horário no formato 'HH:MM' em um objeto timedelta."""
    return timedelta(hours=int(time_str.split(':')[0]), minutes=int(time_str.split(':')[1]))


def has_time_conflict(schedule, start, end, days):
    """
    Verifica se um horário (start, end) e os dias conflitam com uma lista de horários já alocados.

    :param schedule: Lista de tuplas (start, end, days) onde days é um conjunto de números dos dias da semana.
    :param start: Horário de início da nova turma.
    :param end: Horário de término da nova turma.
    :param days: Conjunto de números representando os dias da semana da nova turma.
    :return: True se houver conflito, False caso contrário.
    """
    for s, e, existing_days in schedule:
        if start < e and s < end and not days.isdisjoint(existing_days):  # Verifica sobreposição no tempo e interseção nos dias
            return True
    return False


def calculate_class_balance(class_info, professor_hourly_rate):
    """
    Calcula o saldo de uma turma dada a receita e o custo do professor.

    :param class_info: Dicionário com informações da turma.
    :param professor_hourly_rate: Valor por hora do professor.
    :return: Saldo da turma.
    """
    class_hours = class_info["CH_MINUTOS_MES"] / 60
    return class_info["RECEITA"] - (class_hours * professor_hourly_rate)

# Função de aptidão
def calcular_fitness(allocation, turmas, professores):
  """
  Calcula a aptidão (fitness) de um indivíduo com base no lucro líquido (receita - custo).

  Args:
      individuo (dict): Dicionário representando a alocação de professores em turmas.
      turmas (DataFrame): Dados das turmas.
      professores (DataFrame): Dados dos professores.

  Returns:
      float: Valor do fitness (lucro líquido).
  """
  fitness = 0
  carga_horaria_por_professor = {}
  individuo = [
      (turma_id, professor_id)
      for professor_id, a in allocation.items()
      for turma_id in a['turmas']
  ]
  for turma_id, professor_id in individuo:
    if professor_id == 0:  # Se nenhum professor for alocado a Receita da Turma será negativa
      fitness -= turma['RECEITA_SEMANA']
      continue

    turma = next(t for t in turmas if t['IDTURMA'] == turma_id)
    professor = next(p for p in professores if p['IDPROFESSOR'] == professor_id)
    custo = (turma['CH_MINUTOS_SEMANA'] / 60) * professor['VALORHORA']
    fitness += turma['RECEITA_SEMANA'] - custo

    # Acumula a carga horária em horas
    carga_horaria_por_professor[professor_id] = carga_horaria_por_professor.get(professor_id, 0) + (turma['CH_MINUTOS_SEMANA'])

  # Penaliza professores com carga horária abaixo do mínimo
  for professor_id, carga_atual in carga_horaria_por_professor.items():
    professor = next(p for p in professores if p['IDPROFESSOR'] == professor_id)
    if carga_atual < professor['CHMIN']:
      diferenca = professor['CHMIN'] - carga_atual
      fitness -= (diferenca/60) * professor['VALORHORA']
    elif carga_atual > professor['CHMAX']:
      diferenca = carga_atual - professor['CHMAX']
      fitness -= (diferenca/60) * (professor['VALORHORA']*2) # o dobro da hora normal do professor por ser uma hora extra

  return fitness

def backtrack_allocation(all_classes, professors, classes, allocation, max_revenue, current_revenue):
    """
    Resolve o problema de alocação de professores em turmas usando backtracking.

    :param professors: Lista de professores com informações como carga horária e locais.
    :param classes: Lista de turmas disponíveis para alocação.
    :param allocation: Dicionário da alocação atual {professor_id: [turma_id]}.
    :param max_revenue: Receita máxima até o momento.
    :param current_revenue: Receita atual para a solução parcial.
    :return: Receita máxima e a alocação correspondente.
    """
    if not classes:  # Base do backtracking
        if current_revenue > max_revenue[0]:
            max_revenue[0] = current_revenue
            max_revenue[1] = copy.deepcopy(allocation)
            max_revenue[2] = calcular_fitness(allocation, all_classes, professors)
            print(f'solution found {max_revenue[0]:.2f} {max_revenue[2]:.4f}')
        return

    class_info = classes[0]  # Próxima turma
    remaining_classes = classes[1:]

    # Tenta alocar professores possíveis para a turma
    for professor in professors:
        prof_id = professor["IDPROFESSOR"]
        if (prof_id in allocation and has_time_conflict(
                allocation[prof_id]["schedule"],
                class_info["start_time"], class_info["end_time"], class_info["days"])) or \
           (class_info["IDLOCAL"] not in professor["locais"]) or \
           (class_info["IDCURSO"] not in professor["cursos"]):
            continue

        # Calcula o saldo da turma se este professor for alocado
        class_balance = calculate_class_balance(class_info, professor["VALORHORA"])
        allocation[prof_id]["schedule"].append((class_info["start_time"], class_info["end_time"], class_info["days"]))
        allocation[prof_id]["turmas"].append(class_info["IDTURMA"])

        backtrack_allocation(all_classes, professors, remaining_classes, allocation, max_revenue, current_revenue + class_balance)

        # Desfaz a alocação para explorar outras possibilidades
        allocation[prof_id]["schedule"].pop()
        allocation[prof_id]["turmas"].pop()
    # Caso sem alocar a turma
    backtrack_allocation(all_classes, professors, remaining_classes, allocation, max_revenue, current_revenue)

def load_csv_data(prefix=''):
    """Carrega os dados dos arquivos CSV e retorna listas de turmas e professores."""
    turmas = []
    professores = []
    professor_curso = {}
    professor_local = {}

    with open(f"{prefix}Turmas.csv", newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            turmas.append({
                "IDTURMA": int(row["IDTURMA"]),
                "RECEITA": float(row["RECEITA"]),
                "CH_MINUTOS_MES": float(row["CH_MINUTOS_MES"]),
                "CH_MINUTOS_SEMANA": float(row["CH_MINUTOS_SEMANA"]),
                "RECEITA_SEMANA": float(row["RECEITA_SEMANA"]),
                "start_time": parse_time(row["HORAINICIAL"]),
                "end_time": parse_time(row["HORAFINAL"]),
                "days": set(map(int, row["DIASEMANA"].split('-'))),
                "IDLOCAL": int(row["IDLOCAL"]),
                "IDCURSO": int(row["IDCURSO"])
            })

    with open(f"{prefix}Professores.csv", newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            professores.append({
                "IDPROFESSOR": int(row["IDPROFESSOR"]),
                "VALORHORA": float(row["VALORHORA"]),
                "CHMIN": int(row["CHMIN"]),
                "CHMAX": int(row["CHMAX"]),
                "locais": set(),
                "cursos": set()
            })

    with open(f"{prefix}ProfessorCurso.csv", newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            professor_curso.setdefault(int(row["IDPROFESSOR"]), []).append(int(row["IDCURSO"]))

    with open(f"{prefix}ProfessorLocal.csv", newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            professor_local.setdefault(int(row["IDPROFESSOR"]), []).append(int(row["IDLOCAL"]))

    for professor in professores:
        professor["cursos"] = professor_curso.get(professor["IDPROFESSOR"], [])
        professor["locais"] = professor_local.get(professor["IDPROFESSOR"], [])

    return turmas, professores
def main():
    """
    Função principal que carrega os dados, processa as entradas e executa o algoritmo de backtracking.
    """
    turmas, professores = load_csv_data()

    # Inicializa a alocação
    allocation = {prof["IDPROFESSOR"]: {"schedule": [], "turmas": []} for prof in professores}

    max_revenue = [float("-inf"), None, None]  # Armazena a receita máxima e a alocação correspondente
    backtrack_allocation(turmas, professores, turmas, allocation, max_revenue, 0)
    print(f'Exec {exectimes}')
    print(f"Receita máxima: {max_revenue[0]}")
    print("Alocação:")
    for prof_id, data in max_revenue[1].items():
        print(f"Professor {prof_id}: Turmas {data['turmas']}")


if __name__ == "__main__":
    main()
