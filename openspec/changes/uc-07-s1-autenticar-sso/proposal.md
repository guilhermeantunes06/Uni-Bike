# Proposal: UC-07.S1 Autenticação Institucional Federada (SSO)

## Why
Permitir que os membros das organizações clientes (estudantes e colaboradores) acedam à plataforma Uni-Bike sem necessidade de criação manual de credenciais locais, garantindo a validação automática do vínculo institucional e do estado do contrato da organização no momento do login.

## What Changes
- Introdução do fluxo de autenticação federada via OAuth2/OpenID Connect e SAML (Google Workspace e Microsoft Entra ID).
- Validação automática do domínio de email institucional contra a lista de organizações parceiras com contrato ativo (BR-02).
- Emissão de token JWT assinado para sessões seguras na aplicação móvel e consola web (RNF-06).

## Capabilities

### New Capabilities
- `autenticacao`: Suporte a autenticação institucional federada (SSO), verificação de elegibilidade e gestão de sessão por tokens.

### Modified Capabilities

## Impact
- Impacto nos componentes de Backend (serviço de autenticação e validação de tokens).
- Impacto nos frontends (ecrã inicial de login da app móvel e portal web).
- Sem impacto em base de dados legada (funcionalidade nuclear nova).