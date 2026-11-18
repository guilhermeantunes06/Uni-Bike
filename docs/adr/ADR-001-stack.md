# ADR-001: Escolha da Stack Tecnológica e Ferramenta de Testes

**Data:** 2026-11-18  
**Estado:** Aceite

## Contexto
Para o 1.º incremento do projeto **Uni-Bike**, o sistema necessita de uma aplicação web que disponibilize uma interface de serviços (API REST) para suportar os 5 *slices* do Épico 1 (autenticação SSO, destrancar/trancar eBike, telemetria da frota e dashboard ESG). Adicionalmente, a aplicação web tem de ser testável de ponta a ponta com Playwright e permitir a criação de testes automáticos por *scenario* definido no OpenSpec.

A equipa tem maior familiaridade e fluência em Python do que em TypeScript/Node.js ou Java, sendo importante escolher uma stack que minimize a fricção de arranque e maximize a produtividade entre o Lab 10 e o Lab 11.

## Decisão
Adotar uma arquitetura baseada em **Python**:
* **Backend / API REST:** Python com **FastAPI** (com validação de dados via Pydantic).
* **Frontend:** Aplicação Web leve em **HTML5 / CSS3 / JavaScript** (servida pelo próprio backend ou estática), com identificadores estáveis (`data-testid`) para suportar testes automáticos no browser.
* **Base de Dados:** **SQLite** (com SQLAlchemy ou `sqlite3` nativo), permitindo persistência local em ficheiro único e reposição rápida do estado antes dos testes.
* **Testes Automáticos (1.º Incremento):** **pytest** (com `TestClient` do FastAPI para testes de API/integração e unidade) e **Playwright (Python)** (`pytest-playwright`) para testes E2E no browser.

## Alternativas Consideradas
1. **Node.js / TypeScript (Express/Fastify + React + Vitest):**
   * *Prós:* Linguagem única entre frontend e backend; integração nativa com Playwright em TS.
   * *Motivo da rejeição:* A equipa não domina TypeScript, o que aumentaria o risco de atrasos e erros de tipagem/configuração durante o curto prazo da iteração.
2. **Java (Spring Boot + React + JUnit):**
   * *Prós:* Robusto e fortemente tipado.
   * *Motivo da rejeição:* Maior verbosidade e complexidade na configuração inicial (Maven/Gradle, entidades JPA, servidores) para o âmbito do 1.º incremento.

## Consequências
* **Positivas:**
  * Curva de aprendizagem reduzida e implementação mais rápida por toda a equipa.
  * O FastAPI gera automaticamente a especificação OpenAPI (`openapi.yaml`), facilitando o alinhamento com o contrato de serviços exigido no E5 e no OpenSpec.
  * Base de dados SQLite dispensa serviços externos ou Docker para desenvolvimento local e permite limpar/repor facilmente os dados entre execuções de testes.
  * Suporte oficial de **Playwright em Python**, mantendo os testes unitários, de API e E2E na mesma linguagem e executor (`pytest`).
* **Negativas / Riscos:**
  * O SQLite tem limitações de escrita concorrente em produção em larga escala; no entanto, como o acesso aos dados será isolado numa camada de repositório/persistência, poderá ser migrado para PostgreSQL numa iteração futura sem alterar a lógica de domínio.
