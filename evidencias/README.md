# Evidências da P2

- `evidencia1.png` - primeira execução, antes das correções.
- === CENTRAL DE PEDIDOS ===
Limite simultaneo: 3
Estoque inicial: 10
Pedidos confirmados: [101, 102, 103]
Estoque principal: 7
Replica antes: 10
Replica depois: 7
Consulta apos falha: ('REPLICA', 7)


- `evidencia2.png` - execução após a correção da concorrência.
- === CENTRAL DE PEDIDOS ===
Limite simultaneo: 2
Estoque inicial: 10
Pedidos confirmados: [101, 102, 103]
Estoque principal: 7


- `evidencia3.png` - estoque principal e réplica após a sincronização.
- Estoque principal: 7
Replica antes: 10
Replica depois: 7


- `evidencia4.png` - consulta após a falha do servidor principal.
- Servidor principal: OFFLINE
Servidor replica: ONLINE
Consulta apos falha: ('REPLICA', 7)


- `evidencia5.png` - execução completa após as três correções.
- === CENTRAL DE PEDIDOS ===
Limite simultaneo: 2
Estoque inicial: 10
Pedidos confirmados: [101, 102, 103]
Estoque principal: 7
Replica antes: 10
Replica depois: 7
Consulta apos falha: ('REPLICA', 7)

  
