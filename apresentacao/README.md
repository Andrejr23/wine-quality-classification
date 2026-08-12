# Apresentação executiva e vídeo

## Arquivo pronto para editar

**[`Apresentacao_Executiva_Wine_Quality.pptx`](Apresentacao_Executiva_Wine_Quality.pptx)** —
12 slides já montados seguindo o roteiro abaixo, com os dois gráficos nativos do PowerPoint
(editáveis: clique com o botão direito → *Editar Dados*).

O que precisa ser preenchido antes da entrega:

| Slide | O que substituir |
|---|---|
| 1 | Nomes dos 5 integrantes |
| 4 | Número real de amostras da base escolhida |
| 5 | Percentuais reais do balanceamento (gráfico + o "1 em cada 7") |
| 6 | Correlações reais com a nota (gráfico) |
| 8 | Os 4 coeficientes de correlação |
| 10 | As três métricas do modelo escolhido |
| 11 | Ajustar as recomendações conforme as variáveis realmente influentes |

Todos os slides já têm **anotações do apresentador** com a orientação de fala e o tempo
correspondente no vídeo (aba *Anotações* no PowerPoint).

## O que vai aqui

1. **Apresentação executiva** em PPT ou PDF, com o *storytelling da análise exploratória*.
   O enunciado pede que fique dentro do repositório, para acesso e visualização fáceis.
2. **Link do vídeo executivo** (até 5 minutos) — cole também no `README.md` da raiz.

## Roteiro sugerido da apresentação

| # | Slide | Conteúdo |
|---|---|---|
| 1 | Capa | Título, integrantes, turma |
| 2 | O problema | Avaliação de vinho hoje é sensorial: subjetiva, lenta, depende do avaliador |
| 3 | A oportunidade | Os dados físico-químicos já são coletados na produção — dá para usá-los |
| 4 | Os dados | Origem, volume, variáveis (em linguagem simples) |
| 5 | Achado 1 | O desbalanceamento: poucos vinhos são realmente excelentes |
| 6 | Achado 2 | O que os vinhos bons têm em comum (ex.: teor alcoólico) |
| 7 | Achado 3 | O que derruba a qualidade (ex.: acidez volátil = defeito) |
| 8 | Correlações | O mapa de relações, explicado — não só o heatmap |
| 9 | Como testamos | Dois modelos comparados (sem entrar em matemática) |
| 10 | Resultado | Quanto o modelo acerta, e por que a métrica escolhida foi essa |
| 11 | O que fazer com isso | Recomendações práticas para o processo produtivo |
| 12 | Próximos passos | Limitações e evolução |

## Roteiro do vídeo (≤ 5 min)

| Tempo | Bloco | O que dizer |
|---|---|---|
| 0:00–0:30 | Abertura | Quem somos e qual problema resolvemos |
| 0:30–1:15 | Contexto | Por que avaliar vinho por análise sensorial é caro e inconsistente |
| 1:15–2:45 | Descobertas | Os 3 achados principais da análise, com um gráfico cada |
| 2:45–3:45 | Solução | O modelo, o que ele acerta e o que ele erra — **em português, não em jargão** |
| 3:45–4:40 | Recomendação | O que a vinícola deve mudar no processo |
| 4:40–5:00 | Fechamento | Uma frase de impacto |

> ⚠️ **Requisito do enunciado:** linguagem executiva. Imagine que está falando com diretores.
> Palavras proibidas: *feature*, *overfitting*, *hiperparâmetro*, *F1-score*, *ROC-AUC*,
> *matriz de confusão*, *acurácia*, *dataset*.
>
> Traduções que funcionam:
> - "F1-score alto" → "o modelo acerta bem sem gerar alarme falso"
> - "recall" → "quantos vinhos bons ele consegue encontrar"
> - "features" → "as medições feitas na produção"
> - "falso positivo" → "vinho comum que o modelo classificou como excelente"
