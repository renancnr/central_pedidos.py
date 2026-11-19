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
  1. A função de sincronização é sincronizar().
2. A instrução correta para atualizar a réplica é:
   replica["estoque"] = principal["estoque"]
3. A réplica não recebia o valor atualizado porque a instrução original copiava o estoque dela mesma:
   replica["estoque"] = replica["estoque"]
   Assim, o valor antigo permanecia igual.
4. Corrigi a instrução para copiar o estoque do servidor principal para a réplica. Depois dos três pedidos, ambos ficam com 7 unidades.

  
