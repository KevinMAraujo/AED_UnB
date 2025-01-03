
# Análise e Discussão dos Resultados

## Introdução
Neste documento, serão apresentados os resultados obtidos a partir da execução e análise de dois algoritmos: o Algoritmo Genético e o Backtracking. O objetivo é discutir os métricas de desempenho, comportamento e eficiência de cada abordagem em diferentes cenários de teste, classificados como MICRO, PEQUENO, MÉDIO e GRANDE.

---

## Algoritmo Genético

### Estrutura de Métricas
As métricas avaliadas para o Algoritmo Genético incluem:

- **Melhor Fitness em Cada Geração**: Análise da evolução do melhor fitness ao longo das gerações.
- **Melhor Fitness Final**: Valor do melhor fitness após a última geração.
- **Tempo de Execução**: Duração total do algoritmo.
- **Diversidade Durante as Gerações**: Métrica que avalia a variação populacional em termos de cromossomos.
- **Média e Mínimo do Fitness por Gerações**: Estatísticas de fitness em cada geração.
- **Desvio Padrão por Geração**: Análise da dispersão dos valores de fitness dentro de uma geração.

### Cenários de Teste
Foram definidos quatro cenários de teste:

1. **MICRO**
2. **PEQUENO**
3. **MÉDIO**
4. **GRANDE**

Para cada cenário, realizamos 4 testes independentes, coletando os resultados e gerando as imagens correspondentes.
#### Cenário Micro:
Abaixo apresentamos os gráficos com a evolução do fitness, fitness minimo e média, desvio padrão e diversidade em cada um dos testes.

##### Micro - Evolução Fitness pelas gerações
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img title="Micro Teste 1" src="assets/img/alg_genetico/historico_execucao_micro_teste_1.png" alt="Micro Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/alg_genetico/historico_execucao_micro_teste_2.png" alt="Micro Teste 2" width="400"/>
    </td>
  </tr>
  <tr>
    <td>
      <p>Teste 3</p><br><img src="assets/img/alg_genetico/historico_execucao_micro_teste_3.png" alt="Micro Teste 3" width="400"/>
    </td>
    <td>
      <p>Teste 4</p><br><img src="assets/img/alg_genetico/historico_execucao_micro_teste_4.png" alt="Micro Teste 4" width="400"/>
    </td>
  </tr>
</table>


##### Analises do melhor e pior individuo ao final da ultima geração
##### Melhor Individuo
##### Micro - Quantidade de Turmas por professor
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img src="assets/img/alg_genetico/qtd_turmas_professor_resultado_final_melhor_micro_teste_1.png" alt="Micro Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/alg_genetico/qtd_turmas_professor_resultado_final_melhor_micro_teste_2.png" alt="Micro Teste 2" width="400"/>
    </td>
  </tr>
  <tr>
    <td>
      <p>Teste 3</p><br><img src="assets/img/alg_genetico/qtd_turmas_professor_resultado_final_melhor_micro_teste_3.png" alt="Micro Teste 3" width="400"/>
    </td>
    <td>
      <p>Teste 4</p><br><img src="assets/img/alg_genetico/qtd_turmas_professor_resultado_final_melhor_micro_teste_4.png" alt="Micro Teste 4" width="400"/>
    </td>
  </tr>
</table>



##### Micro - Carga Horaria por professor
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img src="assets/img/alg_genetico/ch_professor_resultado_final_melhor_micro_teste_1.png" alt="Micro Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/alg_genetico/ch_professor_resultado_final_melhor_micro_teste_2.png" alt="Micro Teste 2" width="400"/>
    </td>
  </tr>
  <tr>
    <td>
      <p>Teste 3</p><br><img src="assets/img/alg_genetico/ch_professor_resultado_final_melhor_micro_teste_3.png" alt="Micro Teste 3" width="400"/>
    </td>
    <td>
      <p>Teste 4</p><br><img src="assets/img/alg_genetico/ch_professor_resultado_final_melhor_micro_teste_4.png" alt="Micro Teste 4" width="400"/>
    </td>
  </tr>
</table>


##### Micro - Resultado Liquido por Turma
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img src="assets/img/alg_genetico/resultado_liquido_resultado_final_melhor_micro_teste_1.png" alt="Micro Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/alg_genetico/resultado_liquido_resultado_final_melhor_micro_teste_2.png" alt="Micro Teste 2" width="400"/>
    </td>
  </tr>
  <tr>
    <td>
      <p>Teste 3</p><br><img src="assets/img/alg_genetico/resultado_liquido_resultado_final_melhor_micro_teste_3.png" alt="Micro Teste 3" width="400"/>
    </td>
    <td>
      <p>Teste 4</p><br><img src="assets/img/alg_genetico/resultado_liquido_resultado_final_melhor_micro_teste_4.png" alt="Micro Teste 4" width="400"/>
    </td>
  </tr>
</table> 

#### Cenário Pequeno:
Abaixo apresentamos os gráficos com a evolução do fitness, fitness minimo e média, desvio padrão e diversidade em cada um dos testes.
##### Pequeno - Evolução Fitness pelas gerações
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img src="assets/img/alg_genetico/historico_execucao_pequeno_teste_1.png" alt="Pequeno Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/alg_genetico/historico_execucao_pequeno_teste_2.png" alt="Pequeno Teste 2" width="400"/>
    </td>
  </tr>
  <tr>
    <td>
      <p>Teste 3</p><br><img src="assets/img/alg_genetico/historico_execucao_pequeno_teste_3.png" alt="Pequeno Teste 3" width="400"/>
    </td>
    <td>
      <p>Teste 4</p><br><img src="assets/img/alg_genetico/historico_execucao_pequeno_teste_4.png" alt="Pequeno Teste 4" width="400"/>
    </td>
  </tr>
</table> 

##### Melhor Individuo
#### Quantidade de Turmas por professor
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img src="assets/img/alg_genetico/qtd_turmas_professor_resultado_final_melhor_pequeno_teste_1.png" alt="Pequeno Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/alg_genetico/qtd_turmas_professor_resultado_final_melhor_pequeno_teste_2.png" alt="Pequeno Teste 2" width="400"/>
    </td>
  </tr>
  <tr>
    <td>
      <p>Teste 3</p><br><img src="assets/img/alg_genetico/qtd_turmas_professor_resultado_final_melhor_pequeno_teste_3.png" alt="Pequeno Teste 3" width="400"/>
    </td>
    <td>
      <p>Teste 4</p><br><img src="assets/img/alg_genetico/qtd_turmas_professor_resultado_final_melhor_pequeno_teste_4.png" alt="Pequeno Teste 4" width="400"/>
    </td>
  </tr>
</table>  



##### Pequeno - Carga Horaria por professor
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img src="assets/img/alg_genetico/ch_professor_resultado_final_melhor_pequeno_teste_1.png" alt="Pequeno Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/alg_genetico/ch_professor_resultado_final_melhor_pequeno_teste_2.png" alt="Pequeno Teste 2" width="400"/>
    </td>
  </tr>
  <tr>
    <td>
      <p>Teste 3</p><br><img src="assets/img/alg_genetico/ch_professor_resultado_final_melhor_pequeno_teste_3.png" alt="Pequeno Teste 3" width="400"/>
    </td>
    <td>
      <p>Teste 4</p><br><img src="assets/img/alg_genetico/ch_professor_resultado_final_melhor_pequeno_teste_4.png" alt="Pequeno Teste 4" width="400"/>
    </td>
  </tr>
</table> 

##### Pequeno - Resultado Liquido por Turma
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img src="assets/img/alg_genetico/resultado_liquido_resultado_final_melhor_pequeno_teste_1.png" alt="Pequeno Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/alg_genetico/resultado_liquido_resultado_final_melhor_pequeno_teste_2.png" alt="Pequeno Teste 2" width="400"/>
    </td>
  </tr>
  <tr>
    <td>
      <p>Teste 3</p><br><img src="assets/img/alg_genetico/resultado_liquido_resultado_final_melhor_pequeno_teste_3.png" alt="Pequeno Teste 3" width="400"/>
    </td>
    <td>
      <p>Teste 4</p><br><img src="assets/img/alg_genetico/resultado_liquido_resultado_final_melhor_pequeno_teste_4.png" alt="Pequeno Teste 4" width="400"/>
    </td>
  </tr>
</table> 


#### Cenário Médio:
Abaixo apresentamos os gráficos com a evolução do fitness, fitness minimo e média, desvio padrão e diversidade em cada um dos testes.

##### Medio - Evolução Fitness pelas gerações
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img src="assets/img/alg_genetico/historico_execucao_medio_teste_1.png" alt="Médio Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/alg_genetico/historico_execucao_medio_teste_2.png" alt="Médio Teste 2" width="400"/>
    </td>
  </tr>
  <tr>
    <td>
      <p>Teste 3</p><br><img src="assets/img/alg_genetico/historico_execucao_medio_teste_3.png" alt="Médio Teste 3" width="400"/>
    </td>
    <td>
      <p>Teste 4</p><br><img src="assets/img/alg_genetico/historico_execucao_medio_teste_4.png" alt="Médio Teste 4" width="400"/>
    </td>
  </tr>
</table> 


##### Analises do melhor e pior individuo ao final da ultima geração
##### Melhor Individuo
##### Médio - Quantidade de Turmas por professor
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img src="assets/img/alg_genetico/qtd_turmas_professor_resultado_final_melhor_medio_teste_1.png" alt="Médio Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/alg_genetico/qtd_turmas_professor_resultado_final_melhor_medio_teste_1.png" alt="Médio Teste 2" width="400"/>
    </td>
  </tr>
  <tr>
    <td>
      <p>Teste 3</p><br><img src="assets/img/alg_genetico/qtd_turmas_professor_resultado_final_melhor_medio_teste_1.png" alt="Médio Teste 3" width="400"/>
    </td>
    <td>
      <p>Teste 4</p><br><img src="assets/img/alg_genetico/qtd_turmas_professor_resultado_final_melhor_medio_teste_1.png" alt="Médio Teste 4" width="400"/>
    </td>
  </tr>
</table> 


##### Médio - Carga Horaria por professor
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img src="assets/img/alg_genetico/ch_professor_resultado_final_melhor_medio_teste_1.png" alt="Médio Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/alg_genetico/ch_professor_resultado_final_melhor_medio_teste_2.png" alt="Médio Teste 2" width="400"/>
    </td>
  </tr>
  <tr>
    <td>
      <p>Teste 3</p><br><img src="assets/img/alg_genetico/ch_professor_resultado_final_melhor_medio_teste_3.png" alt="Médio Teste 3" width="400"/>
    </td>
    <td>
      <p>Teste 4</p><br><img src="assets/img/alg_genetico/ch_professor_resultado_final_melhor_medio_teste_4.png" alt="Médio Teste 4" width="400"/>
    </td>
  </tr>
</table>


##### Médio - Resultado Liquido por Turma
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img src="assets/img/alg_genetico/resultado_liquido_resultado_final_melhor_medio_teste_1.png" alt="Médio Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/alg_genetico/resultado_liquido_resultado_final_melhor_medio_teste_2.png" alt="Médio Teste 2" width="400"/>
    </td>
  </tr>
  <tr>
    <td>
      <p>Teste 3</p><br><img src="assets/img/alg_genetico/resultado_liquido_resultado_final_melhor_medio_teste_3.png" alt="Médio Teste 3" width="400"/>
    </td>
    <td>
      <p>Teste 4</p><br><img src="assets/img/alg_genetico/resultado_liquido_resultado_final_melhor_medio_teste_4.png" alt="Médio Teste 4" width="400"/>
    </td>
  </tr>
</table>


#### Cenário Grande:
Abaixo apresentamos os gráficos com a evolução do fitness, fitness minimo e média, desvio padrão e diversidade em cada um dos testes.

##### Grande - Evolução Fitness pelas gerações
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img src="assets/img/alg_genetico/historico_execucao_full_teste_1.png" alt="Grande Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/alg_genetico/historico_execucao_full_teste_2.png" alt="Grande Teste 2" width="400"/>
    </td>
  </tr>
  <tr>
    <td>
      <p>Teste 3</p><br><img src="assets/img/alg_genetico/historico_execucao_full_teste_3.png" alt="Grande Teste 3" width="400"/>
    </td>
    <td>
      <p>Teste 4</p><br><img src="assets/img/alg_genetico/historico_execucao_full_teste_4.png" alt="G5ande Teste 4" width="400"/>
    </td>
  </tr>
</table>


##### Analises do melhor e pior individuo ao final da ultima geração
##### Melhor Individuo
##### Grande - Quantidade de Turmas por professor
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img src="assets/img/alg_genetico/qtd_turmas_professor_resultado_final_melhor_full_teste_1.png" alt="Grande Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/alg_genetico/qtd_turmas_professor_resultado_final_melhor_full_teste_2.png" alt="Grande Teste 2" width="400"/>
    </td>
  </tr>
  <tr>
    <td>
      <p>Teste 3</p><br><img src="assets/img/alg_genetico/qtd_turmas_professor_resultado_final_melhor_full_teste_3.png" alt="Grande Teste 3" width="400"/>
    </td>
    <td>
      <p>Teste 4</p><br><img src="assets/img/alg_genetico/qtd_turmas_professor_resultado_final_melhor_full_teste_4.png" alt="Grande Teste 4" width="400"/>
    </td>
  </tr>
</table>


##### Grande - Carga Horaria por professor
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img src="assets/img/alg_genetico/ch_professor_resultado_final_melhor_full_teste_1.png" alt="Grande Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/alg_genetico/ch_professor_resultado_final_melhor_full_teste_2.png" alt="Grande Teste 2" width="400"/>
    </td>
  </tr>
  <tr>
    <td>
      <p>Teste 3</p><br><img src="assets/img/alg_genetico/ch_professor_resultado_final_melhor_full_teste_3.png" alt="Grande Teste 3" width="400"/>
    </td>
    <td>
      <p>Teste 4</p><br><img src="assets/img/alg_genetico/ch_professor_resultado_final_melhor_full_teste_4.png" alt="Grande Teste 4" width="400"/>
    </td>
  </tr>
</table>


##### Grande - Resultado Liquido por Turma
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img src="assets/img/alg_genetico/resultado_liquido_resultado_final_melhor_full_teste_1.png" alt="Grande Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/alg_genetico/resultado_liquido_resultado_final_melhor_full_teste_2.png" alt="Grande Teste 2" width="400"/>
    </td>
  </tr>
  <tr>
    <td>
      <p>Teste 3</p><br><img src="assets/img/alg_genetico/resultado_liquido_resultado_final_melhor_full_teste_3.png" alt="Grande Teste 3" width="400"/>
    </td>
    <td>
      <p>Teste 4</p><br><img src="assets/img/alg_genetico/resultado_liquido_resultado_final_melhor_full_teste_4.png" alt="Grande Teste 4" width="400"/>
    </td>
  </tr>
</table>



### Resultados e Discussão
Os principais resultados para cada cenário incluem:

#### Tempo, Desvio Padrão e Diversidade
![Tempo, Desvio Padrão e Diversidade](assets/img/alg_genetico/quadro_resultado_tempo.png)


#### Fitness minimo, médio e máximo
![Fitness minimo, médio e máximo](assets/img/alg_genetico/quadro_resultados_fitness.png)

#### Melhor Individuo Gerado
![Melhor Individuo Gerado](assets/img/alg_genetico/quadro_melhor_individuo.png)



## Backtracking



#### Cenário Grande:
Abaixo apresentamos os gráficos com a evolução do fitness, fitness minimo e média, desvio padrão e diversidade em cada um dos testes.

##### Analises do melhor e pior individuo ao final da ultima geração
##### Melhor Individuo
##### Micro - Quantidade de Turmas por professor 
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img src="assets/img/backtracking/teste_1/qtd_turmas_professor_resultado_melhor_solucao_BT_micro.png" alt="Micro Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/backtracking/teste_2/qtd_turmas_professor_resultado_melhor_solucao_BT_micro.png" alt="Micro Teste 2" width="400"/>
    </td>
  </tr>
</table>


##### Micro - Carga Horaria por professor
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img src="assets/img/backtracking/teste_1/ch_professor_resultado_melhor_solucao_BT_micro.png" alt="Micro Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/backtracking/teste_2/ch_professor_resultado_melhor_solucao_BT_micro.png" alt="Micro Teste 2" width="400"/>
    </td>
  </tr>
</table>


##### Micro - Resultado Liquido por Turma
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img src="assets/img/backtracking/teste_1/resultado_liquido_resultado_melhor_solucao_BT_micro.png" alt="Micro Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/backtracking/teste_2/resultado_liquido_resultado_melhor_solucao_BT_micro.png" alt="Micro Teste 2" width="400"/>
    </td>
  </tr>
</table>


##### Pequeno - Quantidade de Turmas por professor 
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img src="assets/img/backtracking/teste_1/qtd_turmas_professor_resultado_melhor_solucao_BT_Pequeno.png" alt="Pequeno Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/backtracking/teste_2/qtd_turmas_professor_resultado_melhor_solucao_BT_Pequeno.png" alt="Pequeno Teste 2" width="400"/>
    </td>
  </tr>
</table>


##### Pequeno - Carga Horaria por professor
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img src="assets/img/backtracking/teste_1/ch_professor_resultado_melhor_solucao_BT_Pequeno.png" alt="Pequeno Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/backtracking/teste_2/ch_professor_resultado_melhor_solucao_BT_Pequeno.png" alt="Pequeno Teste 2" width="400"/>
    </td>
  </tr>
</table>



##### Pequeno - Resultado Liquido por Turma
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img src="assets/img/backtracking/teste_1/resultado_liquido_resultado_melhor_solucao_BT_Pequeno.png" alt="Pequeno Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/backtracking/teste_2/resultado_liquido_resultado_melhor_solucao_BT_Pequeno.png" alt="Pequeno Teste 2" width="400"/>
    </td>
  </tr>
</table>


##### Médio Teste 1 - Quantidade de Turmas por professor 
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img src="assets/img/backtracking/teste_1/qtd_turmas_professor_resultado_melhor_solucao_BT_medio.png" alt="Médio Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/backtracking/teste_2/qtd_turmas_professor_resultado_melhor_solucao_BT_medio.png" alt="Médio Teste 2" width="400"/>
    </td>
  </tr>
</table>




##### Médio - Carga Horaria por professor
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img src="assets/img/backtracking/teste_1/ch_professor_resultado_melhor_solucao_BT_medio.png" alt="Médio Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/backtracking/teste_2/ch_professor_resultado_melhor_solucao_BT_medio.png" alt="Médio Teste 2" width="400"/>
    </td>
  </tr>
</table>



##### Médio - Resultado Liquido por Turma
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img src="assets/img/backtracking/teste_1/resultado_liquido_resultado_melhor_solucao_BT_medio.png" alt="Médio Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/backtracking/teste_2/resultado_liquido_resultado_melhor_solucao_BT_medio.png" alt="Médio Teste 2" width="400"/>
    </td>
  </tr>
</table>



##### Grande - Quantidade de Turmas por professor 
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img src="assets/img/backtracking/teste_1/qtd_turmas_professor_resultado_melhor_solucao_BT_grande.png" alt="Grande Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/backtracking/teste_2/qtd_turmas_professor_resultado_melhor_solucao_BT_grande.png" alt="Grande Teste 2" width="400"/>
    </td>
  </tr>
</table>



##### Grande - Carga Horaria por professor
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img src="assets/img/backtracking/teste_1/ch_professor_resultado_melhor_solucao_BT_grande.png" alt="Grande Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/backtracking/teste_2/ch_professor_resultado_melhor_solucao_BT_grande.png" alt="Grande Teste 2" width="400"/>
    </td>
  </tr>
</table>


##### Grande - Resultado Liquido por Turma
<table>
  <tr>
    <td>
      <p>Teste 1</p><br><img src="assets/img/backtracking/teste_1/resultado_liquido_resultado_melhor_solucao_BT_grande.png" alt="Grande Teste 1" width="400"/>
    </td>
    <td>
      <p>Teste 2</p><br><img src="assets/img/backtracking/teste_2/resultado_liquido_resultado_melhor_solucao_BT_grande.png" alt="Grande Teste 2" width="400"/>
    </td>
  </tr>
</table>



### Resultados e Discussão
Os principais resultados para cada cenário incluem:

#### Tempo de execução, fitness, estados visitados, podados e eficiência de poda
![Tempo, Desvio Padrão e Diversidade](assets/img/backtracking/quadro_fitness.png)


#### Receita médio, minima, maxima e desvio padrão das turmas
![Fitness minimo, médio e máximo](assets/img/backtracking/quadro_melhor_individuo.png)



---

## Conclusões

- Comparativo entre o Algoritmo Genético e o Backtracking.
  
![Melhor Fitness](assets/img/comparativo_fitness.png)
![Tempo de Execução](assets/img/comparativo_tempo_execucao.png)
![Menor Receita da Turma](assets/img/comparativo_menor_receita.png)
![Maior Receita da Turma](assets/img/comparativo_maior_receita.png)



- Vantagens e desvantagens de cada abordagem em diferentes cenários.

- Implicações para a escolha de um algoritmo dependendo do problema e das restrições.



---

## Referências

- 
