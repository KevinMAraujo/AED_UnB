import pandas as pd
import matplotlib.pyplot as plt

def visualizar_evolucao_fitness(evolucao_fitness, desvio_padrao:float=None, nome_fig:str=None):
  """
  Plota a evolução do fitness ao longo das gerações.

  Args:
      historico (list): Lista contendo os dados do histórico
  """
  if nome_fig == None:
    nome_fig = 'evolução_fitness'

  df = pd.read_csv(evolucao_fitness)


  fig, ax1 = plt.subplots(figsize=(10, 6))

  fitness_maximo = df["fitness_melhor"].max()
  fitness_medio = df["fitness_medio"].max()
  fitness_min = df["fitness_pior"].max()

  ax1.plot(df["geracao"], df["fitness_melhor"], label=f"Fitness Máximo: {fitness_maximo:.2f}", color="green")
  ax1.plot(df["geracao"], df["fitness_medio"], label=f"Fitness Médio: {fitness_medio:.2f}", color="blue")
  ax1.plot(df["geracao"], df["fitness_pior"], label=f"Fitness Mínimo: {fitness_min:.2f}", color="red")
  ax1.set_xlabel("Geração")
  ax1.set_ylabel("Fitness")
  ax1.set_title("Evolução do Fitness ao Longo das Gerações")
  ax1.legend(loc="upper left")
  ax1.grid(True)

  diversidade_max = df["diversidade"].max()
  diversidade_min = df["diversidade"].min()

  ax2 = ax1.twinx()
  ax2.plot(df["geracao"], df["diversidade"], label=f"Diversidade- Max: {diversidade_max:.2f} - Min: {diversidade_min:.2f}", color="orange", linestyle="--")
  ax2.set_ylabel("Diversidade")
  ax2.legend(loc="center right")

  #plt.show()
  plt.close()


def visualizar_evolucao_populacao(arquivo_historico:str=None, nome_fig:str=None):
  """
  Plota a evolução do fitness ao longo das gerações.

  Args:
      arquivo_historico (str): Nome do arquivo a ser lido
  """
  if arquivo_historico is None:
    print("Não foi informado o nome do arquivo")
    raise

  if nome_fig == None:
    nome_fig = 'historico_populacao'

  df = pd.read_csv(arquivo_historico)

  colunas_necessarias = {'geracao','fitness', 'diversidade'}
  if not colunas_necessarias.issubset(df.columns):
    print(f"Erro: As colunas {colunas_necessarias} não foram encontradas no arquivo.")
    print("Colunas disponíveis:", df.columns)
    raise


  df_agg = df.groupby('geracao').agg(
      fitness_min=('fitness','min'),
      fitness_media=('fitness','mean'),
      fitness_max=('fitness','max'),
      fitness_std=('fitness',lambda x: x.std(ddof=0)),
      diversidade=('diversidade','mean')
  ).reset_index()

  df_agg_inicial = df[(df['geracao']==0)].groupby('geracao').agg(
      fitness_min=('fitness','min'),
      fitness_media=('fitness','mean'),
      fitness_max=('fitness','max'),
      fitness_std=('fitness',lambda x: x.std(ddof=0)),
      diversidade=('diversidade','mean')
  ).reset_index()

  max_geracao = df['geracao'].max()

  df_agg_final = df[(df['geracao']==max_geracao)].groupby('geracao').agg(
      fitness_min=('fitness','min'),
      fitness_media=('fitness','mean'),
      fitness_max=('fitness','max'),
      fitness_std=('fitness',lambda x: x.std(ddof=0)),
      diversidade=('diversidade','mean')
  ).reset_index()

  fig, ax1 = plt.subplots(figsize=(8, 5))
  ax1.plot(df_agg["geracao"], df_agg["fitness_max"], label=f"Fitness Máximo: {df_agg_inicial['fitness_max'].min():.2f} - {df_agg_final['fitness_max'].max():.2f}", color="green")
  ax1.plot(df_agg["geracao"], df_agg["fitness_media"], label=f"Fitness Médio: {df_agg_inicial['fitness_media'].min():.2f} - {df_agg_final['fitness_media'].max():.2f}", color="blue")
  ax1.plot(df_agg["geracao"], df_agg["fitness_min"], label=f"Fitness Mínimo: {df_agg_inicial['fitness_min'].min():.2f} - {df_agg_final['fitness_min'].max():.2f}", color="red")
  ax1.set_xlabel("Geração")
  #fig.gca().set_axis_off()
  ax1.set_ylabel("Fitness")
  ax1.set_title("Evolução do Fitness ao Longo das Gerações")
  ax1.legend(loc="upper left")
  ax1.grid(True)

  #criando o segundo eixo y para apresentar os dados da diversidade
  ax2 = ax1.twinx()
  ax2.plot(df_agg["geracao"], df_agg["diversidade"], label=f"Diversidade- Inicial: {df_agg_inicial['diversidade'].min():.2f} - Final: {df_agg_final['diversidade'].max():.2f}", color="orange", linestyle="--")
  ax2.set_ylabel("")
  ax2.tick_params(axis='y', left=False, right=False, labelleft=False, labelright=False)
  ax2.legend(loc="center right")


  #criando o segundo eixo y para apresentar os dados da diversidade
  ax3 = ax1.twinx()
  ax3.plot(df_agg["geracao"], df_agg["fitness_std"], label=f"Desvio Padrão: {df_agg_inicial['fitness_std'].min():.2f} - {df_agg_final['fitness_std'].max():.2f}", color="purple", linestyle="-.")
  ax3.set_ylabel("")
  ax3.tick_params(axis='y', left=False, right=False, labelleft=False, labelright=False)
  ax3.legend(loc="lower left")

  plt.savefig(nome_fig)
  #plt.show()
  plt.close()