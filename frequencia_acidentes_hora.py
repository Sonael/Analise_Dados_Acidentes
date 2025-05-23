import pandas as pd

# Carregar o arquivo
file_path = "acidentes_recife_bicicleta_completo.csv"
df = pd.read_csv(file_path)

# Converter a coluna de horário para datetime e extrair a hora
df["hora"] = pd.to_datetime(df["horario"], format="%H:%M:%S", errors='coerce').dt.hour

# Contar a frequência de acidentes por hora
hora_counts = df["hora"].value_counts().sort_index()

# Exibir os valores
print("Frequência de Acidentes por Hora do Dia:\n")
print(hora_counts)
