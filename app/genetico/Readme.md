# Algoritmo Genético para Otimização de Alocação de Professores

Este diretório é apresenta a estrutura do código do Algoritmo Genético criado para a resolução do problema de otimização da alocação de professores em turmas escolares, considerando restrições e objetivos específicos. 

Temos dois modos de execução: 
* **manual** (através do arquivo `main.py`) e 
* **automático** (através do arquivo `execucao_auto.py`).

---

## 🔧 Requisitos do Sistema

- **Python 3.8 ou superior**
- Gerenciador de pacotes `pip`

---

## 📦 Instalação

1. **Clone este repositório** em sua máquina local:
   ```bash
   git clone <https://github.com/KevinMAraujo/AED_UnB>
   ```

2. **Crie um ambiente virtual** e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate     # No Linux/Mac
   venv\Scripts\activate        # No Windows
   ```

3. **Instale as dependências** listadas no arquivo `requirements.txt`:
   ```bash
   pip install -r requirements_2.txt
   ```

---

## 🚀 Execução
A aplicação foi desenvolvida para permitir a execução em diferentes cenários, conforme descrito abaixo. O usuário pode optar por executar um único cenário de sua escolha ou realizar a execução para todos os cenários de uma vez.
### Cenários:
* **Micro**: seleção do local 3 para análise, com pequeno número de turmas e professores, sendo apenas 23 turmas;
* **Pequeno**: seleção dos locais 3 e 9 para análise, com reduzido número de turmas e professores, sendo apenas 61 turmas;
* **Médio**: seleção dos locais 3, 4, 5, 8 e 9 para análise, o que corresponde a 415 registros, sendo aproximadamente 51% do total;
* **Grande**: seleção de toda a base de registros, sendo 816 no total.

Essa configuração possibilita ao usuário adaptar a execução da aplicação conforme a complexidade e o volume de dados desejados para análise.

### Opção 1: Execução Manual (`main.py`)
No modo manual, o usuário pode interagir diretamente com o programa e escolher um dos cenários para a execução que deseja realizar.

Para iniciar, execute o arquivo `main.py`:
```bash
python main.py
```

O programa irá guiá-lo através de um menu para selecionar a execução desejada.

---

### Opção 2: Execução Automática (`execucao_auto.py`)
No modo automático, serão realizadas 4 execuções sequencialmente para cada um dos cenários disponíveis, sem que seja necessário a intervenção manual. 


Para iniciar, execute o arquivo `execucao_auto.py`:
```bash
python execucao_auto.py
```

---

## 📂 Estrutura do Projeto

- **`main.py`**: Arquivo principal para execução manual.
- **`execucao_auto.py`**: Arquivo para execução automática.
- **`../../requirements_2.txt`**: Arquivo com todas as dependências necessárias para o projeto.
- **`.env`**: Arquivo com as configurações dos parametros para a execução do algoritmo genético. Nesse arquivo é definido o tamanho da população, a quantidade de gerações, taxa de mutação entre outros.
- **`/utils/load.py`**: Carrega os dados do arquivo .env.
- **`/utils/setup.py`**: Arquivo com as funções relacionadas ao carregamento inicial dos dados, configuração e criação dos arquivos e registros de logs e da informações das execuções.
- **`/utils/professor.py`**: O arquivo contem as funções relacionadas aos professores. Funções como validação de carga horária, verificar disponibilidade do professor, seleção de professores entre outras.
- **`/utils/individuo.py`**: O arquivo contem as funções relacionadas aos individuos da população. Funções como validação do individuo, calculo de fitness, cruzamento, mutação entre outros.
- **`/utils/populacao.py`**: O arquivo contem as funções relacionadas a população, como a geração da população inicial, calculo de diversidade entre outras.
- **`/utils/algoritmo_genetico.py`**: O arquivo contem o codigo para a execução do algoritmo genetico.
- **`/output`**: Local onde é armazenado os resultados gerados pela a execução do programa.


---

## 🧬 Resultados
Após a conclusão da aplicação, ela irá gerar 6 arquivos, sendo eles:
* **`evolucao_fitness_{cenario_escolhido}{tipo_da_execucao}.csv`**: Este arquivo apresenta os dados da geração, valor de fitness minimo, medio e maximo, e o valor da diversidade da geração.
* **`historico_individuos_{cenario_escolhido}{tipo_da_execucao}.csv`**: Este arquivo apresenta os dados de cada um dos individuos criados pelo algoritmo em cada uma das gerações, seu valor de fitness e sua origem da geração, se foi gerado na população inicial, por cruzamento ou por mutação, e tambem indica se o individuo é valido ou não, e o tempo de execução.
* **`resultado_final_melhor_{cenario_escolhido}{tipo_da_execucao}.csv`**: Apresenta as informações de turmas e professor do melhor individuo obtido pelo algoritmo até a ultima geração.
* **`resultado_final_pior_{cenario_escolhido}{tipo_da_execucao}.csv`**:Apresenta as informações de turmas e professor do pior individuo existente na ultima geração.
* **`historico_execucao_{cenario_escolhido}{tipo_da_execucao}.csv`**: é semelhante ao arquivo de historico_individous, porém ele só apresenta os registros dos individuos que são validos e estão na população a cada geração. 
* **`informacoes_de_execucao_{cenario_escolhido}{tipo_da_execucao}.csv`**: Apresenta os valores que foram inseridos no arquivo `.env` no momento da execução do algoritmo.



