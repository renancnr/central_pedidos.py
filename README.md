ETAPA 1 e 2 
PROBLEMA A B 
| Informação | Resultado |
|---|---:|
| Estoque inicial | 10 |
| Limite simultâneo | 3 |
| Pedidos confirmados | 101, 102 e 103 |
| Estoque do servidor principal | 7 |
| Estoque da réplica antes da sincronização | 10 |
| Estoque da réplica depois da sincronização | 7 |
| Consulta após falha do principal | `("REPLICA", 7)` |


ETAPA 3 PROBLEMA A
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

  
ETAPA 4 VALIDAÇÃO DO PROGRAMA 
A função responsável pela replicação é sincronizar().
A instrução original copiava o estoque da réplica para ela mesma.
Por isso, a réplica mantinha o valor antigo.
Corrigi para copiar o estoque do principal: replica["estoque"] = principal["estoque"].


ETAPA 5 ANALISE TECNICA 

1. O semáforo limita a quantidade de pedidos processados simultaneamente a três.
2. A sincronização mantém a réplica atualizada para que ela tenha o estoque correto caso o servidor principal falhe.
3. Tolerância a falhas é a capacidade de continuar funcionando quando um componente falha. No programa, a consulta usa a réplica quando o principal fica offline.
4. O lock permite que apenas uma thread por vez altere ou leia o estoque durante uma operação protegida, evitando conflitos entre pedidos simultâneos.
5. A sincronização deve acontecer depois do processamento dos pedidos, para copiar para a réplica o estoque já atualizado no principal.

  
