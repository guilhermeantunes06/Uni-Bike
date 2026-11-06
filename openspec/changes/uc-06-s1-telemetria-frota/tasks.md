# Tasks: UC-06.S1 Monitorização de Telemetria e Baterias da Frota

## 1. Infraestrutura IoT e Ingestão

- [ ] 1.1 Configurar tópicos MQTT de telemetria e permissões de acesso com encriptação TLS
- [ ] 1.2 Implementar worker de ingestão assíncrona para persistir registos na tabela `TelemetriaLog`
- [ ] 1.3 Implementar rotina periódica de heartbeat para sinalização de e-bikes sem sinal há mais de 2h

## 2. Backend e Streaming

- [ ] 2.1 Criar endpoint REST para consulta do estado consolidado atual da frota
- [ ] 2.2 Configurar canal WebSocket/SSE para difusão contínua de alterações de localização e bateria para a consola (RNF-02)

## 3. Consola Web e Testes

- [ ] 3.1 Desenvolver componente de mapa na consola (React/Next.js) com marcadores dinâmicos por código de cores (BR-05)
- [ ] 3.2 Implementar teste para o cenário CT-06.1 (taxa de atualização da consola em $\le 30s$)
- [ ] 3.3 Implementar teste para o cenário CT-06.3 (transição de estado para Sem Sinal)