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
