"""Carga da base de vinhos e criação da variável alvo binária."""

from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"
PROCESSED_DIR = Path(__file__).resolve().parents[1] / "data" / "processed"

# Limiar definido no enunciado do Tech Challenge: nota >= 7 e vinho de alta qualidade.
QUALITY_THRESHOLD = 7
TARGET = "high_quality"


# Os arquivos originais do UCI usam ponto-e-virgula como separador.
DEFAULT_FILE = "winequality-red.csv"


def load_raw(filename=DEFAULT_FILE, sep=";"):
    """Le o CSV original em data/raw e devolve o DataFrame sem alteracoes."""
    path = RAW_DIR / filename
    if not path.exists():
        raise FileNotFoundError(
            f"Arquivo nao encontrado: {path}\n"
            "Veja data/raw/README.md para as bases disponiveis."
        )
    df = pd.read_csv(path, sep=sep)
    # A republicacao do Kaggle (WineQT.csv) traz uma coluna 'Id' que nao e preditiva.
    return df.drop(columns=["Id"], errors="ignore")


def load_both(sep=";"):
    """Carrega tinto e branco em uma base unica, com a coluna 'type' identificando a origem.

    Usar apenas se o grupo decidir analisar os dois juntos - nesse caso 'type' vira
    uma feature legitima e precisa ser justificada na apresentacao.
    """
    red = load_raw("winequality-red.csv", sep)
    white = load_raw("winequality-white.csv", sep)
    red["type"] = 0   # tinto
    white["type"] = 1  # branco
    return pd.concat([red, white], ignore_index=True)


def add_binary_target(df, threshold=QUALITY_THRESHOLD):
    """Cria a coluna alvo binaria a partir da nota original de qualidade."""
    df = df.copy()
    df[TARGET] = (df["quality"] >= threshold).astype(int)
    return df


def get_features_and_target(df, drop_original_quality=True):
    """Separa X e y. A nota original e removida para evitar vazamento de dados."""
    cols_to_drop = [TARGET]
    if drop_original_quality:
        cols_to_drop.append("quality")
    X = df.drop(columns=cols_to_drop, errors="ignore")
    y = df[TARGET]
    return X, y


def class_balance(y):
    """Distribuicao absoluta e percentual das classes."""
    counts = y.value_counts().sort_index()
    return pd.DataFrame(
        {"quantidade": counts, "percentual": (counts / len(y) * 100).round(2)}
    )
