# Proposal: UC-06.S1 Monitorização de Telemetria e Baterias da Frota em Tempo Real

## Why
Dotar a equipa técnica e operacional da Uni-Bike de visibilidade contínua sobre a localização geográfica, estado de conectividade e percentagem de bateria de todas as e-bikes da frota, otimizando as rondas de recolha e recarga e prevenindo a perda de veículos.

## What Changes
- Ingestão contínua de pacotes de telemetria (GPS, nível de bateria, temperatura) emitidos pelas e-bikes via MQTT a intervalos $\le 30$ segundos (RNF-02).
- Apresentação em mapa interativo na consola web operacional com marcadores diferenciados por código de cores segundo a carga de bateria (BR-05).
- Deteção automática e geração de alerta técnico para qualquer bicicleta sem reporte de sinal há mais de 2 horas (transição para «Sem Sinal / Offline»).

## Capabilities

### New Capabilities
- `telemetria-frota`: Ingestão de pacotes ciber-físicos periódicos, renderização geoespacial em tempo real na consola web e monitorização de pulso de comunicação da frota.

### Modified Capabilities

## Impact
- Camada IoT: emissão regular de telemetria pelos módulos embarcados das bicicletas via MQTT com TLS 1.3 (RNF-06).
- Backend: pipeline de ingestão de telemetria, persistência em `TelemetriaLog` e canal WebSocket/SSE para a consola.
- Consola Web: módulo de mapa operacional com filtros por nível de bateria e estado da frota.