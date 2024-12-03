# Otimização da Alocação de Professores em Turmas

Este projeto foi desenvolvido no contexto da disciplina de Algoritmos e Estruturas de Dados da turma de Mestrado em Computação Aplicada da Universidade de Brasília (UnB) 2024/2, e aborda o problema de alocação de professores em turmas com o objetivo de maximizar a receita líquida da instituição de ensino, respeitando diversas restrições operacionais.

## Objetivo Principal do Projeto
Este projeto visa aplicar conhecimentos de **Algoritmos e Estruturas de Dados (AED)** para resolver o problema desafiador de alocação de professores em turmas escolares. O foco é abordar a complexidade do problema, que é NP-completo, e utilizar algoritmos aproximados para desenvolver soluções eficazes e eficientes. Além disso, busca-se:

- **Demonstrar a aplicação prática de conceitos aprendidos em AED**, incentivando o aprendizado significativo.
- **Refletir a escolha do aluno** em explorar um problema autêntico, conectando teoria à prática.
- **Medir e validar o desempenho das soluções** por meio de experimentos científicos e análise de complexidade.


## Requisitos Técnicos do Projeto

- **Linguagem**: Python 3.x
- **Arquitetura**: Modularizado em ao menos dois arquivos.
- **Interface**: Menu de opções amigável para usuários.
- **Validação**: Tratamento robusto de erros e testes de entradas.
- **Documentação**: Código comentado e documentado.
- **Deployment**: Repositório no GitHub.

---
## Descrição do Problema

### Sobre a Instituição
A instituição de ensino estudada está no mercado há 50 anos e capacita mais de 10 mil alunos anualmente. Oferece cursos de idiomas em modalidades presenciais e online, para diversos níveis e públicos (crianças, adolescentes e adultos), além de cursos preparatórios e certificações. Para atender a demanda, a instituição organiza cerca de 800 turmas por semestre, distribuídas entre os dias úteis e sábados.

### Definição do Problema
O desafio é distribuir os professores entre as turmas de forma a:
- Maximizar a receita líquida (receita menos custos);
- Reduzir despesas, como custos de deslocamento, horas pagas com atividades extras para atender a carga horaria minima do professor e sobrecarga dos professores;
- Garantir que as turmas sejam distribuídas de maneira uniforme.

#### Restrições
1. Cada professor possui uma carga horária mínima e máxima semanal.
2. Nenhum professor pode ultrapassar sua carga horária máxima, mas será pago pelo mínimo contratado mesmo que não atinja essa carga.
3. Professores não podem ser alocados a mais de uma turma ao mesmo tempo.
4. O custo por hora-aula varia por professor e não pode ultrapassar a receita mínima da turma.
5. Algumas turmas ou cursos exigem professores específicos devido a habilidades ou disponibilidade.

## NP-Completude do Problema
O problema pertence à classe NP, pois:
- É possível verificar uma solução candidata em tempo polinomial.
- Ele pode ser reduzido do Problema da Mochila Multidimensional (MKP), que é NP-completo.

A redução do MKP para este problema consiste em:
- **Itens**: Professores.
- **Dimensões**: Turmas.
- **Peso**: Horas alocadas.
- **Capacidade**: Demanda de horas por turma.
- **Valor**: Receita líquida da alocação.

Assim, o problema é pelo menos tão difícil quanto o MKP, o que comprova sua NP-completude.

## Metodologia
1. **Revisão da Literatura**
2. **Modelagem do Problema**
3. **Implementação dos Algoritmos**
4. **Testes e Validação**

### 1.Revisão Literária
Foram revisados trabalhos que exploram soluções para problemas semelhantes, incluindo:
- Algoritmos genéticos.
- Heurísticas específicas como busca por força bruta como *BackTracking*.

### 2.Modelagem do Problema
Em Desenvolvimento

### 3.Implementação dos Algoritmos

1. **Backtracking**:
   - Resolve instâncias pequenas e médias de forma exata.
   - Explora todas as combinações possíveis, respeitando restrições.

2. **Algoritmo Genético (AG)**:
   - Heurística para instâncias maiores.
   - Utiliza operações de cruzamento, mutação e seleção para buscar soluções eficientes.
   - Mede a qualidade das soluções através de funções de *fitness* que consideram receita líquida e viabilidade.

#### Algoritmo de Backtracking
- **Objetivo**: Buscar soluções ótimas para instâncias menores.
- **Método**:
  - Exploração exaustiva das combinações de alocação.
  - Verificação de restrições e maximização da receita líquida.
Em Desenvolvimento

#### Algoritmo Genético (AG)
- **Objetivo**: Resolver instâncias grandes, priorizando eficiência.
- **Componentes**:
  - **População Inicial**: Geração de soluções iniciais viáveis.
  - **Cruzamento e Mutação**: Garantir diversidade e explorar o espaço de busca.
  - **Função Fitness**: Avaliar receitas líquidas das alocações.
  - **Seleção por Torneio**: Escolha de melhores indivíduos.
- **Registro de Métricas**:
  - Diversidade da população.
  - Histórico de evolução.
- **Geração inicial**: População criada com soluções aleatórias viáveis.
- **Avaliação de *fitness***: Calcula a receita líquida, respeitando as restrições.
- **Operadores genéticos**:
  - **Cruzamento**: Combina soluções para criar novas.
  - **Mutação**: Introduz diversidade ao modificar soluções.
- **Seleção**: Utiliza torneios para escolher as melhores soluções para a próxima geração.

### Métricas Monitoradas


#### Avaliação do Algoritmo Genético
As métricas devem avaliar tanto a qualidade da solução quanto o desempenho computacional.

##### 1. Métricas para Qualidade da Solução
  * Fitness Médio e Melhor Fitness:
  * Fitness médio por geração.
  * Melhor fitness encontrado ao final.
  
##### 2. Diversidade da População:
  * Avaliar a diversidade genética para garantir que o AG explore bem o espaço de soluções.

##### 3. Respeito às Restrições:
  * Percentual de indivíduos válidos em cada geração.
  * Percentual de turmas alocadas corretamente.

##### 4. Grau de Otimização (Lucro Líquido):
  * Valor final da função objetivo: receita - custos.

##### 5. Métricas para Desempenho Computacional
* Tempo de Execução:Tempo total do AG para convergir para uma solução ou atingir o limite de gerações.
Convergência:
* Número de gerações até atingir o fitness ideal ou estabilidade (mudança mínima em X gerações).

#### Avaliação do Algoritmo de Backtracking
##### 1. Métricas para Qualidade da Solução
  * Soluções Exatas: Comparar se a solução é ótima (ou seja, fitness máximo).
##### 2. Viabilidade:
  * Verificar se todas as restrições foram respeitadas (percentual de turmas corretamente alocadas).

##### 3. Métricas para Desempenho Computacional
* Tempo de Execução: Medir o tempo para resolver o problema completo.
* Número de Estados Visitados: Quantidade de combinações exploradas pelo backtracking.
* Eficiência de Poda: Percentual de estados podados graças à aplicação de restrições durante a busca.

#### Comparação entre AG e BT
####
* Fitness do AG vs solução do BT.
* Tempo de execução.
* Percentual de turmas corretamente alocadas.
* Média de Distribuição das Turmas por Professor
* Desvio Médio da Distribuição das Turmas por Professor

##### 1. Métricas de Qualidade
* Qualidade da Solução: Fitness do AG vs fitness da solução do BT (se o AG chegou perto da solução ótima).
* Respeito às Restrições: Percentual de turmas alocadas corretamente em ambos.

##### 2. Métricas de Desempenho
  * Tempo de Execução: Comparar o tempo necessário para resolver o problema.
  * Escalabilidade: Teste os dois algoritmos com volumes de dados variados (veja a seção de roteiro de testes).

## Testes

Os testes incluirão:

- **Métricas de avaliação**:
  - Receita líquida final.
  - Tempo de execução.
  - Taxa de soluções viáveis encontradas.

1. **Avaliação de Complexidade**:
   - Comparação analítica das soluções exata e heurística.
   - Estudo da escalabilidade em instâncias crescentes.
2. **Medidas de Desempenho**:
   - Taxa de convergência para soluções viáveis.
   - Tempo de execução e qualidade da solução.
3. **Validação Científica**:
   - Resultados apresentados com níveis e intervalos de confiança.
   - Análise de métricas como diversidade populacional no AG.


### Roteiro de Testes e Tamanho dos Dados
#### Cenários de Teste
Tamanho de Dados:
  * **Micro:** Selecionar apenas o local 3 para analise (pequeno número de turmas e professores), apenas 23 turmas.
  * **Pequeno:** Selecionar apenas o local 3 e 9 para analise (pequeno número de turmas e professores), apenas 61 turmas.
  * **Médio:** Selecionar os locais 3,4,5,8 e 9 para analise. Corresponde a 415 registros (51% do total aproximadamente).
  * **Grande:** 816 registros (toda a base).
Configurações de Regras:
Altere restrições de carga horária e permissões (como CHMAX ou locais/cursos disponíveis).
Execuções com Variabilidade:

Testar o AG com diferentes tamanhos de população e taxas de mutação.
Testar BT com diferentes heurísticas de ordenação (ex.: priorizar turmas maiores).

#### Roteiro de Teste
##### 1. Executar AG:
Rodar o AG por um número fixo de gerações para cada cenário.
Registrar métricas: fitness, tempo, diversidade, convergência.

##### 2. Executar BT:
Resolver o problema com a mesma configuração.
Registrar métricas: tempo, número de estados visitados, eficiência de poda.

##### 3. Comparar Resultados:
* Fitness do AG vs solução do BT.
* Tempo de execução.
* Percentual de turmas corretamente alocadas.
* Média de Distribuição das Turmas por Professor
* Desvio Médio da Distribuição das Turmas por Professor




------

## Resultados Esperados
1. Um algoritmo baseado em heurística que:
   - Resolva instâncias grandes de forma eficiente.
   - Forneça soluções válidas e próximas ao ótimo em termos de receita líquida.
2. Comparação de desempenho entre o backtracking e o AG.
3. Documentação clara das etapas, resultados e limitações.

- Demonstração de **vantagens práticas e teóricas** da abordagem heurística frente ao algoritmo exato.
- **Engajamento público** por meio de:
  - Apresentação de em sala.
  - Publicação de um artigo científico com os resultados.
  - Disponibilização do Trabalho no Github

## Trabalhos Correlatos
- [1] Babaei, H., Karimpour, J., and Hadidi, A. *A survey of approaches for university course timetabling problem*.  
- [2] Andrade, P. R. d. L., Steiner, M. T. A., and Goes, A. R. T. *Optimization in timetabling in schools using a mathematical model*.  
- [3] Tan, J. S., Goh, S. L., Kendall, G., and Sabar, N. R. *A survey of the state-of-the-art of optimisation methodologies in school timetabling problems*.  



**Professor**: Edison Ishikawa

**Desenvolvedores**: Adam Victor Nazareth Brandizzi, Edinei Coelho Ferreira, Giselle Dias Mendonça, Kevin Martins Araújo e Rita de Cássia Xavier
   
**Universidade de Brasília (UnB)** - Programa de Pós-Graduação em Computação Aplicada  
