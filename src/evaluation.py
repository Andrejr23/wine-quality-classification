"""Metricas e graficos de avaliacao dos modelos."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    classification_report,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
    roc_curve,
)

FIGURES_DIR = Path(__file__).resolve().parents[1] / "results" / "figures"
METRICS_DIR = Path(__file__).resolve().parents[1] / "results" / "metrics"


def evaluate(model, X_test, y_test, name="modelo"):
    """Metricas de um modelo.

    ATENCAO: a base e desbalanceada. Acurácia alta sozinha nao significa nada -
    a decisao deve olhar Recall, F1 e ROC-AUC da classe de alta qualidade.
    """
    y_pred = model.predict(X_test)
    y_proba = (
        model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else None
    )
    return {
        "modelo": name,
        "accuracy": round(accuracy_score(y_test, y_pred), 4),
        "precision": round(precision_score(y_test, y_pred, zero_division=0), 4),
        "recall": round(recall_score(y_test, y_pred, zero_division=0), 4),
        "f1": round(f1_score(y_test, y_pred, zero_division=0), 4),
        "roc_auc": round(roc_auc_score(y_test, y_proba), 4) if y_proba is not None else None,
    }


def compare_models(fitted_models, X_test, y_test, save=True):
    """Tabela comparativa de todos os modelos - entregavel da etapa 5."""
    df = pd.DataFrame(
        [evaluate(m, X_test, y_test, name) for name, m in fitted_models.items()]
    ).sort_values("f1", ascending=False)
    if save:
        METRICS_DIR.mkdir(parents=True, exist_ok=True)
        df.to_csv(METRICS_DIR / "comparativo_modelos.csv", index=False)
    return df


def print_report(model, X_test, y_test, name="modelo"):
    print(f"--- {name} ---")
    print(
        classification_report(
            y_test,
            model.predict(X_test),
            target_names=["Baixa/Media", "Alta qualidade"],
            zero_division=0,
        )
    )


def plot_confusion(model, X_test, y_test, name="modelo", save=True):
    fig, ax = plt.subplots(figsize=(5, 4))
    ConfusionMatrixDisplay.from_estimator(
        model,
        X_test,
        y_test,
        display_labels=["Baixa/Media", "Alta"],
        cmap="Blues",
        ax=ax,
    )
    ax.set_title(f"Matriz de confusao - {name}")
    plt.tight_layout()
    if save:
        FIGURES_DIR.mkdir(parents=True, exist_ok=True)
        slug = name.lower().replace(" ", "_")
        fig.savefig(FIGURES_DIR / f"confusao_{slug}.png", dpi=150)
    return fig


def plot_roc(fitted_models, X_test, y_test, save=True):
    """Curvas ROC sobrepostas - conteudo cobrado na Fase 2."""
    fig, ax = plt.subplots(figsize=(6, 5))
    for name, model in fitted_models.items():
        if not hasattr(model, "predict_proba"):
            continue
        proba = model.predict_proba(X_test)[:, 1]
        fpr, tpr, _ = roc_curve(y_test, proba)
        ax.plot(fpr, tpr, label=f"{name} (AUC={roc_auc_score(y_test, proba):.3f})")
    ax.plot([0, 1], [0, 1], "k--", lw=1, label="Aleatorio")
    ax.set_xlabel("Falso positivo")
    ax.set_ylabel("Verdadeiro positivo")
    ax.set_title("Curva ROC - comparacao entre modelos")
    ax.legend(loc="lower right")
    plt.tight_layout()
    if save:
        FIGURES_DIR.mkdir(parents=True, exist_ok=True)
        fig.savefig(FIGURES_DIR / "curva_roc.png", dpi=150)
    return fig


def plot_feature_importance(importance_df, top=10, save=True, name="modelo"):
    fig, ax = plt.subplots(figsize=(7, 5))
    data = importance_df.head(top)
    sns.barplot(data=data, y="variavel", x="importancia", ax=ax, color="#7C3A4E")
    ax.set_title(f"Variaveis mais influentes - {name}")
    ax.set_xlabel("Importancia")
    ax.set_ylabel("")
    plt.tight_layout()
    if save:
        FIGURES_DIR.mkdir(parents=True, exist_ok=True)
        fig.savefig(FIGURES_DIR / "importancia_variaveis.png", dpi=150)
    return fig
