import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Funções para carregar dados
def carregar_dados():
    """
    Carrega os dados de professores, locais, turmas, cursos  a partir de arquivos CSV.

    Returns:
        tuple: DataFrames contendo os dados de professores, turmas, associações curso-professor e local-professor.
    """
    try:
        diretorio = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data'))

        professores_path = os.path.join(diretorio, 'Professores.csv')
        turmas_path = os.path.join(diretorio, 'Turmas.csv')

        if not os.path.exists(professores_path):
            raise FileNotFoundError(f"O arquivo {professores_path} não foi encontrado no caminho especificado.")
        if not os.path.exists(turmas_path):
            raise FileNotFoundError(f"O arquivo {turmas_path} não foi encontrado no caminho especificado.")

        
        professores = pd.read_csv(professores_path, delimiter=";")
        turmas = pd.read_csv(turmas_path, delimiter=";")

        professores['VALORHORA'] = pd.to_numeric(professores['VALORHORA'], errors='coerce')
        professores['CHMIN'] = pd.to_numeric(professores['CHMIN'], errors='coerce')
        professores['CHMAX'] = pd.to_numeric(professores['CHMAX'], errors='coerce')

        turmas['RECEITA_SEMANA'] = pd.to_numeric(turmas['RECEITA_SEMANA'], errors='coerce')
        turmas['CH_MINUTOS_SEMANA'] = pd.to_numeric(turmas['CH_MINUTOS_SEMANA'], errors='coerce')

        return professores, turmas
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        raise

def carregar_dados_resultados(arquivo_resultado):
    resultados = pd.read_csv(arquivo_resultado)
    
    return resultados

def calcular_resultados(resultados, professores, turmas):

    resultados = resultados.merge(turmas, on='IDTURMA', how='left')
    resultados = resultados.merge(professores[['IDPROFESSOR', 'VALORHORA']], on='IDPROFESSOR', how='left')

    resultados['ResultadoLiquido'] = resultados['RECEITA_SEMANA'] - ((resultados['CH_MINUTOS_SEMANA']/60) * resultados['VALORHORA'])

    carga_horaria_professor = resultados.groupby('IDPROFESSOR')['CH_MINUTOS_SEMANA'].sum().reset_index()
    carga_horaria_professor.columns = ['IDPROFESSOR', 'CargaHorariaTotal']

    # Contar o número de turmas por professor
    quantidade_turmas_professor = resultados['IDPROFESSOR'].value_counts().reset_index()
    quantidade_turmas_professor.columns = ['IDPROFESSOR', 'QuantidadeTurmas']

    return resultados, carga_horaria_professor, quantidade_turmas_professor

def gerar_graficos_resultado_liquido_turma(resultados:pd.DataFrame=None, nome_fig:str=None):
    """
    Plota o resultado liquido das turmas.

    Args:
        resultados (Dataframe):
    """
    if resultados is None:
        print("Não foi informado parametro")
        raise

    if nome_fig == None:
        nome_fig = 'resultado_liquido_turmas'


    colunas_necessarias = {'IDTURMA','ResultadoLiquido'}
    if not colunas_necessarias.issubset(resultados.columns):
        print(f"Erro: As colunas {colunas_necessarias} não foram encontradas no arquivo.")
        print("Colunas disponíveis:", resultados.columns)
        raise


    desvio_padrao = round(resultados['ResultadoLiquido'].std(ddof=0),3)
    media = resultados['ResultadoLiquido'].mean()
    min = resultados['ResultadoLiquido'].min()
    resultado_final = resultados['ResultadoLiquido'].sum()
    max = resultados['ResultadoLiquido'].max()
    plt.figure(figsize=(8, 5))
    plt.plot(resultados.sort_values(by='IDTURMA').reset_index()['index'], resultados['ResultadoLiquido'], color='blue')
    plt.plot(max, color='blue', label=f'Maior Resultado Líquido: {max:.2f}')
    plt.axhline(media, color='green', linestyle='--', label=f'Média Resultado Líquido: {media:.2f}')
    plt.axhline(min, color='yellow', linestyle='--', label=f'Menor Resultado Líquido: {min:.2f}')
    plt.axhline(desvio_padrao, color='purple', linestyle='-.', label=f'Desvio Padrão:{desvio_padrao:.2f}')
    plt.title('Resultado Líquido por Turma')
    plt.xlabel('Turmas')
    plt.ylabel('Resultado Líquido')
    plt.legend()
    plt.grid(True)
    plt.savefig(nome_fig)

    #plt.show()
    plt.close()
    return nome_fig, min, media, desvio_padrao,  max

def gerar_graficos_carga_horario_professor(carga_horaria_professor:pd.DataFrame=None, nome_fig:str=None):
    """
    Plota o resultado liquido das turmas.

    Args:
        carga_horaria_professor (Dataframe):
    """
    if carga_horaria_professor is None:
        print("Não foi informado parametro")
        raise

    if nome_fig == None:
        nome_fig = 'carga_horaria_professor.png'


    colunas_necessarias = {'CargaHorariaTotal','IDPROFESSOR'}
    if not colunas_necessarias.issubset(carga_horaria_professor.columns):
        print(f"Erro: As colunas {colunas_necessarias} não foram encontradas no arquivo.")
        print("Colunas disponíveis:", carga_horaria_professor.columns)
        raise

    # remover as turmas sem professor
    filtro = (carga_horaria_professor['IDPROFESSOR']!=0)
    carga_horaria_professor = carga_horaria_professor[filtro]

    min_ch = carga_horaria_professor['CargaHorariaTotal'].min()
    max_ch = carga_horaria_professor['CargaHorariaTotal'].max()
    media_ch = carga_horaria_professor['CargaHorariaTotal'].mean()
    desvio = carga_horaria_professor['CargaHorariaTotal'].std(ddof=0)

    plt.figure(figsize=(8, 5))
    plt.bar(carga_horaria_professor.sort_values(by='IDPROFESSOR').reset_index()['index'], carga_horaria_professor['CargaHorariaTotal'], label='Carga Horária Total')
    plt.axhline(max_ch, color='red', linestyle='--', label=f'Maior CH em minutos: {max_ch:.2f}')
    plt.axhline(media_ch, color='orange', linestyle='--', label=f'CH Média em minutos: {media_ch:.2f}')
    plt.axhline(min_ch, color='yellow', linestyle='--', label=f'Menor CH em minutos: {min_ch:.2f}')
    plt.axhline(desvio, color='purple', linestyle='-.', label=f'Desvio Padrão: {desvio:.2f}')

    plt.title('Carga Horária por Professor')
    plt.xlabel('Index Professores')
    plt.ylabel('Carga Horária Total')
    plt.legend()
    plt.grid(True)
    plt.savefig(nome_fig)
    #plt.show()
    plt.close()
    return nome_fig, min_ch, media_ch, desvio , max_ch

def gerar_graficos_quantidade_turmas_professor(quantidade_turmas_professor:pd.DataFrame=None, nome_fig:str=None):
    """
    Plota o resultado liquido das turmas.

    Args:
        quantidade_turmas_professor (Dataframe):
    """
    if quantidade_turmas_professor is None:
        print("Não foi informado parametro")
        raise

    if nome_fig == None:
        nome_fig = 'quantidade_turmas_professor.png'


    colunas_necessarias = {'QuantidadeTurmas','IDPROFESSOR'}
    if not colunas_necessarias.issubset(quantidade_turmas_professor.columns):
        print(f"Erro: As colunas {colunas_necessarias} não foram encontradas no arquivo.")
        print("Colunas disponíveis:", quantidade_turmas_professor.columns)
        raise

    # remover as turmas sem professor
    filtro = (quantidade_turmas_professor['IDPROFESSOR']!=0)
    quantidade_turmas_professor = quantidade_turmas_professor[filtro]

    min_td = quantidade_turmas_professor['QuantidadeTurmas'].min()
    max_td = quantidade_turmas_professor['QuantidadeTurmas'].max()
    media_td = quantidade_turmas_professor['QuantidadeTurmas'].mean()
    desvio = quantidade_turmas_professor['QuantidadeTurmas'].std(ddof=0)


    plt.figure(figsize=(8, 5))
    plt.bar(quantidade_turmas_professor.sort_values(by='IDPROFESSOR').reset_index()['index'], quantidade_turmas_professor['QuantidadeTurmas'], label='Quantidade de Turmas')
    plt.axhline(max_td, color='red', linestyle='--', label=f'Maior Qtd. de Turmas: {max_td:.2f}')
    plt.axhline(media_td, color='orange', linestyle='--', label=f'Média de Turmas por professor: {media_td:.2f}')
    plt.axhline(min_td, color='yellow', linestyle='--', label=f'Menor Qtd. de Turmas: {min_td:.2f}')
    plt.axhline(desvio, color='purple', linestyle='-.', label=f'Desvio Padrão: {desvio:.2f}')

    plt.title('Quantidade de Turmas por Professor')
    plt.xlabel('Index Professores')
    plt.ylabel('Quantidade de Turmas')
    plt.legend()
    plt.grid(True)
    plt.savefig(nome_fig)
    #plt.show()
    plt.close()
    return nome_fig, min_td, media_td,desvio, max_td