import os
import sys

from utils.csvload import load_csv_data
from utils.algorithm import Backtracker

def main():
    """
    Função principal que carrega os dados, processa as entradas e executa o algoritmo de backtracking.
    """
    turmas, professores = load_csv_data(os.path.abspath(os.path.join(os.path.dirname(__file__), '../data')) +'/')

    escolha =''
    while True:
        print('********** Algoritmo Genetico para seleção de professores nas turmas **********')
        print('-- Deseja executar o algoritmo para qual cenário? Escolha uma opção:')
        print(f'-- 1 - Micro.')
        print(f'-- 2 - Pequeno.')
        print(f'-- 3 - Médio.')
        print(f'-- 4 - Grande/Completo.')
        print(f'-- 0 - Encerrar')
        escolha = input('-- Escolha uma opção:')
        if escolha == '0':
            sys.exit()
        elif escolha == '1':
            turmas = [t for t in turmas if t['IDLOCAL'] == 3]
            professores = [p for p in professores if p['locais'] & {3}]
            break
        elif escolha == '2':
            turmas = [t for t in turmas if t['IDLOCAL'] in {3, 9}]
            professores = [p for p in professores if p['locais'] & {3, 9}]
            break
        elif escolha == '3':
            turmas = [t for t in turmas if t['IDLOCAL'] in {3, 4, 5, 8, 9}  ]
            professores = [p for p in professores if p['locais'] & {3, 4, 5, 8, 9}]
            break
        elif escolha == '4':
            break
        else:
            print('***** Opção invalida, tente novamente.')
            continue

    print(f'Iniciando execução de backtracking com {len(turmas)} turmas e {len(professores)} professores.')

    # Inicializa a alocação
    backtracker = Backtracker(turmas, professores, 1000000)
    fitness, allocation = backtracker.allocate()


    print('**********************************')
    print(f'Finalizando a execução do item escolhido: {escolha}')
    print(f"Fitness: {fitness}")
    print("Alocação:")
    for prof_id, data in allocation.items():
        print(f"Professor {prof_id}: Turmas {data['turmas']}")


if __name__ == "__main__":
    main()
