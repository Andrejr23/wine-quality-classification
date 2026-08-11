# Plano de Sprints — Tech Challenge Fase 2

**Entrega final: terça-feira, 01/09/2026** · Hoje: 11/08/2026 · **21 dias corridos** · Equipe de 5

---

## 1. Papéis fixos da equipe

Cada pessoa é **dona** de uma etapa do enunciado, mas todos revisam o trabalho de todos.
Preencham os nomes na primeira reunião.

| # | Papel | Dono | Responsabilidade principal | Entregável |
|---|---|---|---|---|
| 1 | **Tech Lead / Repositório** | _nome_ | Cria o repo no GitHub, gerencia branches e merges, mantém `README.md` e `requirements.txt`, garante que tudo roda do zero | Repositório organizado e reprodutível |
| 2 | **EDA & Qualidade de Dados** | _nome_ | Etapas 1 e 2: binarização do alvo, distribuições, correlações **justificadas**, outliers, balanceamento | `01_eda.ipynb` + gráficos em `results/figures/` |
| 3 | **Pré-processamento & Features** | _nome_ | Etapa 3: faltantes, duplicados, padronização, feature engineering, split estratificado | `02_preprocessing.ipynb` + bases em `data/processed/` |
| 4 | **Modelagem & Avaliação** | _nome_ | Etapas 4 e 5: treinar ≥2 modelos, validação cruzada, métricas, ROC, matriz de confusão | `03_modelagem.ipynb` + `results/metrics/` |
| 5 | **Storytelling & Vídeo** | _nome_ | Etapa 6 (leitura de negócio), apresentação executiva e vídeo de até 5 min | `apresentacao/` + link do vídeo |

> 💡 **Sugestão de alocação:** quem tem perfil de negócio/RH/comunicação encaixa melhor no papel 5 —
> é o papel que traduz o modelo para a diretoria, e é onde o enunciado mais cobra (o vídeo tem
> exigência explícita de linguagem executiva, sem termos técnicos).

**Regra de ouro:** ninguém fica ocioso esperando a etapa anterior. Veja as tarefas paralelas de
cada sprint.

---

## 2. Calendário de reuniões (1 por semana, às terças)

| # | Data | Duração | Pauta |
|---|---|---|---|
| **R1 — Kickoff** | Ter **11/08** | 1h | Definir papéis, escolher o dataset (tinto/branco/ambos), criar repo, todos clonam e rodam o ambiente |
| **R2 — Fecha EDA** | Ter **18/08** | 1h | Apresentar achados da EDA, aprovar decisões de outliers e features, travar a narrativa da apresentação |
| **R3 — Fecha modelos** | Ter **25/08** | 1h | Comparar modelos, **escolher o modelo final**, definir as 3 mensagens-chave do vídeo |
| **R4 — Ensaio & envio** | Seg **31/08** | 1h30 | Revisar repo completo, ensaiar e gravar o vídeo, checklist final |
| 📤 **ENTREGA** | **Ter 01/09** | — | Submeter no portal FIAP |

---

## 3. Sprint 1 — Dados e EDA
**12/08 (qua) → 18/08 (ter)** · Fecha na R2

| Dono | Tarefa | Prazo |
|---|---|---|
| 1 · Tech Lead | Criar repo no GitHub, subir este esqueleto, adicionar os 4 colegas como colaboradores | **12/08** |
| 1 · Tech Lead | Todos com ambiente rodando (`pip install -r requirements.txt` + notebook abrindo) | **13/08** |
| 2 · EDA | Baixar o CSV do Kaggle, colocar em `data/raw/`, documentar a versão no README | **13/08** |
| 2 · EDA | Rodar `01_eda.ipynb`: distribuições, balanceamento, faltantes, duplicados | **15/08** |
| 2 · EDA | Matriz de correlação + **justificativa escrita de cada correlação relevante** | **17/08** |
| 2 · EDA | Relatório de outliers + decisão (manter/remover) com justificativa | **17/08** |
| 3 · Pré-proc | Estudar `src/preprocessing.py` e propor as features derivadas que fazem sentido | **17/08** |
| 4 · Modelagem | Preparar o ambiente de modelagem, revisar métricas para base desbalanceada | **17/08** |
| 5 · Storytelling | Montar o esqueleto da apresentação (roteiro de slides, ainda sem números) | **17/08** |
| **Todos** | Ler a seção de síntese do `01_eda.ipynb` antes da R2 | **18/08** |

**✅ Critério de conclusão:** o `01_eda.ipynb` roda de ponta a ponta, todos os gráficos estão em
`results/figures/`, e existe um parágrafo escrito para cada correlação relevante.

---

## 4. Sprint 2 — Pré-processamento e Modelagem
**19/08 (qua) → 25/08 (ter)** · Fecha na R3

| Dono | Tarefa | Prazo |
|---|---|---|
| 3 · Pré-proc | Tratar faltantes/duplicados conforme decidido na R2 | **20/08** |
| 3 · Pré-proc | Implementar e validar as features derivadas (justificar cada uma) | **21/08** |
| 3 · Pré-proc | Split estratificado + padronização; exportar bases para `data/processed/` | **21/08** |
| 4 · Modelagem | Treinar os 2 modelos obrigatórios (Logística + Random Forest) | **22/08** |
| 4 · Modelagem | Ampliar para Gradient Boosting / KNN / SVM + validação cruzada | **23/08** |
| 4 · Modelagem | Tabela comparativa, curvas ROC, matrizes de confusão em `results/` | **24/08** |
| 2 · EDA | Revisar o notebook 02 do colega (code review) | **22/08** |
| 5 · Storytelling | Preencher a apresentação com os gráficos e números reais da EDA | **24/08** |
| 1 · Tech Lead | Revisar e mergear os PRs, garantir que o repo roda limpo do zero | **24/08** |
| **Todos** | Olhar a tabela comparativa antes da R3 para decidir o modelo juntos | **25/08** |

**✅ Critério de conclusão:** tabela comparativa de modelos pronta em
`results/metrics/comparativo_modelos.csv`, com um modelo eleito e justificado **por F1/ROC-AUC —
não por acurácia**.

---

## 5. Sprint 3 — Interpretação, Apresentação e Vídeo
**26/08 (qua) → 31/08 (seg)** · Fecha na R4

| Dono | Tarefa | Prazo |
|---|---|---|
| 4 · Modelagem | Importância das variáveis + coeficientes com direção do efeito | **26/08** |
| 4 + 5 | Traduzir as variáveis influentes em **recomendações para a produção** (Etapa 6) | **27/08** |
| 5 · Storytelling | Fechar a apresentação executiva (PDF/PPT) e subir em `apresentacao/` | **28/08** |
| 5 · Storytelling | Escrever o roteiro do vídeo (≤5 min, linguagem executiva, zero jargão) | **28/08** |
| 1 · Tech Lead | Finalizar `README.md`: resultados, conclusões, equipe, instruções de execução | **29/08** |
| 2 · EDA | Revisão geral: todos os gráficos citados existem e estão legíveis | **29/08** |
| 3 · Pré-proc | Testar o repo do zero em outra máquina (clone → install → rodar tudo) | **29/08** |
| **Todos** | R4: ensaiar e **gravar o vídeo** | **31/08** |
| 1 · Tech Lead | Subir o link do vídeo no README e fazer o commit final | **31/08** |
| **Todos** | 📤 Submeter no portal FIAP | **01/09** |

**✅ Critério de conclusão:** os 3 entregáveis prontos — repositório, apresentação e vídeo.

---

## 6. Como trabalhar no Git (para quem está começando)

Fluxo simples, uma branch por pessoa/etapa:

```bash
git clone <URL-DO-REPO>
cd wine-quality-classification
git checkout -b eda-nome-da-pessoa
# ... trabalha ...
git add .
git commit -m "Adiciona análise de correlações com justificativas"
git push -u origin eda-nome-da-pessoa
```

Depois é só abrir o **Pull Request** no GitHub e pedir a revisão do Tech Lead.

⚠️ **Nunca commitem direto na `main`.** E antes de começar o dia:

```bash
git checkout main
git pull
git checkout -b nova-branch
```

---

## 7. Riscos e como evitá-los

| Risco | Impacto | Prevenção |
|---|---|---|
| Usar **acurácia** como métrica principal | Alto — modelo inútil parecendo bom | Decidir por F1/Recall/ROC-AUC; já está no `03_modelagem.ipynb` |
| Deixar `quality` original entre as features | Alto — vazamento, 100% de acerto falso | `get_features_and_target()` já remove |
| Correlações sem justificativa | Médio — exigência literal do enunciado | Tabela de justificativas no `01_eda.ipynb` |
| Vídeo com jargão técnico | Médio — requisito explícito | Roteiro revisado por quem **não** está na modelagem |
| Tudo travar esperando uma etapa | Alto | Tarefas paralelas já distribuídas em cada sprint |
| Deixar o vídeo para o último dia | Alto | R4 em 31/08 é para **gravar**, não para começar |

---

## 8. Checklist final (rodar na R4)

- [ ] Repositório público (ou com acesso ao professor) e link funcionando
- [ ] `README.md` completo: contexto, dataset, execução, resultados, conclusões, equipe
- [ ] `requirements.txt` instala sem erro num ambiente limpo
- [ ] Notebooks rodam na ordem 01 → 02 → 03 sem erro
- [ ] **Etapa 1** — problema interpretado, alvo definido, binarização feita
- [ ] **Etapa 2** — distribuições, correlações **justificadas**, outliers, balanceamento
- [ ] **Etapa 3** — faltantes, padronização, feature engineering
- [ ] **Etapa 4** — no mínimo 2 modelos treinados e comparados
- [ ] **Etapa 5** — métricas adequadas + comparação entre modelos
- [ ] **Etapa 6** — variáveis influentes + implicações para a produção
- [ ] Apresentação executiva (PDF/PPT) dentro de `apresentacao/`
- [ ] Vídeo de **até 5 minutos**, com pelo menos 1 integrante apresentando
- [ ] Vídeo em **linguagem executiva** — nenhum termo técnico
- [ ] Link do vídeo no `README.md`
- [ ] Professores da Fase 2 consultados pelo menos uma vez (o enunciado convida explicitamente)
