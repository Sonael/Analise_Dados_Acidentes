import pandas as pd

# Substitua este caminho pelo local onde você salvou o arquivo
file_path = "acidentes_recife_bicicleta_completo.csv"

# Carrega o DataFrame
df = pd.read_csv(file_path)

# Top 10 causas mais comuns de acidente
top_10_causas = df["causa_acidente"].value_counts().head(10)

# Exibir os resultados
print("Top 10 Causas Mais Comuns de Acidentes:\n")
print(top_10_causas)
