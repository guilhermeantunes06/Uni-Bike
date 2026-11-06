# Design: UC-01.S1 Destrancar e Iniciar Viagem via QR Code

## Context
O processo de desbloqueio liga o mundo digital (app móvel e APIs) ao mundo físico (tranca IoT da bicicleta). O utilizador precisa de uma resposta quase instantânea ($\le 3s$) junto à doca.

## Goals / Non-Goals

**Goals:**
- Leitura instantânea de identificador único de bicicleta através de QR Code.
- Verificação atómica de regras de negócio: utilizador ativo (BR-02), bateria >20% (BR-05) e ausência de outra viagem em curso (BR-06).
- Disparo de mensagem de desbloqueio ao módulo IoT via protocolo MQTT sobre TLS 1.3.

**Non-Goals:**
- Inserção de código manual alfanumérico (reservado para o slice UC-01.S2).
- Gestão de reservas antecipadas (reservado para UC-03).

## Decisions

- **Decisão 1:** Comunicação assíncrona com o hardware através de tópicos MQTT dedicados por e-bike (`unibike/ebike/{id_ebike}/unlock`).
- **Decisão 2:** Validação atómica na base de dados para evitar condições de corrida (duas pessoas a tentar ler o mesmo QR Code em simultâneo).

## Risks / Trade-offs

- **Risco:** Latência ou perda de pacote na rede móvel da bicicleta (NB-IoT/LTE-M).
  - **Mitigação:** Timeout de 5 segundos no backend. Se a tranca não confirmar a abertura física, a transação reverte para «Disponível» e o utilizador é notificado.