# Wine Quality Classification — Tech Challenge Fase 2

**Pós-Tech FIAP — Data Analytics | Turma 14DTAT | Fase 2: Machine Learning Applied to Business**

Classificação binária da qualidade de vinhos a partir de características físico-químicas.

---

## 1. Contexto e problema de negócio

A avaliação da qualidade de um vinho é tradicionalmente feita por especialistas através de
análise sensorial (aroma, sabor, acidez, equilíbrio). Esse processo é **subjetivo**, **lento** e
**dependente da experiência do avaliador**.

Durante a produção, no entanto, já são coletados dados físico-químicos objetivos. A pergunta
que este projeto responde é:

> **É possível prever a qualidade final de um vinho a partir apenas dos seus indicadores
> físico-químicos de produção?**

Se sim, o produtor ganha um instrumento para ajustar o processo produtivo *antes* do
engarrafamento e padronizar a qualidade do lote.

## 2. Objetivo

Desenvolver e comparar modelos de **classificação binária** que prevejam:

| Classe | Regra | Rótulo |
|---|---|---|
| Alta qualidade | `quality >= 7` | `1` |
| Baixa/média qualidade | `quality < 7` | `0` |

## 3. Dataset

- **Fonte:** [Wine Quality Dataset — Kaggle](https://www.kaggle.com/datasets/yasserh/wine-quality-dataset)
- **Arquivo utilizado:** `data/raw/WineQT.csv` *(preencher se usarem outro)*
- **Registros:** _a preencher_
- **Variável alvo original:** `quality` (nota de 0 a 10 atribuída por especialistas)

### Variáveis

| Variável | Descrição |
|---|---|
| `fixed acidity` | Acidez fixa |
| `volatile acidity` | Acidez volátil |
| `citric acid` | Ácido cítrico |
| `residual sugar` | Açúcar residual |
| `chlorides` | Cloretos |
| `free sulfur dioxide` | Dióxido de enxofre livre |
| `total sulfur dioxide` | Dióxido de enxofre total |
| `density` | Densidade |
| `pH` | pH |
| `sulphates` | Sulfatos |
| `alcohol` | Teor alcoólico |
| `quality` | Nota de qualidade (**alvo**) |

> ⚠️ O dataset de vinhos existe em duas versões públicas (tinto ≈1.599 linhas, branco ≈4.898).
> **Documentar aqui qual foi usada** — e, se as duas forem combinadas, registrar a criação da
> feature `type`.

## 4. Estrutura do repositório

```
wine-quality-classification/
│
├── data/
│   ├── raw/                  # base original, sem alterações
│   └── processed/            # base após limpeza e feature engineering
├── notebooks/
│   ├── 01_eda.ipynb          # Etapas 1 e 2: compreensão do problema + EDA
│   ├── 02_preprocessing.ipynb# Etapa 3: pré-processamento e feature engineering
│   └── 03_modelagem.ipynb    # Etapas 4, 5 e 6: modelos, avaliação e interpretação
├── src/
│   ├── data_loader.py        # carga da base e criação do alvo binário
│   ├── preprocessing.py      # limpeza, split, escalonamento, features
│   ├── modeling.py           # treino dos modelos
│   └── evaluation.py         # métricas, matriz de confusão, curva ROC
├── results/
│   ├── figures/              # gráficos exportados
│   └── metrics/              # tabelas comparativas de métricas (CSV)
├── apresentacao/             # apresentação executiva (PPT/PDF) + link do vídeo
├── requirements.txt
├── SPRINT.md                 # plano de trabalho, papéis e prazos da equipe
└── README.md
```

## 5. Como executar

```bash
git clone <URL-DO-REPO>
cd wine-quality-classification
python -m venv .venv
.venv\Scripts\activate        # Windows  (Linux/Mac: source .venv/bin/activate)
pip install -r requirements.txt
jupyter notebook
```

Baixe o CSV do Kaggle e coloque em `data/raw/`. Execute os notebooks na ordem `01` → `02` → `03`.

## 6. Metodologia

1. **Compreensão do problema** — definição do alvo e binarização da variável `quality`.
2. **EDA** — distribuições, correlações justificadas, outliers e balanceamento de classes.
3. **Pré-processamento** — dados faltantes, padronização, feature engineering.
4. **Modelagem** — treino de no mínimo dois classificadores.
5. **Avaliação** — Precision, Recall, F1, ROC/AUC e matriz de confusão (a base é desbalanceada,
   portanto **acurácia não é a métrica de decisão**).
6. **Interpretação** — variáveis mais influentes e implicações para o processo produtivo.

## 7. Resultados

| Modelo | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---|---|---|---|---|
| _a preencher_ | | | | | |
| _a preencher_ | | | | | |

**Modelo escolhido:** _a preencher_
**Justificativa:** _a preencher_

## 8. Principais conclusões

_A preencher após a modelagem — variáveis mais influentes e o que o produtor deve fazer com isso._

## 9. Entregáveis

- 📓 Código: este repositório
- 📊 Apresentação executiva: [`apresentacao/`](apresentacao/)
- 🎥 Vídeo executivo (até 5 min): _link a preencher_

## 10. Equipe

| Integrante | Papel | GitHub |
|---|---|---|
| _nome_ | Tech Lead / Repositório | |
| _nome_ | EDA & Qualidade de Dados | |
| _nome_ | Pré-processamento & Features | |
| _nome_ | Modelagem & Avaliação | |
| _nome_ | Storytelling & Vídeo | |

Ver [`SPRINT.md`](SPRINT.md) para a divisão detalhada de tarefas e prazos.
