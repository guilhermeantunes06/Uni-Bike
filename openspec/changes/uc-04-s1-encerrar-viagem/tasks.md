# Tasks: UC-04.S1 Encerramento de Viagem e Bloqueio em Doca Oficial

## 1. Backend e Lógica Espacial

- [ ] 1.1 Implementar serviço de validação de geofencing para correspondência de docas (`DocaService.isWithinGeofence`)
- [ ] 1.2 Implementar transação de encerramento de viagem calculando duração, km e $CO_2$ evitado
- [ ] 1.3 Atualizar associação de doca e estado da e-bike para «Disponível» (BR-04)

## 2. Integração IoT e Mensagens

- [ ] 2.1 Subscrever tópico MQTT de notificação de bloqueio mecânico (`unibike/ebike/{id}/locked`)
- [ ] 2.2 Processar payload de encerramento contendo timestamp e coordenadas GPS

## 3. Frontend e Testes

- [ ] 3.1 Desenhar ecrã de resumo de conclusão de viagem na app móvel com métricas de sustentabilidade
- [ ] 3.2 Implementar teste de integração para o cenário CT-04.1 (devolução correta em doca oficial)