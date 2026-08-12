# data/raw

Base original, versionada sem nenhuma alteração para garantir reprodutibilidade.

## Arquivos

| Arquivo | Registros | Colunas | Alta qualidade (nota ≥ 7) |
|---|---|---|---|
| `winequality-red.csv` | 1.599 | 11 variáveis + `quality` | 217 (**13,6%**) |
| `winequality-white.csv` | 4.898 | 11 variáveis + `quality` | 1.060 (**21,6%**) |
| `winequality.names` | — | — | documentação original dos autores |

> ⚠️ Os dois CSV usam **ponto-e-vírgula (`;`)** como separador. O `src/data_loader.py`
> já trata isso — não altere os arquivos.

## Origem

Baixados do **UCI Machine Learning Repository**, que é a fonte primária destes dados:
https://archive.ics.uci.edu/dataset/186/wine+quality

O *Wine Quality Dataset* citado no enunciado (Kaggle) é uma republicação desta mesma base.
A versão mais comum no Kaggle (`WineQT.csv`) contém 1.143 linhas — um recorte da base tinta —
mais uma coluna `Id` sem valor preditivo. Optamos pela base original por ser completa
(1.599 registros no tinto) e por dispensar autenticação para download, o que torna o
repositório reprodutível por qualquer pessoa.

**Referência acadêmica:** Cortez, P., Cerdeira, A., Almeida, F., Matos, T., & Reis, J. (2009).
*Modeling wine preferences by data mining from physicochemical properties.* Decision Support
Systems, 47(4), 547-553.

## Qual base usar

**Decisão da equipe na R1** — registre a escolha no `README.md` da raiz:

- **Só o tinto** (`winequality-red.csv`) — caminho mais direto, e é o recorte usado pela
  versão do Kaggle citada no enunciado. É o padrão do `data_loader.load_raw()`.
- **Só o branco** (`winequality-white.csv`) — base maior e classes um pouco menos
  desbalanceadas.
- **Os dois juntos** — use `data_loader.load_both()`, que concatena as bases e cria a coluna
  `type` (0 = tinto, 1 = branco). Conta como feature engineering e precisa ser justificado.

## Se o grupo preferir o arquivo exato do Kaggle

O download exige autenticação — cada integrante precisa gerar o próprio token:

1. Acesse https://www.kaggle.com/settings → seção **API** → *Create New Token*
2. Salve o `kaggle.json` baixado em `C:\Users\<seu-usuario>\.kaggle\kaggle.json`
3. Rode:

```bash
pip install kaggle
```

```bash
kaggle datasets download -d yasserh/wine-quality-dataset -p data/raw --unzip
```

Nesse caso, ajuste a chamada para `load_raw("WineQT.csv", sep=",")`.
