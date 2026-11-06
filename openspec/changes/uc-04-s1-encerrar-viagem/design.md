# Design: UC-04.S1 Encerramento de Viagem e Bloqueio em Doca Oficial

## Context
A devolução e imobilização em docas formais é a regra nuclear do modelo de operação partilhada da Uni-Bike (BR-04), evitando o abandono desordenado de veículos em vias públicas e assegurando a segurança física da frota.

## Goals / Non-Goals

**Goals:**
- Reconhecimento automático do trancamento mecânico do fecho IoT.
- Algoritmo de validação de geofence circular com raio configurável por doca (`raio_geofence_m`).
- Cálculo atómico das emissões de $CO_2$ poupadas no momento de fecho da viagem.
- Reatribuição da e-bike à respetiva doca de destino (`doca_destino_id`).

**Non-Goals:**
- Deteção de estacionamento ilegal e aplicação de penalizações/multas (reservado para o slice UC-04.S2).
- Procedimento de contingência por Bluetooth em caso de perda de sinal de rede móvel (reservado para UC-04 exceção E2).

## Decisions

- **Decisão 1:** A validação espacial da doca baseia-se na fórmula de Haversine calculada no backend a partir das coordenadas GPS do módulo IoT da bicicleta.
- **Decisão 2:** Atualização atómica em transação única da base de dados: encerramento da viagem, libertação do utilizador para novas viagens e marcação da bicicleta como disponível na doca.

## Risks / Trade-offs

- **Risco:** Desvios momentâneos de sinal GPS junto a edifícios altos do campus.
  - **Mitigação:** Raio de tolerância (geofence) calibrado com margem de segurança de 15 metros em torno de cada doca.