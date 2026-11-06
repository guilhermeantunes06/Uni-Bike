# Design: UC-07.S1 Autenticação Institucional Federada

## Context
O sistema opera em regime B2B, onde cada cliente institucional (Universidade ou Empresa) possui o seu próprio fornecedor de identidade (IdP). A solução não deve armazenar palavras-passe de utilizadores finais, delegando a autenticação nos protocolos OpenID Connect e SAML 2.0 (RNF-06).

## Goals / Non-Goals

**Goals:**
- Integração transparente com Google Workspace e Microsoft Entra ID via OAuth2/OIDC.
- Validação automática da elegibilidade do utilizador através do domínio de email e do estado do contrato da organização (BR-02).
- Emissão de tokens JWT com expiração configurada para comunicação segura com as APIs.

**Non-Goals:**
- Criação e gestão de palavras-passe locais para utilizadores finais (pay-per-use está expressamente fora de âmbito).
- Gestão interna de permissões federadas do lado da instituição cliente.

## Decisions

- **Decisão 1:** Adoção de tokens JWT (JSON Web Tokens) assinados assimetricamente (RS256) para controlo de sessão sem estado no backend.
- **Decisão 2:** Mapeamento dinâmico entre o domínio de email (`@ua.pt`) e a entidade `OrganizacaoCliente` na base de dados para validação de contratos ativos.

## Risks / Trade-offs

- **Risco:** Indisponibilidade do IdP institucional da universidade impede o login do utilizador.
  - **Mitigação:** Tratamento graceful de timeout na app com mensagem explicativa e retenção de refresh token seguro para sessões previamente ativas.