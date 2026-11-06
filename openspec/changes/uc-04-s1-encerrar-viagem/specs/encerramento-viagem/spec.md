# Capability: encerramento-viagem

## Purpose
Gerir o processo de devolução e trancamento físico das bicicletas elétricas em docas oficiais autorizadas, consolidando as métricas de tempo, distância e descarbonização.

## ADDED Requirements

### Requirement: UC-04.S1 Devolução em Doca Oficial e Bloqueio Físico
O sistema Uni-Bike SHALL detetar o trancamento mecânico do fecho inteligente, validar que a localização reportada pela e-bike se encontra dentro do raio de geofencing de uma doca oficial autorizada (BR-04), registar o encerramento da viagem em menos de 3 segundos (RNF-01), colocar o veículo no estado «Disponível» e calcular a distância percorrida, tempo de viagem e o $CO_2$ evitado.

#### Scenario: CT-04.1 Encerramento bem-sucedido de viagem em doca oficial
- **WHEN** o utilizador com viagem ativa imobiliza a e-bike numa vaga livre de uma doca oficial e fecha manualmente o fecho inteligente
- **THEN** o módulo IoT envia o sinal de bloqueio via canal cifrado (RNF-06), o sistema confirma a presença na doca oficial (BR-04), encerra a viagem, repõe o estado da e-bike como «Disponível» e exibe na app o resumo com duração, distância e $CO_2$ poupado