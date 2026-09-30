# Ficha de Avaliação de Processo (PDD) — Questão 5

**Cenário escolhido:** A

1. **Nome do processo e descrição resumida:**
   Importação e consolidação de notas fiscais de fornecedores.
   O processo consiste em receber arquivos CSV enviados periodicamente por
   fornecedores, ler cada nota, validar os dados e calcular o total faturado
   no período para alimentar o sistema financeiro.

2. **Volume / frequência estimados:**
   Aproximadamente 50 a 200 notas por dia, processadas em lotes diários ao
   final do expediente (uma execução por dia útil).

3. **As entradas são estruturadas?** Sim.
   Os arquivos CSV possuem colunas fixas e conhecidas (`nota`, `cliente`,
   `valor`), com separador padrão e codificação definida. O formato não varia
   entre fornecedores, pois é gerado por um sistema ERP padronizado.

4. **As regras são claras e determinísticas?** Sim.
   A regra de negócio é objetiva: somar a coluna `valor` de todas as linhas
   válidas. Os casos de erro (arquivo ausente, arquivo vazio) têm tratamento
   definido e não dependem de julgamento humano. Não há ambiguidade na
   tomada de decisão.

5. **Veredito — o processo é elegível a RPA?** Sim, o processo é elegível.
   Os três critérios fundamentais para RPA são atendidos:
   - **Dados estruturados:** entrada em CSV com esquema fixo.
   - **Regras claras e determinísticas:** lógica de soma e tratamento de erros
     sem necessidade de interpretação subjetiva.
   - **Alta repetibilidade:** execução diária com o mesmo fluxo, sem variação
     no procedimento.
   A automação eliminaria retrabalho manual, reduziria erros humanos de
   digitação e liberaria o colaborador para atividades de maior valor agregado.
