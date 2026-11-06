# Design: UC-08.S1 Consulta de Dashboard ESG e Relatórios

## Context
As métricas de sustentabilidade alimentam relatórios corporativos oficiais de sustentabilidade (ESG). O processamento de relatórios não pode comprometer a performance transacional do backend.

## Goals / Non-Goals

**Goals:**
- Agregação atómica de viagens por organização parceira (`OrganizacaoCliente`).
- Cálculo auditável de emissões: $CO_2\text{ evitado (kg)} = \text{distância (km)} \times \text{fator de emissão automóvel}$ (BR-03).
- Resposta rápida na geração de relatórios (< 5 segundos - RNF-04).
- Anonimização total: conformidade estrita com o RGPD (sem identificação de quem fez cada viagem).

**Non-Goals:**
- Gestão de créditos de carbono ou transações em mercados voluntários de carbono.
- Ranking individual de colaboradores (privacidade de dados).

## Decisions

- **Decisão 1:** Tabela de agregação analítica `MetricaESG` para evitar varrimentos pesados na tabela `Viagem` a cada carregamento de página.
- **Decisão 2:** Geração de relatórios PDF no backend utilizando templates leves em HTML-to-PDF com gráficos estáticos embutidos.

## Risks / Trade-offs

- **Risco:** Desfasamento de dados caso as agregações ocorram em batch diferido.
  - **Mitigação:** Atualização incremental da tabela `MetricaESG` sempre que uma viagem transita para «Concluída» (UC-04).