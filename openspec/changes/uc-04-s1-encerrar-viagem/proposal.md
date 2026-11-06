# Proposal: UC-04.S1 Encerramento de Viagem e Bloqueio de Cadeado em Doca Oficial

## Why
Garantir a devolução ordenada e segura das e-bikes nas infraestruturas dedicadas (docas oficiais), confirmando o bloqueio mecânico do veículo, cessando a contagem de tempo da viagem e apresentando de imediato ao utilizador o impacto ambiental positivo gerado.

## What Changes
- Deteção do fecho físico do cadeado IoT através de sensores embarcados na e-bike.
- Validação no backend de que as coordenadas de devolução estão dentro do raio de tolerância (geofence) de uma doca oficial (BR-04).
- Transição de estado da viagem para «Concluída» e da e-bike para «Disponível» na respetiva doca.
- Cálculo automático das métricas da sessão: duração em minutos, distância em quilómetros e $CO_2$ evitado.
- Apresentação do ecrã de resumo pós-viagem na aplicação móvel.

## Capabilities

### New Capabilities
- `encerramento-viagem`: Validação geográfica de doca oficial, receção de telemetria de trancamento físico e consolidação de métricas pós-viagem.

### Modified Capabilities

## Impact
- Camada IoT: emissão de pacote MQTT cifrado aquando do engate do fecho inteligente (RNF-06).
- Backend: serviço de validação geoespacial de docas e consolidação transacional de viagens.
- Frontend móvel: encerramento da vista de viagem ativa e exibição do ecrã de resumo e impacto ecológico.