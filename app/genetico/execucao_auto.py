import pandas as pd
from utils.setup import carregar_dados
from utils.load_env import get_env
from utils.algoritmo_genetico import algoritmo_genetico

def main():
    professores, turmas, professor_curso, professor_local = carregar_dados()

    professores, turmas, professor_curso, professor_local = carregar_dados()
    filtro_micro = (turmas['IDLOCAL']==3)
    nome_arquivo = 'micro_teste_1'
    turmas = turmas[filtro_micro]
    populacao, melhor_individuo, historico = algoritmo_genetico(professores, turmas, professor_curso, professor_local, nome_arquivo, geracoes=int(get_env('GERACOES')))
    professores, turmas, professor_curso, professor_local = carregar_dados()
    filtro_micro = (turmas['IDLOCAL']==3)
    nome_arquivo = 'micro_teste_2'
    turmas = turmas[filtro_micro]
    populacao, melhor_individuo, historico = algoritmo_genetico(professores, turmas, professor_curso, professor_local, nome_arquivo, geracoes=int(get_env('GERACOES')))
    professores, turmas, professor_curso, professor_local = carregar_dados()
    filtro_micro = (turmas['IDLOCAL']==3)
    nome_arquivo = 'micro_teste_3'
    turmas = turmas[filtro_micro]
    populacao, melhor_individuo, historico = algoritmo_genetico(professores, turmas, professor_curso, professor_local, nome_arquivo, geracoes=int(get_env('GERACOES')))

    professores, turmas, professor_curso, professor_local = carregar_dados()
    filtro_micro = (turmas['IDLOCAL']==3)
    nome_arquivo = 'micro_teste_4'
    turmas = turmas[filtro_micro]
    populacao, melhor_individuo, historico = algoritmo_genetico(professores, turmas, professor_curso, professor_local, nome_arquivo, geracoes=int(get_env('GERACOES')))

    professores, turmas, professor_curso, professor_local = carregar_dados()
    filtro_peq = (turmas['IDLOCAL']==3) | (turmas['IDLOCAL']==9)
    nome_arquivo = 'pequeno_teste_1'
    turmas = turmas[filtro_peq]
    populacao, melhor_individuo, historico = algoritmo_genetico(professores, turmas, professor_curso, professor_local, nome_arquivo, geracoes=int(get_env('GERACOES')))

    professores, turmas, professor_curso, professor_local = carregar_dados()
    filtro_peq = (turmas['IDLOCAL']==3) | (turmas['IDLOCAL']==9)
    nome_arquivo = 'pequeno_teste_2'
    turmas = turmas[filtro_peq]
    populacao, melhor_individuo, historico = algoritmo_genetico(professores, turmas, professor_curso, professor_local, nome_arquivo, geracoes=int(get_env('GERACOES')))

    professores, turmas, professor_curso, professor_local = carregar_dados()
    filtro_peq = (turmas['IDLOCAL']==3) | (turmas['IDLOCAL']==9)
    nome_arquivo = 'pequeno_teste_3'
    turmas = turmas[filtro_peq]
    populacao, melhor_individuo, historico = algoritmo_genetico(professores, turmas, professor_curso, professor_local, nome_arquivo, geracoes=int(get_env('GERACOES')))

    professores, turmas, professor_curso, professor_local = carregar_dados()
    filtro_peq = (turmas['IDLOCAL']==3) | (turmas['IDLOCAL']==9)
    nome_arquivo = 'pequeno_teste_4'
    turmas = turmas[filtro_peq]
    populacao, melhor_individuo, historico = algoritmo_genetico(professores, turmas, professor_curso, professor_local, nome_arquivo, geracoes=int(get_env('GERACOES')))

    professores, turmas, professor_curso, professor_local = carregar_dados()
    filtro_medio = (turmas['IDLOCAL']==3) | (turmas['IDLOCAL']==4) | (turmas['IDLOCAL']==5) | (turmas['IDLOCAL']==8) | (turmas['IDLOCAL']==9)
    nome_arquivo = 'medio_teste_1'
    turmas = turmas[filtro_medio]
    populacao, melhor_individuo, historico = algoritmo_genetico(professores, turmas, professor_curso, professor_local, nome_arquivo, geracoes=int(get_env('GERACOES')))

    professores, turmas, professor_curso, professor_local = carregar_dados()
    filtro_medio = (turmas['IDLOCAL']==3) | (turmas['IDLOCAL']==4) | (turmas['IDLOCAL']==5) | (turmas['IDLOCAL']==8) | (turmas['IDLOCAL']==9)
    nome_arquivo = 'medio_teste_2'
    turmas = turmas[filtro_medio]
    populacao, melhor_individuo, historico = algoritmo_genetico(professores, turmas, professor_curso, professor_local, nome_arquivo, geracoes=int(get_env('GERACOES')))


    professores, turmas, professor_curso, professor_local = carregar_dados()
    filtro_medio = (turmas['IDLOCAL']==3) | (turmas['IDLOCAL']==4) | (turmas['IDLOCAL']==5) | (turmas['IDLOCAL']==8) | (turmas['IDLOCAL']==9)
    nome_arquivo = 'medio_teste_3'
    turmas = turmas[filtro_medio]
    populacao, melhor_individuo, historico = algoritmo_genetico(professores, turmas, professor_curso, professor_local, nome_arquivo, geracoes=int(get_env('GERACOES')))


    professores, turmas, professor_curso, professor_local = carregar_dados()
    filtro_medio = (turmas['IDLOCAL']==3) | (turmas['IDLOCAL']==4) | (turmas['IDLOCAL']==5) | (turmas['IDLOCAL']==8) | (turmas['IDLOCAL']==9)
    nome_arquivo = 'medio_teste_4'
    turmas = turmas[filtro_medio]
    populacao, melhor_individuo, historico = algoritmo_genetico(professores, turmas, professor_curso, professor_local, nome_arquivo, geracoes=int(get_env('GERACOES')))


    professores, turmas, professor_curso, professor_local = carregar_dados()
    nome_arquivo = 'full_teste_1'
    populacao, melhor_individuo, historico = algoritmo_genetico(professores, turmas, professor_curso, professor_local, nome_arquivo, geracoes=int(get_env('GERACOES')))

    professores, turmas, professor_curso, professor_local = carregar_dados()
    nome_arquivo = 'full_teste_2'
    populacao, melhor_individuo, historico = algoritmo_genetico(professores, turmas, professor_curso, professor_local, nome_arquivo, geracoes=int(get_env('GERACOES')))

    professores, turmas, professor_curso, professor_local = carregar_dados()
    nome_arquivo = 'full_teste_3'
    populacao, melhor_individuo, historico = algoritmo_genetico(professores, turmas, professor_curso, professor_local, nome_arquivo, geracoes=int(get_env('GERACOES')))

    professores, turmas, professor_curso, professor_local = carregar_dados()
    nome_arquivo = 'full_teste_4'
    populacao, melhor_individuo, historico = algoritmo_genetico(professores, turmas, professor_curso, professor_local, nome_arquivo, geracoes=int(get_env('GERACOES')))

if __name__=="__main__":
    main()
