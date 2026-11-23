"""Jogo educacional de Estatística e Probabilidade usando Streamlit.

Execução (no terminal do VS Code): python -m streamlit run jogo_estatistica.py
"""

import csv
from io import StringIO
import secrets
from collections import Counter

import pandas as pd
import streamlit as st

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

st.set_page_config(page_title="Missão Estatística", page_icon="🎲", layout="wide")

st.markdown(
    """
<style>
.stApp {background: #f8fafc; color: #18263b;}
.hero {background: linear-gradient(110deg, #142b51, #165d85); padding: 28px 32px;
       border-radius: 18px; color: white; margin-bottom: 18px;}
.hero h1 {font-size: 2.6rem; margin: 0 0 8px 0; color: white;}
.hero p {color: #e0f3ff; font-size: 1.04rem; margin: 0;}
.mission {color: #06758a; font-weight: 700; letter-spacing: .06em;
          font-size: .84rem; margin-bottom: 5px;}
.info-box {padding: 15px 18px; border-left: 4px solid #0c93ac;
           background: #eaf8fb; border-radius: 8px; margin: 10px 0 15px;}
.score-pill {background: #e7f4ee; border-radius: 12px; padding: 14px 20px;
             font-weight: 700; margin-bottom: 10px;}
</style>
""",
    unsafe_allow_html=True,
)

TITULOS = (
    "O laboratório do dado",
    "Detetive dos dados",
    "A lei dos grandes números",
    "Controle de qualidade binomial",
    "O enigma do teste positivo",
)


def criar_partida():
    semente = secrets.randbelow(2**31)
    return {
        "semente": semente,
        "desafios": construir_desafios(semente),
        "missao": 0,
        "pontos": 0,
        "resultados": {},
        "lancamentos": 0,
    }


if "partida" not in st.session_state:
    st.session_state.partida = criar_partida()

partida = st.session_state.partida


def reiniciar():
    st.session_state.clear()
    st.session_state.partida = criar_partida()
    st.rerun()


def salvar(missao: int, pontos: int, avaliacao: str, resolucao: str):
    """Uma missão pode ser pontuada apenas uma vez."""
    if missao not in partida["resultados"]:
        partida["resultados"][missao] = {
            "pontos": pontos,
            "avaliacao": avaliacao,
            "resolucao": resolucao,
        }
        partida["pontos"] += pontos
    st.rerun()


def resultado_e_avanco(missao: int):
    resultado = partida["resultados"].get(missao)
    if not resultado:
        return False
    st.markdown("---")
    if resultado["pontos"] > 0:
        st.success(f"{resultado['avaliacao']}  ·  +{resultado['pontos']} pontos")
    else:
        st.warning(resultado["avaliacao"])
    st.markdown("**Resolução comentada**")
    st.info(resultado["resolucao"])
    texto = "🏆 Ver resultado final" if missao == 4 else "Próxima missão →"
    if st.button(texto, type="primary", key=f"avanco_{missao}"):
        partida["missao"] += 1
        st.rerun()
    return True


def titulo_missao(numero: int, subtitulo: str):
    st.markdown(f'<div class="mission">MISSÃO {numero + 1} DE 5 · ATÉ 20 PONTOS</div>', unsafe_allow_html=True)
    st.header(TITULOS[numero])
    st.caption(subtitulo)


def grafico_barras(contagens: dict, campo: str, nome_indice: str):
    dados = pd.DataFrame(
        [{nome_indice: str(chave), campo: valor} for chave, valor in contagens.items()]
    ).set_index(nome_indice)
    st.bar_chart(dados, height=240)


def missao_1():
    titulo_missao(0, "Probabilidade clássica e frequência relativa em lançamentos de um dado.")
    evento = partida["desafios"]["evento_dado"]
    faces = set(evento["faces"])
    st.markdown(
        f'<div class="info-box">Você recebeu um dado equilibrado de seis faces. '
        f'<b>Qual é a probabilidade teórica de {evento["descricao"]}?</b> '
        f'Responda em porcentagem (por exemplo: 50 ou 50%).</div>',
        unsafe_allow_html=True,
    )
    st.write("**Experimente antes de responder:**")
    col1, col2, col3 = st.columns(3)
    for coluna, quantidade in zip((col1, col2, col3), (20, 100, 500)):
        if coluna.button(
            f"🎲 Lançar +{quantidade}",
            disabled=partida["lancamentos"] + quantidade > 1000,
            use_container_width=True,
        ):
            partida["lancamentos"] += quantidade
            st.rerun()
    n = partida["lancamentos"]
    if n:
        observacoes = simular_dados(partida["semente"] + 101, n)
        acertos = sum(face in faces for face in observacoes)
        c1, c2 = st.columns(2)
        c1.metric("Lançamentos realizados", n)
        c2.metric("Frequência relativa observada", f"{100 * acertos / n:.1f}%")
        grafico_barras({i: observacoes.count(i) for i in range(1, 7)}, "Lançamentos", "Face")
    else:
        st.caption("Use os botões para gerar dados reais de uma simulação.")
    if 0 not in partida["resultados"]:
        resposta = st.text_input("Sua previsão de probabilidade (%)", key="r1", placeholder="Ex.: 33,3")
        with st.expander("💡 Dica"):
            st.write("Em um dado equilibrado, todas as faces são equiprováveis. Conte os casos favoráveis e divida por 6.")
        if st.button("Conferir resposta", type="primary", key="enviar1"):
            try:
                valor = ler_numero(resposta)
                if not 0 <= valor <= 100:
                    raise ValueError("A probabilidade percentual deve estar entre 0 e 100.")
            except ValueError as erro:
                st.error(f"Informe uma porcentagem válida. {erro}")
            else:
                correto = 100 * len(faces) / 6
                diferenca = abs(valor - correto)
                pontos = 20 if diferenca <= 0.6 else 10 if diferenca <= 5 else 0
                mensagem = "Excelente previsão!" if pontos == 20 else "Você chegou perto!" if pontos else "A previsão não coincidiu com a probabilidade teórica."
                resolucao = (
                    f"P(evento) = casos favoráveis / casos possíveis = {len(faces)}/6 "
                    f"= {correto:.2f}%. A frequência observada pode diferir do valor teórico."
                )
                salvar(0, pontos, mensagem, resolucao)
    resultado_e_avanco(0)


def missao_2():
    titulo_missao(1, "Estatística descritiva para analisar um conjunto de medições.")
    valores = partida["desafios"]["dados_descritivos"]
    st.markdown(
        '<div class="info-box">Uma equipe registrou nove medições de tempo (minutos). '
        'Calcule a <b>média</b>, a <b>mediana</b> e a <b>moda</b>. '
        'Na média, use duas casas decimais.</div>',
        unsafe_allow_html=True,
    )
    st.code("  ·  ".join(map(str, valores)), language=None)
    frequencias = dict(sorted(Counter(valores).items()))
    grafico_barras(frequencias, "Frequência", "Tempo (min)")
    if 1 not in partida["resultados"]:
        with st.form("form_missao_2"):
            a, b, c = st.columns(3)
            media_digitada = a.text_input("Média", placeholder="Ex.: 7,33")
            mediana_digitada = b.text_input("Mediana", placeholder="Ex.: 7")
            moda_digitada = c.text_input("Moda", placeholder="Ex.: 6")
            enviar = st.form_submit_button("Conferir cálculos", type="primary")
        with st.expander("💡 Dica"):
            st.write("Média: soma dividida pelo total. Mediana: valor central da lista ordenada. Moda: valor mais frequente.")
        if enviar:
            try:
                respostas = [ler_numero(x) for x in (media_digitada, mediana_digitada, moda_digitada)]
            except ValueError as erro:
                st.error(f"Revise os três campos: {erro}")
            else:
                medidas = medidas_descritivas(valores)
                esperados = [medidas["media"], medidas["mediana"], medidas["moda"]]
                acertos = [abs(r - v) <= 0.015 for r, v in zip(respostas, esperados)]
                pontos = sum(p for ok, p in zip(acertos, (8, 6, 6)) if ok)
                acertados = ", ".join(nome for nome, ok in zip(("média", "mediana", "moda"), acertos) if ok)
                mensagem = "Acertou todas as medidas!" if all(acertos) else (
                    f"Acertou: {acertados}." if acertados else "Nenhuma medida correta nesta tentativa."
                )
                resolucao = (
                    f"Ordem crescente: {sorted(valores)}. Soma = {sum(valores)}. "
                    f"Média = {sum(valores)}/9 = {medidas['media']:.2f}; "
                    f"mediana = {medidas['mediana']}; moda = {medidas['moda']}."
                )
                salvar(1, pontos, mensagem, resolucao)
    resultado_e_avanco(1)


def missao_3():
    titulo_missao(2, "Observe como a frequência relativa evolui com o tamanho da amostra.")
    p = partida["desafios"]["p_moeda"]
    st.markdown(
        f'<div class="info-box">Uma moeda de laboratório tem probabilidade real de cara '
        f'igual a <b>{100 * p:.0f}%</b>. Simule lançamentos e observe a frequência de caras.</div>',
        unsafe_allow_html=True,
    )
    n = st.slider("Tamanho da amostra", min_value=20, max_value=1000, value=100, step=20)
    observacoes = simular_bernoulli(partida["semente"] + 303, p, n)
    soma = 0
    registros = []
    for indice, valor in enumerate(observacoes, start=1):
        soma += valor
        if indice == 1 or indice % 10 == 0 or indice == n:
            registros.append({"n": indice, "Frequência observada": soma / indice, "Probabilidade real": p})
    a, b, c = st.columns(3)
    a.metric("Amostra", n)
    b.metric("Frequência de caras", f"{100 * soma / n:.1f}%")
    c.metric("Erro absoluto", f"{100 * abs(soma / n - p):.1f} p.p.")
    st.line_chart(pd.DataFrame(registros).set_index("n"), height=270)
    st.caption("A convergência não precisa ocorrer de forma monotônica: em amostras pequenas, há oscilações.")
    if 2 not in partida["resultados"]:
        st.write("**Qual afirmação descreve corretamente a Lei dos Grandes Números?**")
        opcoes = (
            "A frequência relativa tende a se aproximar da probabilidade real quando n aumenta, apesar das oscilações.",
            "A frequência relativa se aproxima a cada lançamento, sem nunca se afastar.",
            "Com 20 lançamentos, a frequência relativa será necessariamente igual à probabilidade real.",
        )
        escolha = st.radio("Escolha uma alternativa", opcoes, index=None, key="r3")
        if st.button("Validar interpretação", type="primary", key="enviar3"):
            if escolha is None:
                st.warning("Selecione uma alternativa.")
            else:
                certo = escolha == opcoes[0]
                salvar(
                    2,
                    20 if certo else 0,
                    "Conceito compreendido!" if certo else "Atenção à diferença entre tendência e garantia em cada lançamento.",
                    "A Lei dos Grandes Números afirma convergência da frequência relativa para p "
                    "com aumento do tamanho amostral. Isso não implica redução do erro a cada observação.",
                )
    resultado_e_avanco(2)


def missao_4():
    titulo_missao(3, "Use o modelo binomial para planejar inspeções de produção.")
    d = partida["desafios"]["binomial"]
    n, p, k = d["n"], d["p"], d["k"]
    st.markdown(
        f'<div class="info-box">Uma inspeção verifica <b>{n} componentes independentes</b>. '
        f'Cada componente apresenta defeito com probabilidade <b>{100 * p:.0f}%</b>. '
        f'Qual a chance de encontrar <b>exatamente {k} defeituosos</b>? '
        f'Informe em porcentagem, com duas casas decimais.</div>',
        unsafe_allow_html=True,
    )
    st.write("**Simulação de 1.500 lotes para apoiar sua estimativa:**")
    simulacao = simular_binomial(partida["semente"] + 404, n, p, 1500)
    grafico_barras(simulacao, "Lotes", "Peças defeituosas")
    frequencia = 100 * simulacao[k] / 1500
    st.metric(f"Frequência simulada de {k} defeitos", f"{frequencia:.2f}%")
    if 3 not in partida["resultados"]:
        resposta = st.text_input("P(X = k), em %", placeholder="Ex.: 24,58", key="r4")
        with st.expander("💡 Dica"):
            st.latex(r"P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}")
            st.write("A simulação é uma estimativa; a fórmula fornece a probabilidade teórica.")
        if st.button("Validar cálculo binomial", type="primary", key="enviar4"):
            try:
                valor = ler_numero(resposta)
                if not 0 <= valor <= 100:
                    raise ValueError("O resultado percentual deve estar entre 0 e 100.")
            except ValueError as erro:
                st.error(f"Informe uma porcentagem válida. {erro}")
            else:
                correto = 100 * probabilidade_binomial(n, p, k)
                diferenca = abs(valor - correto)
                pontos = 20 if diferenca <= 0.25 else 10 if diferenca <= 2 else 0
                mensagem = "Aplicação correta da distribuição binomial!" if pontos == 20 else (
                    "A resposta ficou próxima do valor teórico." if pontos else "Revise a função de probabilidade binomial."
                )
                resolucao = (
                    f"P(X={k}) = C({n},{k}) × ({p:.2f})^{k} × "
                    f"({1-p:.2f})^{n-k} = {correto:.2f}%. "
                    "O gráfico ilustra a distribuição empírica em 1.500 lotes simulados."
                )
                salvar(3, pontos, mensagem, resolucao)
    resultado_e_avanco(3)


def missao_5():
    titulo_missao(4, "Interprete um resultado de teste por meio de probabilidade condicional.")
    d = partida["desafios"]["teste"]
    vp, fp, fn, vn = d["vp"], d["fp"], d["fn"], d["vn"]
    st.markdown(
        '<div class="info-box">Uma fábrica testou <b>1.000 peças</b>. '
        'A tabela apresenta a situação real e o resultado do teste. '
        'Se uma peça teve <b>teste positivo</b>, qual a probabilidade de ela '
        'ser <b>realmente defeituosa</b>?</div>',
        unsafe_allow_html=True,
    )
    tabela = pd.DataFrame(
        {
            "Teste positivo": [vp, fp, vp + fp],
            "Teste negativo": [fn, vn, fn + vn],
            "Total": [vp + fn, fp + vn, vp + fp + fn + vn],
        },
        index=["Peça defeituosa", "Peça normal", "Total"],
    )
    st.dataframe(tabela, use_container_width=True)
    st.caption("Atenção: P(defeito | positivo) não é, necessariamente, igual a P(positivo | defeito).")
    if 4 not in partida["resultados"]:
        resposta = st.text_input("P(defeito | positivo), em %", placeholder="Ex.: 66,67", key="r5")
        with st.expander("💡 Dica"):
            st.write("Restrinja o universo a todas as peças com teste positivo. Dessas, conte quantas são de fato defeituosas.")
        if st.button("Resolver enigma", type="primary", key="enviar5"):
            try:
                valor = ler_numero(resposta)
                if not 0 <= valor <= 100:
                    raise ValueError("O resultado percentual deve estar entre 0 e 100.")
            except ValueError as erro:
                st.error(f"Informe uma porcentagem válida. {erro}")
            else:
                correto = 100 * probabilidade_positivo_defeito(vp, fp)
                diferenca = abs(valor - correto)
                pontos = 20 if diferenca <= 0.25 else 10 if diferenca <= 2 else 0
                mensagem = "Você interpretou a condição corretamente!" if pontos == 20 else (
                    "Quase lá: você identificou uma probabilidade próxima." if pontos else "Confira qual grupo constitui o denominador."
                )
                resolucao = (
                    f"P(defeito | positivo) = VP / (VP + FP) = {vp}/({vp}+{fp}) "
                    f"= {correto:.2f}%. O denominador inclui somente os testes positivos."
                )
                salvar(4, pontos, mensagem, resolucao)
    resultado_e_avanco(4)


def gerar_relatorio_csv() -> bytes:
    arquivo = StringIO()
    escritor = csv.writer(arquivo, delimiter=";")
    escritor.writerow(["missao", "tema", "pontos", "maximo"])
    for i, nome in enumerate(TITULOS):
        escritor.writerow([i + 1, nome, partida["resultados"].get(i, {}).get("pontos", 0), 20])
    escritor.writerow(["", "TOTAL", partida["pontos"], 100])
    return arquivo.getvalue().encode("utf-8-sig")


def tela_final():
    pontos = partida["pontos"]
    st.balloons() if pontos == 100 and not st.session_state.get("celebrou") else None
    st.session_state.celebrou = True
    st.header("🏆 Missões concluídas!")
    st.metric("Pontuação final", f"{pontos}/100")
    if pontos >= 90:
        conceito = "🥇 Mestre da Estatística"
    elif pontos >= 70:
        conceito = "🥈 Explorador Avançado"
    elif pontos >= 50:
        conceito = "🥉 Aprendiz Investigador"
    else:
        conceito = "📚 Pesquisador em formação"
    st.subheader(conceito)
    st.write("Reveja a pontuação de cada missão e tente superar sua marca em uma nova partida.")
    tabela = pd.DataFrame(
        [{"Missão": i + 1, "Tema": tema, "Pontos": partida["resultados"][i]["pontos"]}
         for i, tema in enumerate(TITULOS)]
    )
    st.dataframe(tabela, use_container_width=True, hide_index=True)
    st.download_button(
        "📥 Baixar meu resultado (.csv)",
        data=gerar_relatorio_csv(),
        file_name="resultado_missao_estatistica.csv",
        mime="text/csv",
    )
    if st.button("🔄 Jogar novamente", type="primary"):
        reiniciar()


# Interface principal e placar.
st.markdown(
    '<div class="hero"><h1>🎲 Missão Estatística</h1>'
    '<p>Descubra padrões, simule experimentos e resolva desafios com dados. '
    'Cinco missões · 100 pontos possíveis · aprendizagem na prática.</p></div>',
    unsafe_allow_html=True,
)

with st.sidebar:
    st.header("📊 Seu painel")
    st.metric("Pontuação", f"{partida['pontos']} / 100")
    st.progress(len(partida["resultados"]) / 5)
    st.caption(f"{len(partida['resultados'])} de 5 missões respondidas")
    st.markdown("**Trilha de aprendizagem**")
    for i, nome in enumerate(TITULOS):
        simbolo = "✅" if i in partida["resultados"] else "▶️" if i == partida["missao"] else "🔒"
        st.write(f"{simbolo} {i + 1}. {nome}")
    st.divider()
    if st.button("🔄 Reiniciar partida", use_container_width=True):
        reiniciar()
    st.caption("Projeto didático em Python + Streamlit. Cada resposta pontua uma única vez.")

if partida["missao"] == 0:
    missao_1()
elif partida["missao"] == 1:
    missao_2()
elif partida["missao"] == 2:
    missao_3()
elif partida["missao"] == 3:
    missao_4()
elif partida["missao"] == 4:
    missao_5()
else:
    tela_final()
