"""Limpeza, feature engineering e preparacao dos dados para modelagem."""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

RANDOM_STATE = 42


def missing_report(df):
    """Quantidade e percentual de valores faltantes por coluna."""
    total = df.isna().sum()
    return pd.DataFrame(
        {"faltantes": total, "percentual": (total / len(df) * 100).round(2)}
    ).sort_values("faltantes", ascending=False)


def duplicates_report(df):
    """Numero de linhas duplicadas."""
    return int(df.duplicated().sum())


def outlier_bounds(series, k=1.5):
    """Limites inferior e superior pelo criterio IQR."""
    q1, q3 = series.quantile(0.25), series.quantile(0.75)
    iqr = q3 - q1
    return q1 - k * iqr, q3 + k * iqr


def outlier_report(df, columns=None, k=1.5):
    """Contagem de outliers por variavel numerica segundo o criterio IQR."""
    columns = columns or df.select_dtypes(include=np.number).columns
    rows = []
    for col in columns:
        low, high = outlier_bounds(df[col], k)
        n = int(((df[col] < low) | (df[col] > high)).sum())
        rows.append(
            {
                "variavel": col,
                "limite_inferior": round(low, 4),
                "limite_superior": round(high, 4),
                "outliers": n,
                "percentual": round(n / len(df) * 100, 2),
            }
        )
    return pd.DataFrame(rows).sort_values("outliers", ascending=False)


def add_engineered_features(X):
    """Features derivadas com leitura enologica.

    Cada uma precisa ser justificada na apresentacao - nao adicionar feature sem
    explicacao de negocio.
    """
    X = X.copy()
    # Proporcao de SO2 livre: o SO2 livre e o que de fato protege o vinho da oxidacao.
    X["free_to_total_so2"] = X["free sulfur dioxide"] / X["total sulfur dioxide"]
    # Balanco acidez fixa x volatil: a volatil em excesso e o defeito ("cheiro de vinagre").
    X["acidity_ratio"] = X["fixed acidity"] / X["volatile acidity"]
    # Densidade tende a cair com mais alcool e subir com mais acucar residual.
    X["alcohol_density"] = X["alcohol"] / X["density"]
    return X.replace([np.inf, -np.inf], np.nan).fillna(X.median(numeric_only=True))


def split_data(X, y, test_size=0.2, random_state=RANDOM_STATE):
    """Split estratificado - obrigatorio aqui, porque as classes sao desbalanceadas."""
    return train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )


def scale_data(X_train, X_test):
    """Padroniza as variaveis. O scaler e ajustado SO no treino, para evitar vazamento."""
    scaler = StandardScaler()
    X_train_scaled = pd.DataFrame(
        scaler.fit_transform(X_train), columns=X_train.columns, index=X_train.index
    )
    X_test_scaled = pd.DataFrame(
        scaler.transform(X_test), columns=X_test.columns, index=X_test.index
    )
    return X_train_scaled, X_test_scaled, scaler
