import csv

from datetime import timedelta

def parse_time(time_str):
    """Converte uma string de horário no formato 'HH:MM' em um objeto timedelta."""
    return timedelta(hours=int(time_str.split(':')[0]), minutes=int(time_str.split(':')[1]))


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
        professor["cursos"] = set(professor_curso.get(professor["IDPROFESSOR"], []))
        professor["locais"] = set(professor_local.get(professor["IDPROFESSOR"], []))

    return turmas, professores
