import copy
from utils.fitness import calculate_fitness

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
            max_revenue[2] = calculate_fitness(allocation, all_classes, professors)
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
