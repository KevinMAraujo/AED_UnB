import os
import sys
import argparse
import random

from utils.csvload import load_csv_data
from utils.algorithm import Backtracker

def main():
    """
    Função principal que carrega os dados, processa as entradas e executa o algoritmo de backtracking.
    """
        # Create an argument parser
    parser = argparse.ArgumentParser(description="Process the number of iteracoes.")
    parser.add_argument("--iteracoes", type=int, required=False, help="Número de iterações")
    parser.add_argument("--cenario", type=str, required=False, help="Cenário (1, 2, 3 ou 4)")

    # Parse the arguments
    args = parser.parse_args()

    # Get the iteracoes value
    iteracoes = args.iteracoes
    cenario = args.cenario

    turmas, professores = load_csv_data(os.path.abspath(os.path.join(os.path.dirname(__file__), '../data')) +'/')

    while cenario not in ['0', '1', '2', '3', '4']:
        print('********** Algoritmo Genetico para seleção de professores nas turmas **********')
        print('-- Deseja executar o algoritmo para qual cenário? Escolha uma opção:')
        print(f'-- 1 - Micro.')
        print(f'-- 2 - Pequeno.')
        print(f'-- 3 - Médio.')
        print(f'-- 4 - Grande/Completo.')
        print(f'-- 0 - Encerrar')
        cenario = input('-- Escolha uma opção:')
        if cenario not in ['0', '1', '2', '3', '4']:
            print('***** Opção invalida, tente novamente.')

    if cenario == '0':
        sys.exit()
    elif cenario == '1':
        turmas = [t for t in turmas if t['IDLOCAL'] == 3]
        professores = [p for p in professores if p['locais'] & {3}]
    elif cenario == '2':
        turmas = [t for t in turmas if t['IDLOCAL'] in {3, 9}]
        professores = [p for p in professores if p['locais'] & {3, 9}]
    elif cenario == '3':
        turmas = [t for t in turmas if t['IDLOCAL'] in {3, 4, 5, 8, 9}  ]
        professores = [p for p in professores if p['locais'] & {3, 4, 5, 8, 9}]
    elif cenario == '4':
        pass

    print(f'Iniciando execução de backtracking em cenário {cenario}:')
    print(f' {len(turmas)} turmas e {len(professores)} professores.')
    print(f' iteracoes {iteracoes}')

    # "Bagunça" lista para obter resultados diferentes em cada execução
    random.shuffle(turmas)
    random.shuffle(professores)

    # Inicializa a alocação
    backtracker = Backtracker(turmas, professores, iteracoes)
    fitness, allocation = backtracker.allocate()


    print('**********************************')
    print(f'Finalizando a execução do item escolhido: {cenario}')
    print(f"Fitness: {fitness}")
    print("Alocação:")
    for prof_id, data in allocation.items():
        print(f"Professor {prof_id}: Turmas {data['turmas']}")


if __name__ == "__main__":
    main()
