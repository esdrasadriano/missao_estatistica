"""Testes da lógica independente da interface Streamlit."""

import math
import unittest

from regras_estatisticas import (
    construir_desafios,
    ler_numero,
    medidas_descritivas,
    probabilidade_binomial,
    probabilidade_positivo_defeito,
    simular_bernoulli,
    simular_binomial,
    simular_dados,
)


class TestRegrasEstatisticas(unittest.TestCase):
    def test_entrada_de_numeros(self):
        self.assertEqual(ler_numero("33,3%"), 33.3)
        self.assertEqual(ler_numero(" 50 "), 50)
        self.assertEqual(ler_numero(".5"), 0.5)
        with self.assertRaises(ValueError):
            ler_numero("abc")
        with self.assertRaises(ValueError):
            ler_numero("1,2,3")

    def test_medidas(self):
        self.assertEqual(
            medidas_descritivas([2, 2, 3, 5, 7]),
            {"media": 3.8, "mediana": 3, "moda": 2},
        )
        with self.assertRaises(ValueError):
            medidas_descritivas([1, 2, 3])

    def test_probabilidades(self):
        self.assertAlmostEqual(probabilidade_binomial(5, 0.5, 2), 10 / 32)
        self.assertEqual(probabilidade_binomial(5, 0.5, 6), 0)
        self.assertAlmostEqual(sum(probabilidade_binomial(10, 0.3, i) for i in range(11)), 1)
        self.assertEqual(probabilidade_positivo_defeito(30, 10), 0.75)
        with self.assertRaises(ValueError):
            probabilidade_positivo_defeito(0, 0)

    def test_simulacoes(self):
        self.assertEqual(simular_dados(13, 20), simular_dados(13, 100)[:20])
        self.assertTrue(all(1 <= x <= 6 for x in simular_dados(13, 100)))
        self.assertEqual(simular_bernoulli(9, 0.5, 30), simular_bernoulli(9, 0.5, 100)[:30])
        self.assertTrue(set(simular_bernoulli(9, 0.4, 100)) <= {0, 1})
        freq = simular_binomial(14, 10, 0.2, 1500)
        self.assertEqual(list(freq.keys()), list(range(11)))
        self.assertEqual(sum(freq.values()), 1500)
        self.assertTrue(all(v >= 0 for v in freq.values()))

    def test_todos_os_desafios(self):
        for semente in range(1000):
            desafio = construir_desafios(semente)
            self.assertEqual(desafio, construir_desafios(semente))
            self.assertEqual(set(desafio), {"evento_dado", "dados_descritivos", "p_moeda", "binomial", "teste"})
            self.assertTrue(set(desafio["evento_dado"]["faces"]) <= set(range(1, 7)))
            self.assertEqual(len(desafio["dados_descritivos"]), 9)
            medidas_descritivas(desafio["dados_descritivos"])
            self.assertTrue(0 < desafio["p_moeda"] < 1)
            b = desafio["binomial"]
            self.assertTrue(0 <= b["k"] <= b["n"])
            self.assertTrue(0 <= probabilidade_binomial(b["n"], b["p"], b["k"]) <= 1)
            t = desafio["teste"]
            self.assertEqual(sum(t.values()), 1000)
            self.assertTrue(all(v >= 0 for v in t.values()))
            self.assertTrue(0 <= probabilidade_positivo_defeito(t["vp"], t["fp"]) <= 1)


if __name__ == "__main__":
    unittest.main()
