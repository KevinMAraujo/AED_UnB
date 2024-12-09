import os
from analise_geracao_populacao import visualizar_evolucao_populacao
from analise_individuo import carregar_dados, carregar_dados_resultados, calcular_resultados, gerar_graficos_carga_horario_professor
from analise_individuo import gerar_graficos_quantidade_turmas_professor, gerar_graficos_resultado_liquido_turma

diretorio = os.path.abspath(os.path.join(os.path.dirname(__file__)))
#file_path = os.path.join(diretorio, nome_arquivo)

professores, turmas = carregar_dados()
resultados_gerais = []

for subpasta, x, arquivos in os.walk(diretorio):
    for arquivo in arquivos:
        print(f"Arquivo: {arquivo}")
        if arquivo.endswith(".csv"):            
            
            caminho_arquivo = os.path.join(subpasta, arquivo)
            
            if arquivo.startswith("evolucao_fitness_"):
                pass
            elif arquivo.startswith("historico_execucao_"):
                visualizar_evolucao_populacao(caminho_arquivo, os.path.join(subpasta, arquivo.replace('csv','png')))
                
            elif arquivo.startswith("resultado_final_melhor_") or arquivo.startswith("resultado_final_pior_"):
                resultados_test_1  = carregar_dados_resultados(caminho_arquivo)
                resultados_test_1, carga_horaria_professor_test_1, quantidade_turmas_professor_test_1 = calcular_resultados(resultados_test_1, professores, turmas)
                resultado_liquido_fig, min_rl, media_rl, desvio_rl, max_rl = gerar_graficos_resultado_liquido_turma(resultados_test_1, os.path.join(subpasta, 'resultado_liquido_'+arquivo.replace('.csv','.png')))
                carga_horaria_fig, min_ch, media_ch, desvio_ch, max_ch = gerar_graficos_carga_horario_professor(carga_horaria_professor_test_1, os.path.join(subpasta, 'ch_professor_'+arquivo.replace('.csv','.png')))
                qtd_turmas_fig, min_td, media_td, desvio_td, max_td = gerar_graficos_quantidade_turmas_professor(quantidade_turmas_professor_test_1, os.path.join(subpasta, 'qtd_turmas_professor_'+arquivo.replace('.csv','.png')))
                
                
                
