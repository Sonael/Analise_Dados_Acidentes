"""
Script Python para extrair dados do CSV de acidentes e gerar um arquivo JSON.
"""
import pandas as pd
import json

# Caminho do arquivo CSV (ajuste se necessário)
csv_path = 'acidentes_recife_bicicleta_completo.csv'
# Nome do arquivo JSON de saída
json_path = 'acidentes_recife_bicicleta.json'

# Colunas que serão mantidas no JSON
data_columns = [
    'data_inversa',
    'horario',
    'sexo',
    'mortos',
    'ilesos',
    'feridos_leves',
    'feridos_graves',
    'causa_acidente',
    'tipo_acidente',
    'condicao_metereologica'
]

# Leitura do CSV
print(f"Carregando dados de: {csv_path}")
df = pd.read_csv(csv_path, parse_dates=['data_inversa'], dayfirst=True, dtype=str)

# Filtrar apenas colunas relevantes e remover linhas sem data ou hora
print("Filtrando colunas e removendo registros inválidos...")
df = df[data_columns].dropna(subset=['data_inversa', 'horario'])

# Conversão de tipos numéricos (opcional)
df['mortos'] = pd.to_numeric(df['mortos'], errors='coerce').fillna(0).astype(int)
df['ilesos'] = pd.to_numeric(df['ilesos'], errors='coerce').fillna(0).astype(int)
df['feridos_leves'] = pd.to_numeric(df['feridos_leves'], errors='coerce').fillna(0).astype(int)
df['feridos_graves'] = pd.to_numeric(df['feridos_graves'], errors='coerce').fillna(0).astype(int)

# Geração da lista de registros (dicionários)
print("Convertendo para lista de dicionários...")
records = df.to_dict(orient='records')

# Escrita do JSON no disco
print(f"Salvando JSON em: {json_path}")
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(records, f, ensure_ascii=False)

print("Concluído com sucesso!")
