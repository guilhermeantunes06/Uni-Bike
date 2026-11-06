# Capability: telemetria-frota

## Purpose
Garantir a recolha contínua de telemetria operacional das bicicletas elétricas e a sua visualização em tempo real na consola web para suporte técnico e gestão proativa de baterias.

## ADDED Requirements

### Requirement: UC-06.S1 Monitorização de Telemetria e Baterias da Frota
O sistema Uni-Bike SHALL recolher pacotes de telemetria emitidos pelas e-bikes com intervalo máximo de 30 segundos (RNF-02) contendo coordenadas GPS e percentagem de bateria, atualizar o mapa da consola operacional em tempo real categorizando marcadores por nível de carga (BR-05) e assinalar como «Sem Sinal / Offline» qualquer e-bike que não comunique há mais de 2 horas consecutivas.

#### Scenario: CT-06.1 Atualização de telemetria em tempo real na consola
- **WHEN** o operador operacional acede ao painel de telemetria em tempo real na consola web
- **THEN** a consola apresenta a posição de todas as e-bikes ativas atualizada a cada 30 segundos (RNF-02), destacando com cores os níveis de carga (Verde >50%, Amarelo 20-50%, Vermelho <20%)

#### Scenario: CT-06.3 Deteção de e-bike offline ou sem sinal
- **WHEN** uma e-bike permanece sem emitir qualquer pacote de telemetria GPS/MQTT há mais de 2 horas
- **THEN** o sistema altera o estado do veículo para «Sem Sinal / Offline» e gera um alerta técnico prioritário no painel operacional (BR-05, RNF-02)