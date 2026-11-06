# Proposal: UC-01.S1 Destrancar e Iniciar Viagem via QR Code

## Why
Disponibilizar aos utilizadores elegíveis uma forma rápida, autónoma e sem atrito de destrancar uma bicicleta elétrica numa doca oficial através da leitura ótica de um código QR na app móvel, dando início imediato à contagem da viagem.

## What Changes
- Leitura e descodificação do código QR da e-bike na aplicação móvel.
- Validação no backend da elegibilidade do utilizador (sessão ativa, sem viagens simultâneas - BR-06).
- Verificação de que a e-bike se encontra disponível e com nível de bateria operacional >20% (BR-05).
- Envio de comando remoto IoT para abertura do fecho inteligente em menos de 3 segundos (RNF-01).
- Transição de estado da bicicleta para «Em Viagem» e início do registo de viagem.

## Capabilities

### New Capabilities
- `desbloqueio-ebike`: Mecanismo de leitura ótica, validações de início de sessão de mobilidade e comando de destrancamento ciber-físico.

### Modified Capabilities

## Impact
- Frontend móvel: módulo de câmara/scanner de QR Code e ecrã de transição para "Viagem Ativa".
- Backend: endpoint de reserva/início de viagem e emissão de mensagens de controlo para o broker MQTT.
- Camada IoT: receção de comando de desbloqueio pelo atuador do fecho físico da e-bike.