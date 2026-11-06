# Tasks: UC-08.S1 Consulta de Dashboard ESG e Relatórios

## 1. Modelação Analítica e Backend

- [ ] 1.1 Criar esquema da entidade `MetricaESG` e índices por organização e data
- [ ] 1.2 Implementar motor de cálculo de $CO_2$ evitado baseado no histórico de viagens (BR-03)
- [ ] 1.3 Criar endpoint analítico com filtros temporais (`GET /api/v1/esg/dashboard`)

## 2. Motor de Exportação

- [ ] 2.1 Desenvolver serviço de compilação de relatórios PDF executivos e exportação CSV
- [ ] 2.2 Otimizar queries e pipeline de geração para garantir tempo de resposta < 5s (RNF-04)

## 3. Consola Web e Testes

- [ ] 3.1 Construir ecrã de Dashboard ESG no portal B2B com cartões de métricas e gráficos temporais
- [ ] 3.2 Implementar teste para o cenário CT-08.1 (geração de relatório em < 5s)
- [ ] 3.3 Implementar teste para o cenário CT-08.2 (comportamento com dados a zero)