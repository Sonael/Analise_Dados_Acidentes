import pandas as pd
import os

# Lista com os caminhos dos arquivos
arquivos = [
    "acidentes2020_recife_bicicleta.csv",
    "acidentes2021_recife_bicicleta.csv",
    "acidentes2022_recife_bicicleta.csv",
    "acidentes2023_recife_bicicleta.csv",
    "acidentes2024_recife_bicicleta.csv",
    "acidentes2025_recife_bicicleta.csv",
]

# Lista para armazenar os DataFrames
dataframes = []

# Lê cada arquivo CSV e adiciona à lista
for arquivo in arquivos:
    if os.path.exists(arquivo):
        try:
            df = pd.read_csv(arquivo, sep=';')  # <- usa ; como separador
            dataframes.append(df)
        except Exception as e:
            print(f"Erro ao ler {arquivo}: {e}")
    else:
        print(f"Arquivo não encontrado: {arquivo}")


# Concatena todos os DataFrames
df_completo = pd.concat(dataframes, ignore_index=True)

# Salva o resultado em um novo CSV
saida = "acidentes_recife_bicicleta_completo.csv"
df_completo.to_csv(saida, index=False)

print(f"Arquivo combinado salvo em: {saida}")
