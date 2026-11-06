# Design: UC-06.S1 Monitorização de Telemetria e Baterias da Frota

## Context
A gestão de frotas de micromobilidade elétrica exige monitorização em tempo real para evitar baterias esgotadas e bicicletas fora de serviço, mantendo canais de comunicação cifrados e leves.

## Goals / Non-Goals

**Goals:**
- Ingestão assíncrona de eventos de telemetria sem bloqueio de base de dados.
- Notificação em tempo real para a consola web via WebSockets ou Server-Sent Events (SSE).
- Classificação visual dos veículos por severidade de bateria (BR-05).
- Mecanismo de heartbeat/watchdog para deteção de falha de conectividade (timeout > 2 horas).

**Non-Goals:**
- Bloqueio remoto do motor elétrico da bicicleta (reservado para o slice UC-06.S2 do Épico 3).
- Gestão de ordens de serviço presenciais para técnicos mecânicos (UC-05).

## Decisions

- **Decisão 1:** Uso de broker MQTT com suporte a canais cifrados TLS 1.3 (porta 8883) e tópicos estruturados por ID (`unibike/telemetry/{id_ebike}`).
- **Decisão 2:** Tarefa periódica (background worker a correr a cada 5 minutos) para inspecionar o último timestamp recebido de cada e-bike e atualizar para «Sem Sinal».

## Risks / Trade-offs

- **Risco:** Elevado volume de dados de GPS a sobrecarregar o tráfego móvel da bicicleta quando imobilizada.
  - **Mitigação:** Intervalo dinâmico de telemetria: 15s quando em andamento e 5 minutos quando estacionada e trancada na doca.