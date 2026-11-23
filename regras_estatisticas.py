"""Regras matemáticas e simulações para o jogo educacional Missão Estatística.

Implementação reconstruída para atender à interface esperada por
``jogo_estatistica.py``. Usa somente a biblioteca padrão do Python.
Cada simulação tem uma semente: a mesma semente produz resultados reproduzíveis.
"""

from __future__ import annotations

from collections import Counter
from math import comb, isfinite
from random import Random
from statistics import mean, median
import re


def ler_numero(texto: str) -> float:
    """Converte respostas como '33,3', '33.3' e '33,3%' em floats.

    O sinal de porcentagem apenas identifica a unidade informada pelo aluno;
    não divide o valor por 100, pois as respostas no jogo já são em %.
    """
    entrada = str(texto).strip().replace("\u00a0", "").replace(" ", "")
    if entrada.endswith("%"):
        entrada = entrada[:-1]
    if not re.fullmatch(r"[+-]?(?:\d+(?:[.,]\d+)?|[.,]\d+)", entrada):
        raise ValueError("Digite um número, como 33,3 ou 50%.")
    resultado = float(entrada.replace(",", "."))
    if not isfinite(resultado):
        raise ValueError("O número deve ser finito.")
    return resultado


def medidas_descritivas(valores: list[int] | tuple[int, ...]) -> dict[str, float | int]:
    """Calcula média, mediana e moda única dos dados fornecidos."""
    if not valores:
        raise ValueError("A lista de dados não pode estar vazia.")
    contagens = Counter(valores)
    maior_frequencia = max(contagens.values())
    modas = [numero for numero, frequencia in contagens.items() if frequencia == maior_frequencia]
    if len(modas) != 1:
        raise ValueError("A amostra possui mais de uma moda; a missão requer moda única.")
    return {"media": mean(valores), "mediana": median(valores), "moda": modas[0]}


def probabilidade_binomial(n: int, p: float, k: int) -> float:
    """P(X=k), para X ~ Binomial(n,p)."""
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n deve ser um inteiro não negativo.")
    if not 0 <= p <= 1:
        raise ValueError("p deve estar entre 0 e 1.")
    if not isinstance(k, int) or isinstance(k, bool):
        raise ValueError("k deve ser inteiro.")
    if k < 0 or k > n:
        return 0.0
    return comb(n, k) * p**k * (1 - p) ** (n - k)


def probabilidade_positivo_defeito(vp: int, fp: int) -> float:
    """P(defeito | positivo) = verdadeiros positivos / todos os positivos."""
    if vp < 0 or fp < 0:
        raise ValueError("As contagens não podem ser negativas.")
    if vp + fp == 0:
        raise ValueError("Não há resultados positivos para calcular a proporção.")
    return vp / (vp + fp)


def simular_dados(semente: int, quantidade: int) -> list[int]:
    """Obtém faces 1,...,6 de um dado justo, com reposição."""
    if quantidade < 0:
        raise ValueError("quantidade não pode ser negativa.")
    gerador = Random(semente)
    return [gerador.randint(1, 6) for _ in range(quantidade)]


def simular_bernoulli(semente: int, p: float, quantidade: int) -> list[int]:
    """Retorna 1 para sucesso e 0 para fracasso em ensaios independentes."""
    if not 0 <= p <= 1:
        raise ValueError("p deve estar entre 0 e 1.")
    if quantidade < 0:
        raise ValueError("quantidade não pode ser negativa.")
    gerador = Random(semente)
    return [int(gerador.random() < p) for _ in range(quantidade)]


def simular_binomial(semente: int, n: int, p: float, quantidade: int) -> dict[int, int]:
    """Simula lotes Binomial(n,p); retorna frequências para k=0,...,n."""
    if n < 0 or quantidade < 0:
        raise ValueError("n e quantidade não podem ser negativos.")
    if not 0 <= p <= 1:
        raise ValueError("p deve estar entre 0 e 1.")
    gerador = Random(semente)
    contagens = {k: 0 for k in range(n + 1)}
    for _ in range(quantidade):
        defeituosos = sum(gerador.random() < p for _ in range(n))
        contagens[defeituosos] += 1
    return contagens


def construir_desafios(semente: int) -> dict:
    """Cria dados coerentes e variados para as cinco missões de uma partida.

    - Missão 1: evento em um dado equilibrado.
    - Missão 2: nove medições de tempo, com moda única.
    - Missão 3: probabilidade conhecida para ensaios de Bernoulli.
    - Missão 4: parâmetros de uma Binomial, com evento plausível.
    - Missão 5: tabela de confusão com exatamente 1.000 peças.
    """
    gerador = Random(semente)

    eventos = [
        {"descricao": "obter um número par", "faces": (2, 4, 6)},
        {"descricao": "obter um número ímpar", "faces": (1, 3, 5)},
        {"descricao": "obter um número primo", "faces": (2, 3, 5)},
        {"descricao": "obter um número maior que 4", "faces": (5, 6)},
        {"descricao": "obter um número menor que 3", "faces": (1, 2)},
        {"descricao": "obter a face 6", "faces": (6,)},
    ]
    evento = gerador.choice(eventos).copy()

    moda = gerador.randint(5, 12)
    outros = gerador.sample([numero for numero in range(3, 19) if numero != moda], 6)
    dados = [moda, moda, moda, *outros]
    gerador.shuffle(dados)

    p_moeda = gerador.choice([0.3, 0.4, 0.5, 0.6, 0.7])

    n = gerador.choice([8, 10, 12, 15])
    p = gerador.choice([0.1, 0.2, 0.25, 0.3, 0.4])
    k_central = int((n + 1) * p)
    k = max(0, min(n, k_central + gerador.choice([-1, 0, 1])))

    defeituosas = gerador.choice([80, 100, 120, 150, 200])
    sensibilidade = gerador.choice([0.80, 0.85, 0.90, 0.95])
    especificidade = gerador.choice([0.92, 0.95, 0.96, 0.98])
    vp = round(defeituosas * sensibilidade)
    fn = defeituosas - vp
    normais = 1000 - defeituosas
    fp = round(normais * (1 - especificidade))
    vn = normais - fp

    return {
        "evento_dado": evento,
        "dados_descritivos": dados,
        "p_moeda": p_moeda,
        "binomial": {"n": n, "p": p, "k": k},
        "teste": {"vp": vp, "fp": fp, "fn": fn, "vn": vn},
    }
