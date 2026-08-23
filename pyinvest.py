# Nome dos integrantes: Gabriel Jardim, Gabriel Alonso, Nicolas Gabriel

import math
import random
import datetime
import statistics
import locale

locale.setlocale(locale.LC_ALL, '')

# Função que formata um número para moeda brasileira (R$)
def moeda(valor):
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return "R$ " + texto

# Função que converte uma taxa anual (%) para taxa mensal equivalente
def taxa_mensal(taxa_anual):
    return math.pow(1 + taxa_anual / 100, 1 / 12) - 1

# Função que calcula o montante final de um investimento com juros compostos
# Considera capital inicial + aportes mensais + taxa + tempo
def montante(capital, aporte, taxa, meses):
    parte1 = capital * math.pow(1 + taxa, meses)
    parte2 = aporte * ((math.pow(1 + taxa, meses) - 1) / taxa)
    return parte1 + parte2

# Função que define a alíquota de imposto de renda para CDB
# baseada no tempo do investimento (em meses)
def ir_cdb(meses):
    dias = meses * 30

    if dias <= 180:
        return 0.225
    elif dias <= 360:
        return 0.20
    elif dias <= 720:
        return 0.175
    else:
        return 0.15

# Função que cria uma barra gráfica proporcional (máx 50 blocos)
# usada para representar visualmente os valores
def barra(valor, maior):
    qtd = round((valor / maior) * 50)

    if qtd < 1:
        qtd = 1

    return "█" * qtd

# Função que compara os investimentos e retorna o melhor (nome e valor)
def melhor_opcao(cdb, lci, poupanca, fii):
    melhor_nome = "CDB"
    melhor_valor = cdb

    if lci > melhor_valor:
        melhor_nome = "LCI/LCA"
        melhor_valor = lci

    if poupanca > melhor_valor:
        melhor_nome = "Poupança"
        melhor_valor = poupanca

    if fii > melhor_valor:
        melhor_nome = "FII (Média)"
        melhor_valor = fii

    return melhor_nome, melhor_valor

# Função principal de cálculo e geração do relatório completo
# Aqui acontece tudo: cálculos, simulações, estatísticas e impressão
def gerar_relatorio(capital, aporte, prazo, cdi, perc_cdb, perc_lci, fii_percentual, meta):
    total = capital + aporte * prazo

    taxa_cdb = taxa_mensal(cdi) * (perc_cdb / 100)
    bruto_cdb = montante(capital, aporte, taxa_cdb, prazo)
    lucro_cdb = bruto_cdb - total
    cdb = bruto_cdb - (lucro_cdb * ir_cdb(prazo))

    taxa_lci = taxa_mensal(cdi) * (perc_lci / 100)
    lci = montante(capital, aporte, taxa_lci, prazo)

    poupanca = montante(capital, aporte, 0.005, prazo)

    taxa_fii = fii_percentual / 100
    base_fii = montante(capital, aporte, taxa_fii, prazo)

    # Simulação de variação dos FIIs (5 cenários)
    v1 = base_fii * (1 + random.uniform(-0.03, 0.03))
    v2 = base_fii * (1 + random.uniform(-0.03, 0.03))
    v3 = base_fii * (1 + random.uniform(-0.03, 0.03))
    v4 = base_fii * (1 + random.uniform(-0.03, 0.03))
    v5 = base_fii * (1 + random.uniform(-0.03, 0.03))

    fii_media = statistics.mean((v1, v2, v3, v4, v5))
    fii_mediana = statistics.median((v1, v2, v3, v4, v5))
    fii_desvio = statistics.stdev((v1, v2, v3, v4, v5))

    hoje = datetime.date.today()
    resgate = hoje + datetime.timedelta(days=prazo * 30)

    maior = max(cdb, lci, poupanca, fii_media)

    nome_melhor, valor_melhor = melhor_opcao(cdb, lci, poupanca, fii_media)

    if valor_melhor >= meta:
        meta_atingida = "Sim"
    else:
        meta_atingida = "Não"

    print("==================== PYINVEST ====================")
    print("Capital Inicial (R$):", capital)
    print("Aporte Mensal (R$):", aporte)
    print("Prazo (meses):", prazo)
    print("CDI Anual (%):", cdi)
    print("Percentual CDI no CDB (%):", perc_cdb)
    print("Percentual CDI na LCI (%):", perc_lci)
    print("Rentabilidade FII (%):", fii_percentual)
    print("Meta Financeira (R$):", meta)

    print()
    print("==================================================")
    print("RELATÓRIO PYINVEST -", hoje.strftime("%d/%m/%Y"))
    print("Data estimada de resgate:", resgate.strftime("%d/%m/%Y"))
    print("Total investido:", moeda(total))
    print("--------------------------------------------------")

    print("CDB         :", moeda(cdb))
    print("Gráfico     :", barra(cdb, maior))

    print("LCI/LCA     :", moeda(lci))
    print("Gráfico     :", barra(lci, maior))

    print("Poupança    :", moeda(poupanca))
    print("Gráfico     :", barra(poupanca, maior))

    print("FII (Média) :", moeda(fii_media))
    print("Gráfico     :", barra(fii_media, maior))

    print("--------------------------------------------------")
    print("Estatísticas FII (Mediana):", moeda(fii_mediana))
    print("Desvio Padrão FII:", moeda(fii_desvio))
    print("Meta atingida?", meta_atingida)
    print()
    print("Melhor opção:", nome_melhor, "com", moeda(valor_melhor))

# Função principal do programa (entrada de dados do usuário)
def main():

    capital = float(input("Capital Inicial (R$): "))
    aporte = float(input("Aporte Mensal (R$): "))
    prazo = int(input("Prazo (meses): "))
    cdi = float(input("CDI Anual (%): "))
    perc_cdb = float(input("Percentual CDI no CDB (%): "))
    perc_lci = float(input("Percentual CDI na LCI (%): "))
    fii_percentual = float(input("Rentabilidade FII (%): "))
    meta = float(input("Meta Financeira (R$): "))

    print()
    gerar_relatorio(capital, aporte, prazo, cdi, perc_cdb, perc_lci, fii_percentual, meta)

# Executa o programa
if __name__ == "__main__":
    main()
