import pandas as pd
from utils.setup import carregar_dados
from utils.load_env import get_env
from utils.algoritmo_genetico import algoritmo_genetico

def main():
    professores, turmas, professor_curso, professor_local = carregar_dados()
    filtro_micro = (turmas['IDLOCAL']==3)
    micro = turmas[filtro_micro].shape[0]
    filtro_peq = (turmas['IDLOCAL']==3) | (turmas['IDLOCAL']==9)
    pequeno = turmas[filtro_peq].shape[0]

    filtro_medio = (turmas['IDLOCAL']==3) | (turmas['IDLOCAL']==4) | (turmas['IDLOCAL']==5) | (turmas['IDLOCAL']==8) | (turmas['IDLOCAL']==9)
    medio = turmas[filtro_medio].shape[0]
    escolha =''
    while True:
        print('********** Algoritmo Genetico para seleção de professores nas turmas **********')
        print('-- Deseja executar o algoritmo para qual cenário? Escolha uma opção:')
        print(f'-- 1 - Micro (aproximadamente {micro} turmas).')
        print(f'-- 2 - Pequeno (aproximadamente {pequeno} turmas).')
        print(f'-- 3 - Médio (aproximadamente {medio} turmas).')
        print(f'-- 4 - Grande/Completo (aproximadamente {turmas.shape[0]} turmas).')
        print(f'-- 0 - Encerrar')
        escolha = input('-- Escolha uma opção:')
        if escolha == '0':
            break
        elif escolha == '1':
            turmas = turmas[filtro_micro]
        elif escolha == '2':
            turmas = turmas[filtro_peq]
        elif escolha == '3':
            turmas = turmas[filtro_medio]
        elif escolha == '4':
            pass
        else:
            print('***** Opção invalida, tente novamente.')
            continue
        
        print(f'Iniciando execução do algoritmo genetico com {turmas.shape[0]} turmas.')
        populacao, melhor_individuo, historico = algoritmo_genetico(professores, turmas, professor_curso, professor_local,nome_arquivo=None, geracoes=int(get_env('GERACOES')) )
        break
    print('**********************************')
    print(f'Finalizando a execução do item escolhido: {escolha}')
    return populacao, melhor_individuo, historico


if __name__=="__main__":
    main()
