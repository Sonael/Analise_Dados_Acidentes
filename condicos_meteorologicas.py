import pandas as pd

# Substitua com o caminho do seu arquivo se necessário
file_path = "acidentes_recife_bicicleta_completo.csv"

# Carregar o arquivo
df = pd.read_csv(file_path)

# Contar as condições meteorológicas
cond_meteo_counts = df["condicao_metereologica"].value_counts(dropna=False)
cond_meteo_percent = (cond_meteo_counts / cond_meteo_counts.sum() * 100).round(2)

# Combinar em um DataFrame
cond_meteo_resultado = pd.DataFrame({
    "Quantidade": cond_meteo_counts,
    "Porcentagem (%)": cond_meteo_percent
})

# Exibir o resultado
print("Condições Meteorológicas dos Acidentes:\n")
print(cond_meteo_resultado)
