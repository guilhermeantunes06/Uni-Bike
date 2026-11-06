# Tasks: UC-07.S1 Autenticação Institucional Federada

## 1. Modelação e Base de Dados

- [ ] 1.1 Criar migrações para as entidades `OrganizacaoCliente` e `UtilizadorFinal` com campos de SSO e estado de perfil
- [ ] 1.2 Implementar serviço de verificação de domínio de email e contrato institucional (BR-02)

## 2. Backend e Integração SSO

- [ ] 2.1 Configurar endpoints OAuth2/OIDC para Google Workspace e Microsoft Entra ID
- [ ] 2.2 Implementar callback de receção de tokens do IdP e geração de JWT seguro (RNF-06)
- [ ] 2.3 Implementar middleware de autenticação e proteção de rotas da API

## 3. Frontend e Testes de Aceitação

- [ ] 3.1 Integrar botão de login institucional na aplicação móvel e consola web
- [ ] 3.2 Implementar teste de integração para o cenário CT-07.1 (sucesso de login)
- [ ] 3.3 Implementar teste de integração para o cenário CT-07.2 (rejeição de conta inativa)