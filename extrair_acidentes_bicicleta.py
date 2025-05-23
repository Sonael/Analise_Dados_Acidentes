import pandas as pd
import unicodedata

def clean_column_name(col: str) -> str:
    """
    Remove acentos, espaços e normaliza pra minúsculas.
    Ex.: ' Município ' → 'municipio'
    """
    nfkd = unicodedata.normalize('NFKD', col)
    no_accents = "".join(c for c in nfkd if not unicodedata.combining(c))
    return no_accents.strip().lower()

def ler_com_fallback(arquivo, encodings=('utf-8', 'cp1252', 'latin1')):
    """Tenta ler CSV com diferentes encodings usando sep=';'. Retorna DataFrame."""
    last_err = None
    for enc in encodings:
        try:
            return pd.read_csv(arquivo, sep=';', encoding=enc, dtype=str)
        except UnicodeDecodeError as e:
            print(f"Falha ao ler com encoding '{enc}': {e}")
            last_err = e
    raise last_err

def filtrar_recife_bicicleta(arquivo_entrada: str,
                             arquivo_saida: str) -> None:
    # 1. Leitura
    df = ler_com_fallback(arquivo_entrada)

    # 2. Limpa nomes de coluna
    df.rename(columns={c: clean_column_name(c) for c in df.columns}, inplace=True)

    # 3. Verifica colunas
    for col in ('municipio', 'tipo_veiculo'):
        if col not in df.columns:
            raise KeyError(f"Coluna esperada não encontrada: {col}")

    # 4. Filtra Recife + Bicicleta
    filtro = (
        df['municipio'].str.strip().str.lower() == 'recife'
    ) & (
        df['tipo_veiculo'].str.strip().str.lower() == 'bicicleta'
    )
    df_filtrado = df.loc[filtro]

    # 5. Salva ou avisa
    if df_filtrado.empty:
        print("Nenhum registro de bicicleta em Recife encontrado.")
    else:
        df_filtrado.to_csv(arquivo_saida, sep=';', index=False)
        print(f"{len(df_filtrado)} registro(s) salvo(s) em '{arquivo_saida}'.")

if __name__ == "__main__":
    entrada = "acidentes2020_todas_causas_tipos.csv"
    saida   = "acidentes2020_recife_bicicleta.csv"
    filtrar_recife_bicicleta(entrada, saida)
