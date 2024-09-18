import math
import pandas as pd
import os


def ler_arquivo_xlsx():
    # Ler o arquivo Excel
    # Lendo sem cabeçalhos para pegar todas as linhas

    caminho = os.path.abspath('controle_epis.xlsx')

    df = pd.read_excel(caminho, header=None)

    # Converter o DataFrame em uma lista de listas, ignorando linhas onde a primeira célula é NaN
    lista_linhas = [linha for linha in df.values.tolist() if not (
        isinstance(linha[0], float) and math.isnan(linha[0]))]

    dados = lista_linhas[1:6000]

    # Imprimir as listas
    for i, linha in enumerate(dados):
        print(f"Linha {i+1}: {linha}")

    return dados


if __name__ == '__main__':
    ler_arquivo_xlsx()
