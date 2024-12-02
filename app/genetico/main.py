import pandas as pd
from utils.setup import carregar_dados, CONFIG
from utils.algoritmo_genetico import algoritmo_genetico


# Executar o algoritmo genético
professores, locais, turmas, cursos, professor_curso, professor_local = carregar_dados()
#melhor_solucao = algoritmo_genetico(professores, locais, turmas, cursos, professor_curso, professor_local, geracoes=2)
populacao, melhor_individuo, historico = algoritmo_genetico(professores, locais, turmas, cursos, professor_curso, professor_local, geracoes=CONFIG['geracoes'])
#algoritmo_genetico(professores, locais, turmas, cursos, professor_curso, professor_local, geracoes=100):