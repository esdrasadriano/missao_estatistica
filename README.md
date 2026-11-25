# 🎲 Missão Estatística — Jogo educacional em Python

Jogo interativo para apresentar conceitos de **Estatística e Probabilidade** a estudantes do Ensino Médio. Construído com [Streamlit](https://streamlit.io/) e Python.

## Conteúdo didático

São cinco missões, de até 20 pontos cada (pontuação máxima: 100):

1. **O laboratório do dado**: probabilidade clássica e frequência relativa.
2. **Detetive dos dados**: média, mediana e moda.
3. **A lei dos grandes números**: simulação de ensaios de Bernoulli.
4. **Controle de qualidade binomial**: probabilidade binomial e simulação de lotes.
5. **O enigma do teste positivo**: probabilidade condicional em uma tabela de contingência.

O jogo mostra resoluções comentadas, gráficos, placar e permite baixar um relatório individual em CSV ao final da partida.

## Estrutura

```text
Missao_Estatistica_Python/
├── jogo_estatistica.py       # Interface Streamlit: 5 missões
├── regras_estatisticas.py    # Simulações, fórmulas e desafios
├── requirements.txt         # Dependências para instalação/deploy
├── README.md                # Este documento
├── .gitignore               # Arquivos que não devem ir ao Git
└── tests/
    └── test_regras_estatisticas.py
```

> **Nota sobre a origem dos arquivos:** `jogo_estatistica.py` foi preservado a partir do arquivo fornecido, com apenas a instrução inicial de execução atualizada para VS Code. Como a versão histórica de `regras_estatisticas.py` não foi disponibilizada, este módulo foi **reconstruído** para atender às funções e aos formatos esperados pela interface. Não é uma cópia comprovada do módulo original.

> A pasta `.venv/` **não vem no ZIP**: ela é criada em cada computador e não é enviada ao GitHub.

## 1. Abrir no VS Code (Ubuntu/Linux)

Extraia o ZIP. No VS Code, escolha **File → Open Folder** e abra a pasta `Missao_Estatistica_Python`.

Abra **Terminal → New Terminal**, confirme que está na raiz do projeto e execute:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

No VS Code, pressione `Ctrl+Shift+P`, escolha **Python: Select Interpreter** e selecione o Python em `.venv/bin/python`.

## 2. Iniciar a aplicação localmente

```bash
python -m streamlit run jogo_estatistica.py
```

Abra o endereço informado no terminal, normalmente `http://localhost:8501`.

Para encerrar o servidor, pressione `Ctrl+C` no terminal.

## 3. Testar as regras matemáticas

Os testes usam somente a biblioteca padrão do Python:

```bash
python -m unittest discover -s tests -v
```

## 4. Publicar no GitHub

Pelo **Source Control** do VS Code, inicialize o repositório (se necessário), crie um commit e publique no GitHub. O `.gitignore` impede que `.venv/` e outros arquivos locais sejam adicionados.

Alternativamente, pelo terminal:

```bash
git init
git add .
git commit -m "Versão inicial da Missão Estatística"
git branch -M main
```

Depois, crie um repositório vazio no GitHub e siga as instruções mostradas para configurar `origin` e fazer o push; não cole comandos com uma URL de repositório fictícia.

## 5. Deploy no Streamlit Community Cloud

1. Acesse https://share.streamlit.io/ e entre com sua conta GitHub.
2. Crie uma aplicação a partir do repositório publicado.
3. Selecione a branch `main`.
4. No campo **Main file path**, informe `jogo_estatistica.py` (se estiver na raiz).
5. Publique. O serviço instalará automaticamente as dependências declaradas em `requirements.txt`.

Depois, atualizações enviadas à branch configurada podem ser implantadas no serviço.

## Observações sobre pontuação

- As respostas são pontuadas uma única vez por missão.
- O progresso é mantido em `st.session_state`, na sessão da interface. **Não é persistido num banco de dados**.
- O CSV é gerado para download pelo próprio aluno; não há armazenamento central de notas.
- Em um cenário escolar, não utilize o CSV como prova de identidade ou nota oficial sem criar controle de autenticação e persistência.

## Requisitos

Python 3.10 ou superior (recomendado: Python 3.12). Instale `streamlit` e `pandas` usando o `requirements.txt`.


---

# 📘 Manual de Uso — Missão Estatística

**Universidade Federal de Sergipe — UFS**  
**Departamento de Estatística e Ciências Atuariais — DECAT**

## 🎮 1. Apresentação

O **Missão Estatística** é um jogo educacional interativo,
desenvolvido em Python com Streamlit, que tem como objetivo
promover a aprendizagem de Estatística e Probabilidade
de maneira lúdica, experimental e investigativa.

O jogo foi desenvolvido especialmente para estudantes
do Ensino Médio, podendo também ser utilizado em disciplinas
introdutórias de Estatística no Ensino Superior.

Por meio de desafios, simulações computacionais, gráficos
e situações-problema, os participantes são estimulados
a desenvolver o raciocínio estatístico.

## 🌐 2. Acesso ao jogo

O jogo pode ser acessado diretamente pelo navegador,
sem necessidade de instalação de programas.

### ▶️ [CLIQUE AQUI PARA JOGAR](https://missao-estatistica-ufs-decat.streamlit.app/)

O aplicativo pode ser utilizado em:

- Computadores;
- Notebooks;
- Tablets;
- Smartphones.

### Requisitos

- Conexão com a internet;
- Navegador atualizado;
- Conhecimentos básicos de matemática;
- Calculadora, quando necessário;
- Papel e lápis para realizar os cálculos.

---

## 🎯 3. Objetivos educacionais

Ao concluir o jogo, espera-se que o estudante seja capaz de:

- Compreender os conceitos básicos de probabilidade;
- Diferenciar probabilidade teórica de frequência relativa;
- Interpretar gráficos e distribuições de frequências;
- Calcular média, mediana e moda;
- Compreender a Lei dos Grandes Números;
- Aplicar a distribuição binomial;
- Compreender a probabilidade condicional;
- Interpretar tabelas de contingência;
- Desenvolver o pensamento crítico e estatístico;
- Aprender por meio de simulações computacionais.

---

## 🕹️ 4. Funcionamento do jogo

O jogo é organizado em cinco missões sequenciais.

Cada missão apresenta um desafio relacionado a um
conceito de Estatística ou Probabilidade.

| Missão | Título | Conteúdo | Pontuação |
| :---: | :--- | :--- | ---: |
| 1 | O laboratório do dado | Probabilidade clássica | 20 |
| 2 | Detetive dos dados | Média, mediana e moda | 20 |
| 3 | A lei dos grandes números | Simulação de experimentos | 20 |
| 4 | Controle de qualidade binomial | Distribuição binomial | 20 |
| 5 | O enigma do teste positivo | Probabilidade condicional | 20 |
| | **TOTAL** | | **100** |

### Regras gerais

1. Leia atentamente o enunciado da missão.
2. Explore os gráficos e as simulações disponíveis.
3. Utilize as dicas quando necessário.
4. Realize os cálculos solicitados.
5. Informe sua resposta.
6. Confira o resultado.
7. Leia a resolução comentada.
8. Avance para a próxima missão.
9. Ao finalizar, baixe seu relatório de desempenho.

> [!IMPORTANT]
> Cada missão é pontuada apenas uma vez por partida.
> Revise sua resposta antes de confirmá-la.

---

## 📊 5. Interface do jogo

A interface apresenta duas áreas principais:

### 5.1. Painel lateral

O painel lateral permite acompanhar:

- Pontuação acumulada;
- Pontuação máxima;
- Barra de progresso;
- Quantidade de missões respondidas;
- Trilha de aprendizagem;
- Opção de reiniciar a partida.

### Indicadores da trilha

| Símbolo | Significado |
| :---: | :--- |
| ✅ | Missão respondida |
| ▶️ | Missão atual |
| 🔒 | Missão ainda não disponível |

### 5.2. Área principal

Na área principal são apresentados:

- Título da missão;
- Situação-problema;
- Gráficos;
- Simulações;
- Campos para respostas;
- Dicas;
- Botões de confirmação;
- Resoluções comentadas.

---

# 🎲 6. Missão 1 — O laboratório do dado

## Objetivo

Compreender a probabilidade clássica e sua relação
com a frequência relativa observada experimentalmente.

## Situação-problema

O jogador recebe um dado equilibrado de seis faces
e deve calcular a probabilidade de ocorrência
de determinado evento.

Os eventos podem envolver:

- Obter um número par;
- Obter um número ímpar;
- Obter um número primo;
- Obter um número maior que quatro;
- Obter um número menor que três;
- Obter a face seis.

## Como jogar

1. Leia o evento apresentado.
2. Utilize os botões de lançamento do dado.
3. Observe a frequência relativa.
4. Analise o gráfico de barras.
5. Calcule a probabilidade teórica.
6. Informe a resposta em porcentagem.
7. Clique em **Conferir resposta**.
8. Leia a resolução comentada.
9. Avance para a próxima missão.

## Simulações disponíveis

| Botão | Função |
| :--- | :--- |
| 🎲 Lançar +20 | Acrescenta 20 lançamentos |
| 🎲 Lançar +100 | Acrescenta 100 lançamentos |
| 🎲 Lançar +500 | Acrescenta 500 lançamentos |

O limite da simulação é de 1.000 lançamentos.

## Fundamentação matemática

Considerando resultados equiprováveis:

$$
P(A)=\frac{n(A)}{n(\Omega)}
$$

Em que:

- $P(A)$ representa a probabilidade do evento;
- $n(A)$ representa o número de casos favoráveis;
- $n(\Omega)$ representa o número de casos possíveis.

## Exemplo ilustrativo

Qual é a probabilidade de obter um número par
no lançamento de um dado equilibrado?

Espaço amostral:

$$
\Omega=\{1,2,3,4,5,6\}
$$

Evento:

$$
A=\{2,4,6\}
$$

Portanto:

$$
P(A)=\frac{3}{6}=0,5
$$

Em porcentagem:

$$
P(A)=50\%
$$

## Pontuação

| Diferença em relação ao valor correto | Pontos |
| :--- | ---: |
| Até 0,60 ponto percentual | 20 |
| Acima de 0,60 até 5 pontos percentuais | 10 |
| Acima de 5 pontos percentuais | 0 |

> [!TIP]
> A frequência relativa observada na simulação não precisa
> ser exatamente igual à probabilidade teórica.

---

# 🔎 7. Missão 2 — Detetive dos dados

## Objetivo

Compreender e calcular as principais medidas
de tendência central.

## Conteúdos abordados

- Média aritmética;
- Mediana;
- Moda;
- Distribuição de frequências;
- Interpretação de gráficos.

## Situação-problema

Uma equipe registrou nove medições de tempo,
expressas em minutos.

O jogador deverá analisar os dados apresentados
e calcular a média, a mediana e a moda.

## Como jogar

1. Observe os nove valores apresentados.
2. Analise o gráfico de frequências.
3. Calcule a média aritmética.
4. Organize os valores em ordem crescente.
5. Identifique a mediana.
6. Identifique o valor mais frequente.
7. Preencha os três campos.
8. Clique em **Conferir cálculos**.
9. Leia a resolução comentada.

## Fundamentação matemática

### Média aritmética

$$
\bar{x}=\frac{\sum_{i=1}^{n}x_i}{n}
$$

### Mediana

Para uma quantidade ímpar de observações:

$$
Md=x_{(\frac{n+1}{2})}
$$

Os dados devem estar previamente ordenados.

### Moda

A moda corresponde ao valor que apresenta
a maior frequência absoluta.

## Exemplo ilustrativo

Considere os seguintes valores:

| Observação | Tempo (minutos) |
| :---: | ---: |
| 1 | 5 |
| 2 | 6 |
| 3 | 7 |
| 4 | 7 |
| 5 | 7 |
| 6 | 8 |
| 7 | 9 |
| 8 | 10 |
| 9 | 13 |

### Cálculo da média

$$
\bar{x}=\frac{5+6+7+7+7+8+9+10+13}{9}
$$

$$
\bar{x}=\frac{72}{9}=8
$$

### Cálculo da mediana

Como existem nove observações:

$$
\frac{9+1}{2}=5
$$

O quinto valor da sequência ordenada é 7.

$$
Md=7
$$

### Cálculo da moda

O valor 7 aparece três vezes.

$$
Mo=7
$$

### Respostas

| Medida | Resultado |
| :--- | ---: |
| Média | 8,00 |
| Mediana | 7 |
| Moda | 7 |

## Pontuação

| Medida | Pontuação |
| :--- | ---: |
| Média correta | 8 |
| Mediana correta | 6 |
| Moda correta | 6 |
| **Total** | **20** |

> [!TIP]
> Informe a média com duas casas decimais.

---

# 🪙 8. Missão 3 — A lei dos grandes números

## Objetivo

Compreender como a frequência relativa se comporta
quando aumentamos o número de observações
de um experimento aleatório.

## Situação-problema

Uma moeda de laboratório possui uma probabilidade
conhecida de apresentar cara.

O jogador deverá simular diferentes quantidades
de lançamentos e observar o comportamento
da frequência relativa.

## Como jogar

1. Observe a probabilidade real apresentada.
2. Movimente o controle de tamanho da amostra.
3. Experimente diferentes números de lançamentos.
4. Observe a frequência relativa de caras.
5. Analise o erro absoluto.
6. Interprete o gráfico.
7. Selecione a alternativa correta.
8. Clique em **Validar interpretação**.
9. Leia a resolução comentada.

## Tamanhos de amostra

O controle permite selecionar amostras entre
20 e 1.000 observações, em incrementos de 20.

## Fundamentação matemática

Seja:

$$
X_i=
\begin{cases}
1, & \text{se ocorrer cara} \\
0, & \text{caso contrário}
\end{cases}
$$

A frequência relativa é:

$$
\hat{p}_n=\frac{1}{n}\sum_{i=1}^{n}X_i
$$

Para ensaios independentes de Bernoulli,
com probabilidade de sucesso constante $p$,
a Lei dos Grandes Números estabelece que:

$$
\hat{p}_n \xrightarrow{P} p
$$

quando:

$$
n\rightarrow\infty
$$

## Exemplo ilustrativo

Considere uma moeda cuja probabilidade
de apresentar cara seja de 60%.

Uma possível simulação seria:

| Lançamentos | Caras | Frequência relativa |
| ---: | ---: | ---: |
| 20 | 14 | 70,0% |
| 100 | 64 | 64,0% |
| 500 | 294 | 58,8% |
| 1.000 | 603 | 60,3% |

Os resultados são ilustrativos e podem variar
entre diferentes partidas.

## Pontuação

| Resultado | Pontuação |
| :--- | ---: |
| Alternativa correta | 20 |
| Alternativa incorreta | 0 |

> [!IMPORTANT]
> A Lei dos Grandes Números não afirma que a frequência
> relativa se aproxima da probabilidade real a cada
> novo lançamento. Podem ocorrer oscilações durante
> o experimento.

---

# 🏭 9. Missão 4 — Controle de qualidade binomial

## Objetivo

Aplicar a distribuição binomial em uma situação
de controle de qualidade industrial.

## Situação-problema

Uma fábrica inspeciona determinado número
de componentes independentes.

Cada componente apresenta uma probabilidade
conhecida de possuir defeito.

O jogador deverá calcular a probabilidade
de encontrar exatamente uma determinada
quantidade de componentes defeituosos.

## Como jogar

1. Identifique o número de componentes inspecionados.
2. Identifique a probabilidade de defeito.
3. Identifique a quantidade de defeituosos solicitada.
4. Observe a simulação de 1.500 lotes.
5. Analise o gráfico de barras.
6. Utilize a função de probabilidade binomial.
7. Converta o resultado para porcentagem.
8. Informe o valor com duas casas decimais.
9. Clique em **Validar cálculo binomial**.
10. Leia a resolução comentada.

## Fundamentação matemática

Seja:

$$
X\sim Binomial(n,p)
$$

A função de probabilidade é dada por:

$$
P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}
$$

Em que:

- $n$: número de componentes;
- $p$: probabilidade de defeito;
- $k$: quantidade de componentes defeituosos;
- $1-p$: probabilidade de um componente não ter defeito.

O coeficiente binomial é:

$$
\binom{n}{k}=\frac{n!}{k!(n-k)!}
$$

## Exemplo ilustrativo

Uma fábrica inspeciona 10 componentes.

A probabilidade de defeito de cada componente
é igual a 20%.

Qual é a probabilidade de encontrar
exatamente dois componentes defeituosos?

Temos:

$$
n=10
$$

$$
p=0,20
$$

$$
k=2
$$

Aplicando a fórmula:

$$
P(X=2)=\binom{10}{2}(0,20)^2(0,80)^8
$$

Calculando o coeficiente binomial:

$$
\binom{10}{2}=\frac{10!}{2!8!}=45
$$

Substituindo:

$$
P(X=2)=45(0,20)^2(0,80)^8
$$

$$
P(X=2)=0,301989888
$$

Em porcentagem:

$$
P(X=2)\approx30,20\%
$$

## Pontuação

| Diferença em relação ao valor correto | Pontos |
| :--- | ---: |
| Até 0,25 ponto percentual | 20 |
| Acima de 0,25 até 2 pontos percentuais | 10 |
| Acima de 2 pontos percentuais | 0 |

> [!NOTE]
> A simulação fornece uma estimativa experimental.
> A distribuição binomial fornece a probabilidade
> teórica solicitada pela missão.

---

# 🧩 10. Missão 5 — O enigma do teste positivo

## Objetivo

Compreender o conceito de probabilidade condicional
por meio da interpretação de tabelas de contingência.

## Situação-problema

Uma fábrica realizou testes em 1.000 componentes
para identificar possíveis defeitos.

O jogador deverá calcular a probabilidade de um
componente ser realmente defeituoso, sabendo
que apresentou resultado positivo no teste.

## Como jogar

1. Analise a tabela apresentada.
2. Identifique os verdadeiros positivos.
3. Identifique os falsos positivos.
4. Determine o total de testes positivos.
5. Calcule a probabilidade condicional.
6. Informe a resposta em porcentagem.
7. Clique em **Resolver enigma**.
8. Leia a resolução comentada.
9. Clique em **Ver resultado final**.

## Fundamentação matemática

A definição de probabilidade condicional é:

$$
P(A|B)=\frac{P(A\cap B)}{P(B)}
$$

Desde que:

$$
P(B)>0
$$

Na situação apresentada:

$$
P(D|+)=\frac{VP}{VP+FP}
$$

Em que:

- $D$: componente realmente defeituoso;
- $VP$: verdadeiros positivos;
- $FP$: falsos positivos;
- $FN$: falsos negativos;
- $VN$: verdadeiros negativos.

## Exemplo ilustrativo

Considere a seguinte tabela:

| Situação real | Teste positivo | Teste negativo | Total |
| :--- | ---: | ---: | ---: |
| Peça defeituosa | 90 | 10 | 100 |
| Peça normal | 45 | 855 | 900 |
| **Total** | **135** | **865** | **1.000** |

Deseja-se calcular:

$$
P(D|+)
$$

Aplicando a fórmula:

$$
P(D|+)=\frac{90}{90+45}
$$

$$
P(D|+)=\frac{90}{135}
$$

$$
P(D|+)=0,6667
$$

Em porcentagem:

$$
P(D|+)\approx66,67\%
$$

## Pontuação

| Diferença em relação ao valor correto | Pontos |
| :--- | ---: |
| Até 0,25 ponto percentual | 20 |
| Acima de 0,25 até 2 pontos percentuais | 10 |
| Acima de 2 pontos percentuais | 0 |

> [!WARNING]
> Não confunda a probabilidade de uma peça ser
> defeituosa dado que seu teste foi positivo
> com a probabilidade de o teste ser positivo
> dado que a peça é defeituosa.
>
> Em geral, essas probabilidades são diferentes.

---

# 🏆 11. Resultado final

Após responder às cinco missões, o jogador
terá acesso à tela de resultados.

Nessa tela serão apresentados:

- Pontuação final;
- Classificação do jogador;
- Pontuação individual por missão;
- Relatório de desempenho;
- Opção de iniciar uma nova partida.

## Classificação

| Pontuação | Classificação |
| :---: | :--- |
| 90 a 100 | 🥇 Mestre da Estatística |
| 70 a 89 | 🥈 Explorador Avançado |
| 50 a 69 | 🥉 Aprendiz Investigador |
| 0 a 49 | 📚 Pesquisador em formação |

## Exemplo de resultado

| Missão | Pontuação obtida | Máximo |
| :--- | ---: | ---: |
| O laboratório do dado | 20 | 20 |
| Detetive dos dados | 20 | 20 |
| A lei dos grandes números | 20 | 20 |
| Controle de qualidade binomial | 10 | 20 |
| O enigma do teste positivo | 20 | 20 |
| **TOTAL** | **90** | **100** |

Nesse exemplo, o jogador recebe a classificação:

**🥇 Mestre da Estatística**

---

# 📥 12. Exportação dos resultados

Ao finalizar a partida, o estudante poderá
baixar seu relatório de desempenho.

Para isso:

1. Conclua as cinco missões.
2. Acesse a tela de resultados.
3. Clique em **Baixar meu resultado (.csv)**.
4. Salve o arquivo em seu dispositivo.

O arquivo recebe o nome:

`resultado_missao_estatistica.csv`

O relatório pode ser aberto em programas como:

- Microsoft Excel;
- LibreOffice Calc;
- Google Planilhas;
- Python;
- R;
- Outros programas de análise de dados.

> [!IMPORTANT]
> O jogo não possui, nesta versão, um banco de dados
> centralizado para armazenamento das notas.
> O estudante deverá salvar seu resultado antes
> de encerrar ou reiniciar a partida.

---

# 🔄 13. Reiniciando o jogo

O jogador poderá começar uma nova partida
a qualquer momento.

Para isso, utilize um dos botões:

- **Reiniciar partida**, no painel lateral;
- **Jogar novamente**, na tela de resultados.

Ao iniciar uma nova partida:

- A pontuação será zerada;
- O progresso anterior será reiniciado;
- Novos desafios poderão ser apresentados;
- Novas simulações serão realizadas.

Essa característica permite utilizar o jogo
diversas vezes como ferramenta de aprendizagem.

---

# 👨‍🏫 14. Orientações para professores

O Missão Estatística pode ser utilizado como
uma ferramenta de aprendizagem ativa, permitindo
que os estudantes construam conhecimentos
por meio da experimentação.

## Possibilidades de utilização

- Introdução aos conceitos de Estatística;
- Introdução à Probabilidade;
- Revisão de conteúdos;
- Atividades individuais;
- Atividades em grupos;
- Oficinas de aprendizagem;
- Avaliação diagnóstica;
- Avaliação formativa;
- Projetos de investigação estatística;
- Feiras de Ciências;
- Atividades de extensão universitária.

## Sugestão de plano de aula

**Duração estimada:** 60 minutos.

| Etapa | Atividade | Duração |
| :--- | :--- | ---: |
| 1 | Apresentação do jogo | 5 min |
| 2 | Missão 1 — Probabilidade clássica | 8 min |
| 3 | Missão 2 — Estatística descritiva | 10 min |
| 4 | Missão 3 — Lei dos Grandes Números | 8 min |
| 5 | Missão 4 — Distribuição binomial | 12 min |
| 6 | Missão 5 — Probabilidade condicional | 10 min |
| 7 | Discussão dos resultados | 7 min |
| | **Total** | **60 min** |

## Metodologias ativas

O jogo pode ser associado às seguintes abordagens:

- Gamificação;
- Aprendizagem baseada em problemas (PBL);
- Aprendizagem baseada em jogos;
- Aprendizagem por investigação;
- Aprendizagem experiencial;
- Experimentação computacional;
- Avaliação formativa.

## Questões para discussão após o jogo

1. Qual foi a missão mais difícil? Por quê?
2. Qual a diferença entre probabilidade teórica
   e frequência relativa?
3. A média representa adequadamente todos os conjuntos
   de dados?
4. Em que situações a mediana pode ser mais adequada
   que a média?
5. Por que a frequência relativa pode oscilar mesmo
   quando aumentamos o tamanho da amostra?
6. Em quais situações reais podemos utilizar
   a distribuição binomial?
7. Um teste positivo garante que uma peça
   seja defeituosa?
8. Como a Estatística pode auxiliar na tomada de decisão?

> [!NOTE]
> A pontuação do jogo deve ser utilizada preferencialmente
> como instrumento de avaliação formativa.
> O relatório CSV não constitui, por si só,
> comprovação de identidade ou autoria do estudante.

---

# ❓ 15. Perguntas frequentes

### Preciso instalar o Python?

Não. A versão on-line pode ser utilizada
diretamente pelo navegador.

### Preciso criar uma conta para jogar?

O código do jogo não possui um sistema próprio
de cadastro ou autenticação de estudantes.
Eventuais restrições de acesso dependem
da configuração da hospedagem.

### Posso utilizar o celular?

Sim. Recomenda-se utilizar um navegador atualizado.
Caso necessário, abra o painel lateral.

### Posso utilizar vírgula nos números decimais?

Sim. O jogo aceita números com vírgula ou ponto decimal.

Exemplos:

- `33,33`
- `33.33`
- `50%`

### Posso utilizar calculadora?

Sim, quando autorizado pelo professor.

O objetivo principal é desenvolver a compreensão
dos conceitos estatísticos.

### Posso utilizar as dicas?

Sim. As dicas fazem parte do processo de aprendizagem
e não provocam desconto na pontuação.

### Posso corrigir uma resposta depois de confirmá-la?

Não. Cada missão recebe pontuação uma única vez
por partida.

### Os desafios são sempre iguais?

Não necessariamente. Os parâmetros e dados dos
desafios são gerados a partir de uma semente
aleatória em cada nova partida.

### Preciso acertar para avançar?

Não. Após uma resposta válida, o jogo apresenta
a resolução comentada e permite avançar,
independentemente da pontuação obtida.

### O jogo pode ser utilizado no Ensino Superior?

Sim. Especialmente em disciplinas introdutórias
de Estatística e Probabilidade.

### O jogo armazena minhas notas?

O progresso é mantido durante a sessão.
Não existe armazenamento permanente das notas
em um banco de dados nesta versão.

---

# 🛠️ 16. Tecnologias utilizadas

| Tecnologia | Finalidade |
| :--- | :--- |
| Python | Linguagem de programação |
| Streamlit | Interface interativa |
| Pandas | Organização e apresentação dos dados |
| Random | Simulações de experimentos aleatórios |
| Math | Cálculos matemáticos |
| Statistics | Medidas estatísticas |
| CSV | Exportação dos resultados |
| GitHub | Versionamento do código-fonte |
| Streamlit Community Cloud | Hospedagem do aplicativo |

---

# 📚 17. Referências bibliográficas

- BUSSAB, Wilton de Oliveira; MORETTIN, Pedro Alberto.
  **Estatística Básica**. 9. ed. São Paulo: Saraiva, 2017.

- MAGALHÃES, Marcos Nascimento; LIMA, Antonio Carlos
  Pedroso de. **Noções de Probabilidade e Estatística**.
  7. ed. São Paulo: EDUSP, 2010.

- ROSS, Sheldon M. **A First Course in Probability**.
  10th ed. Pearson, 2019.

- BRASIL. Ministério da Educação.
  **Base Nacional Comum Curricular**.
  Brasília: MEC, 2018.

- PYTHON SOFTWARE FOUNDATION.
  [Python Documentation](https://docs.python.org/3/).

- STREAMLIT.
  [Streamlit Documentation](https://docs.streamlit.io/).

---

# 🎓 18. Considerações finais

O Missão Estatística busca aproximar os conceitos
matemáticos e estatísticos das experiências práticas
dos estudantes.

A utilização de simulações, gráficos, desafios e
resoluções comentadas permite transformar o estudo
da Estatística em uma experiência interativa,
investigativa e significativa.

Mais importante do que alcançar a pontuação máxima
é compreender os conceitos, interpretar os resultados
e desenvolver a capacidade de tomar decisões
fundamentadas em dados.

---

<div align="center">

## 🎲 Aceite o desafio!

### Você consegue se tornar um Mestre da Estatística?

[![Jogar Missão Estatística](https://img.shields.io/badge/JOGAR-MISSÃO%20ESTATÍSTICA-0078D4?style=for-the-badge)](https://missao-estatistica-ufs-decat.streamlit.app/)

**Estatística: aprender, experimentar e descobrir.**

**Universidade Federal de Sergipe — UFS**

**Departamento de Estatística e Ciências Atuariais — DECAT**

</div>
