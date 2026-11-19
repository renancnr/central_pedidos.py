Etapa 1 e 2 da prova 
| Informação | Resultado |
|---|---:|
| Estoque inicial | 10 |
| Limite simultâneo | 3 |
| Pedidos confirmados | 101, 102 e 103 |
| Estoque do servidor principal | 7 |
| Estoque da réplica antes da sincronização | 10 |
| Estoque da réplica depois da sincronização | 7 |
| Consulta após falha do principal | `("REPLICA", 7)` |


etapa 3
investigaçao e correção dos problemas 
1. A variável que define o limite é MAXIMO_SIMULTANEO.
2. O valor anterior era 3.
3. Alterei o valor para 2 e corrigi os erros que impediam o script de funcionar.
