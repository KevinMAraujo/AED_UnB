import os

from utils.csvload import load_csv_data
from utils.algorithm import backtrack_allocation

def main():
    """
    Função principal que carrega os dados, processa as entradas e executa o algoritmo de backtracking.
    """
    turmas, professores = load_csv_data(os.path.abspath(os.path.join(os.path.dirname(__file__), '../data')) +'/')

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
