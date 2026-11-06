# Capability: autenticacao

## Purpose
Disponibilizar autenticação federada institucional para utilizadores e gestores, garantindo acesso seguro e verificação de elegibilidade contratual da organização parceira.

## ADDED Requirements

### Requirement: UC-07.S1 Autenticação Federada via SSO
O sistema Uni-Bike SHALL redirecionar o utilizador para o fornecedor de identidade institucional configurado (Google Workspace ou Microsoft Entra ID), validar a assinatura do token de retorno e confirmar que o domínio do email pertence a uma organização cliente com contrato ativo (BR-02), emitindo um token JWT de sessão cifrado via TLS 1.3 (RNF-06).

#### Scenario: CT-07.1 Autenticação com credenciais corporativas válidas
- **WHEN** o utilizador seleciona "Entrar com Conta Institucional" e introduz credenciais válidas com domínio reconhecido e contrato ativo
- **THEN** o sistema autentica a identidade federada, valida o vínculo institucional ativo (BR-02), emite um token JWT assinado e concede acesso imediato à aplicação (RNF-06)

#### Scenario: CT-07.2 Autenticação com perfil suspenso ou domínio não autorizado
- **WHEN** o utilizador tenta autenticar-se via SSO mas o perfil local encontra-se com estado «Suspenso» ou a organização parceira não possui contrato ativo
- **THEN** o sistema recusa a autenticação, bloqueia a emissão de sessão e exibe a mensagem de conta inativa/suspensa (BR-02)