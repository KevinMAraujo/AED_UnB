# Função de aptidão
def calculate_fitness(allocation, turmas, professores):
  """
  Calcula a aptidão (fitness) de um indivíduo com base no lucro líquido (receita - custo).

  Args:
      individuo (dict): Dicionário representando a alocação de professores em turmas.
      turmas (DataFrame): Dados das turmas.
      professores (DataFrame): Dados dos professores.

  Returns:
      float: Valor do fitness (lucro líquido).
  """
  fitness = 0
  carga_horaria_por_professor = {}
  individuo = [
      (turma_id, professor_id)
      for professor_id, a in allocation.items()
      for turma_id in a['turmas']
  ]
  for turma_id, professor_id in individuo:
    if professor_id == 0:  # Se nenhum professor for alocado a Receita da Turma será negativa
      fitness -= turma['RECEITA_SEMANA']
      continue

    turma = next(t for t in turmas if t['IDTURMA'] == turma_id)
    professor = next(p for p in professores if p['IDPROFESSOR'] == professor_id)
    custo = (turma['CH_MINUTOS_SEMANA'] / 60) * professor['VALORHORA']
    fitness += turma['RECEITA_SEMANA'] - custo

    # Acumula a carga horária em horas
    carga_horaria_por_professor[professor_id] = carga_horaria_por_professor.get(professor_id, 0) + (turma['CH_MINUTOS_SEMANA'])

  # Penaliza professores com carga horária abaixo do mínimo
  for professor_id, carga_atual in carga_horaria_por_professor.items():
    professor = next(p for p in professores if p['IDPROFESSOR'] == professor_id)
    if carga_atual < professor['CHMIN']:
      diferenca = professor['CHMIN'] - carga_atual
      fitness -= (diferenca/60) * professor['VALORHORA']
    elif carga_atual > professor['CHMAX']:
      diferenca = carga_atual - professor['CHMAX']
      fitness -= (diferenca/60) * (professor['VALORHORA']*2) # o dobro da hora normal do professor por ser uma hora extra

  return fitness
