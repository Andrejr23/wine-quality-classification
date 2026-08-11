"""Definicao e treino dos modelos de classificacao."""

import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, StratifiedKFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

RANDOM_STATE = 42


def get_models():
    """Modelos candidatos.

    O enunciado exige no minimo dois. A dupla recomendada e Regressao Logistica
    (baseline interpretavel) + Random Forest (nao-linear e ja entrega importancia
    de variaveis para a etapa de interpretacao). Os demais ficam disponiveis para
    ampliar a comparacao.

    class_weight='balanced' compensa o desbalanceamento das classes.
    """
    return {
        "Regressao Logistica": LogisticRegression(
            max_iter=1000, class_weight="balanced", random_state=RANDOM_STATE
        ),
        "Random Forest": RandomForestClassifier(
            n_estimators=300, class_weight="balanced", random_state=RANDOM_STATE
        ),
        "Gradient Boosting": GradientBoostingClassifier(random_state=RANDOM_STATE),
        "KNN": KNeighborsClassifier(n_neighbors=5),
        "SVM": SVC(
            probability=True, class_weight="balanced", random_state=RANDOM_STATE
        ),
    }


def train_models(models, X_train, y_train):
    """Treina cada modelo e devolve o dicionario com os modelos ajustados."""
    return {name: model.fit(X_train, y_train) for name, model in models.items()}


def cross_validate_models(models, X, y, scoring="f1", cv=5):
    """Validacao cruzada estratificada - conteudo cobrado na Fase 2."""
    skf = StratifiedKFold(n_splits=cv, shuffle=True, random_state=RANDOM_STATE)
    rows = []
    for name, model in models.items():
        scores = cross_val_score(model, X, y, scoring=scoring, cv=skf)
        rows.append(
            {
                "modelo": name,
                f"{scoring}_medio": round(scores.mean(), 4),
                "desvio_padrao": round(scores.std(), 4),
            }
        )
    return pd.DataFrame(rows).sort_values(f"{scoring}_medio", ascending=False)


def tune_random_forest(X_train, y_train, scoring="f1", cv=5):
    """Busca de hiperparametros para a Random Forest."""
    grid = {
        "n_estimators": [200, 300, 500],
        "max_depth": [None, 8, 12],
        "min_samples_leaf": [1, 2, 4],
    }
    search = GridSearchCV(
        RandomForestClassifier(class_weight="balanced", random_state=RANDOM_STATE),
        grid,
        scoring=scoring,
        cv=StratifiedKFold(n_splits=cv, shuffle=True, random_state=RANDOM_STATE),
        n_jobs=-1,
    )
    search.fit(X_train, y_train)
    return search.best_estimator_, search.best_params_, round(search.best_score_, 4)


def feature_importance(model, feature_names):
    """Importancia das variaveis - alimenta a etapa 6 (interpretacao)."""
    if hasattr(model, "feature_importances_"):
        values = model.feature_importances_
    elif hasattr(model, "coef_"):
        values = abs(model.coef_[0])
    else:
        raise ValueError("Modelo sem importancia de variaveis disponivel.")
    return (
        pd.DataFrame({"variavel": feature_names, "importancia": values})
        .sort_values("importancia", ascending=False)
        .reset_index(drop=True)
    )
