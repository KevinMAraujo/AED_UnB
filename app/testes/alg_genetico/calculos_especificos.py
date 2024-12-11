import os
import pandas as pd
import numpy as np
import scipy.stats as stats

def intervalo_confianca(cenario:str, fitness:list):# Resultados do melhor fitness para cada execução do AG
    
    n_execucoes = len(fitness)
    
    nivel_confianca = 0.95 # Nível de confiança desejado (95%)

    media = np.mean(resultados)
    desvio_padrao = np.std(resultados, ddof=1) #desvio padrão, ddof=1 para amostra

    # erro padrão da média
    erro_padrao = desvio_padrao / np.sqrt(n_execucoes)

    # Determinar o valor crítico (t) da distribuição t-Student
    # Como a amostra é n< 30, então usamos o valor crítico 𝑡 da distribuição 𝑡-Student, considerando o grau de liberdade 𝑛−1
    t_critico = stats.t.ppf((1 + nivel_confianca) / 2, df=n_execucoes - 1)

    # Calcular o intervalo de confiança
    margem_erro = t_critico * erro_padrao
    intervalo_confianca = (media - margem_erro, media + margem_erro)

    return {
        "cenario":cenario,
        "media":media,
        "desvio_padrao":desvio_padrao,
        "erro_padrao":erro_padrao,
        "nivel_confianca": nivel_confianca,
        "intervalo_de_confiança_": [round(intervalo_confianca[0],2), round(intervalo_confianca[1])]
    }

def melhor_fitness(nome_cenario:str, arquivo_path:str):
    df = pd.read_csv(arquivo_path)
    colunas_necessarias = {'geracao','fitness', 'diversidade'}
    if not colunas_necessarias.issubset(df.columns):
        print(f"Erro: As colunas {colunas_necessarias} não foram encontradas no arquivo.")
        print("Colunas disponíveis:", df.columns)
        raise
    tipo_execucao = ''
    n_teste = ''
    if nome_cenario.startswith("full_"):
        tipo_execucao = 'full'
        n_teste = nome_cenario.replace("full_",'')
    elif nome_cenario.startswith("medio_"):
        tipo_execucao = 'medio'
        n_teste = nome_cenario.replace("medio_",'')
    elif nome_cenario.startswith("pequeno_"):
        tipo_execucao = 'pequeno'
        n_teste = nome_cenario.replace("pequeno_",'')
    elif nome_cenario.startswith("micro_"):
        tipo_execucao = 'micro'
        n_teste = nome_cenario.replace("micro_",'')
    else:
        print(f"Erro: Cenário não mapeado - {nome_cenario}")
        raise

    fitness = df['fitness'].max()

    return {
        "tipo": tipo_execucao,
        "teste": n_teste,
        "fitness": fitness
    }

  
diretorio = os.path.abspath(os.path.join(os.path.dirname(__file__)))
#file_path = os.path.join(diretorio, nome_arquivo)

resultados_testes = []

for subpasta, x, arquivos in os.walk(diretorio):
    for arquivo in arquivos:
        print(f"Arquivo: {arquivo}")
        if arquivo.endswith(".csv"):                        
            caminho_arquivo = os.path.join(subpasta, arquivo)
            
            if arquivo.startswith("evolucao_fitness_"):
                pass
            elif arquivo.startswith("historico_execucao_"):                
                resultados_testes.append(melhor_fitness)            

df_resultados_testes = pd.DataFrame(resultados_testes)
resultados = []
cenario = ['full','medio','pequeno','micro']
for c in cenario:
    filtro = (df_resultados_testes["tipo"]==c)
    resultados.append(intervalo_confianca(c, df_resultados_testes['fitness'][filtro]))

df_resultados = pd.DataFrame(resultados)
df_resultados.to_csv(os.path.join(diretorio, "resultados_intervalo_confianca.csv"), index=False)     

                
                
