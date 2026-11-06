# Capability: metricas-esg

## Purpose
Consolidar e expor métricas agregadas de descarbonização e sustentabilidade associadas às viagens da organização parceira, permitindo a extração de relatórios auditáveis.

## ADDED Requirements

### Requirement: UC-08.S1 Visualização e Exportação de Métricas ESG
O sistema Uni-Bike SHALL calcular e disponibilizar aos gestores da organização cliente indicadores consolidados de mobilidade suave (distância total e estimativa de $CO_2$ evitado conforme a fórmula da BR-03), assegurando que a compilação e exportação de relatórios em formato PDF ou CSV ocorre em tempo inferior a 5 segundos para intervalos de até 1 ano (RNF-04).

#### Scenario: CT-08.1 Exportação de relatório anual de sustentabilidade
- **WHEN** o gestor da organização cliente autenticado acede ao Dashboard ESG, seleciona o filtro anual e clica em "Exportar Relatório PDF"
- **THEN** o sistema gera e transfere o ficheiro executivo em menos de 5 segundos (RNF-04), com dados consolidados e estritamente anónimos de quilómetros e $CO_2$ poupado (BR-03)

#### Scenario: CT-08.2 Consulta de intervalo sem histórico de viagens
- **WHEN** o gestor aplica um filtro de datas para um período sem qualquer viagem realizada pela organização
- **THEN** o painel analítico apresenta os indicadores a zero e sugere o alargamento do intervalo de datas da pesquisa (BR-03)