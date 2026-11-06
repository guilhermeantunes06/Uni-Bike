# Tasks: UC-01.S1 Destrancar e Iniciar Viagem via QR Code

## 1. Backend e Lógica de Domínio

- [ ] 1.1 Criar endpoint de validação de início de viagem (`POST /api/v1/trips/unlock`)
- [ ] 1.2 Implementar verificações de bateria (>20%) e viagem ativa concorrente (BR-05, BR-06)
- [ ] 1.3 Configurar publicação de comando de desbloqueio no broker MQTT

## 2. Camada Ciber-Física (IoT)

- [ ] 2.1 Subscrever tópico de comando de destrancamento no microcontrolador da e-bike
- [ ] 2.2 Implementar envio de mensagem de confirmação de destrancamento mecânico

## 3. Aplicação Móvel e Testes

- [ ] 3.1 Implementar leitor de QR Code na aplicação com validação de formato
- [ ] 3.2 Construir transição para o ecrã de viagem ativa após confirmação
- [ ] 3.3 Implementar teste de integração para o cenário CT-01.1 (desbloqueio bem-sucedido)
- [ ] 3.4 Implementar teste de integração para o cenário CT-01.3 (recusa por bateria < 20%)