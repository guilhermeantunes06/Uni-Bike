# Capability: desbloqueio-ebike

## Purpose
Gerir a validação e o comando ciber-físico de desbloqueio de bicicletas elétricas através de leitura de QR Code, assegurando restrições de elegibilidade e bateria.

## ADDED Requirements

### Requirement: UC-01.S1 Desbloqueio e Início de Viagem via QR Code
O sistema Uni-Bike SHALL permitir que um utilizador autenticado e elegível (BR-02) destranque uma e-bike no estado «Disponível» com bateria superior a 20% (BR-05), enviando um comando remoto via MQTT que resulte na abertura física do cadeado em tempo inferior a 3 segundos (RNF-01), alterando o estado do veículo para «Em Viagem» e impedindo viagens concorrentes em simultâneo (BR-06).

#### Scenario: CT-01.1 Desbloqueio bem-sucedido via QR Code
- **WHEN** um utilizador autenticado com perfil ativo e sem viagens em curso lê o código QR de uma e-bike funcional ancorada numa doca com bateria > 20%
- **THEN** o fecho inteligente abre em menos de 3 segundos (RNF-01), o estado da e-bike transita para «Em Viagem», a viagem é iniciada e a app exibe o ecrã de viagem ativa

