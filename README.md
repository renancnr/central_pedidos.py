# P2 - Sistemas Distribuídos

**Aluno(a):** Renan dos Santos Carneiro  
**Professora:** Simone Tatiane do Canto  
**Data:** 18/11/2026

## 1. Situação-problema

A Central de Pedidos apresentava três problemas: permitia três pedidos ao mesmo tempo, a réplica não recebia o estoque atualizado e a consulta não utilizava corretamente a réplica quando o servidor principal falhava.

## 2. Primeira execução

Na primeira execução, o programa mostrava o estoque inicial de 10 unidades e processava os três pedidos. O limite de processamento estava configurado como 3.

**Evidência 1:** adicionar a captura da primeira execução, antes das correções, em `evidencias/evidencia1.png`.

## 3. Problema A - Concorrência

**Qual problema foi identificado?**

O limite estava configurado para permitir três pedidos simultâneos, mas a regra da empresa permite apenas dois.

**Qual alteração foi realizada?**

O valor de `MAXIMO_SIMULTANEO` foi alterado de 3 para 2. Os três pedidos continuam sendo processados, mas no máximo dois ao mesmo tempo.

**Evidência 2:** adicionar a captura da execução após a alteração em `evidencias/evidencia2.png`.

## 4. Problema B - Replicação e consistência

**Qual problema foi identificado?**

A réplica continuava com o estoque antigo porque a função de sincronização copiava o valor dela mesma.

**Qual alteração foi realizada?**

Na função `sincronizar()`, a atribuição foi corrigida para copiar o estoque do servidor principal:

```python
replica["estoque"] = principal["estoque"]
```

**Evidência 3:** adicionar a captura mostrando o estoque principal e o da réplica após a sincronização em `evidencias/evidencia3.png`.

## 5. Problema C - Tolerância a falhas

**Qual problema foi identificado?**

A consulta não verificava corretamente se a réplica estava disponível quando o servidor principal ficava offline.

**Qual alteração foi realizada?**

A função `consultar_estoque()` foi ajustada para consultar o principal quando estiver online e utilizar a réplica quando o principal estiver indisponível.

**Evidência 4:** adicionar a captura da consulta após a falha do servidor principal em `evidencias/evidencia4.png`.

## 6. Validação do programa

Após as três correções, o programa deve apresentar limite simultâneo de 2, confirmar os pedidos 101, 102 e 103, atualizar o estoque principal para 7, sincronizar a réplica para 7 e consultar a réplica após a falha do principal.

**Evidência 5:** adicionar a captura da execução completa em `evidencias/evidencia5.png`.

## 7. Análise técnica

### Questão 1

**Qual é a função do semáforo no processamento dos pedidos?**

O semáforo controla quantos pedidos podem ser processados ao mesmo tempo. Neste programa, permite no máximo dois.

### Questão 2

**Por que é necessário sincronizar os dados entre o servidor principal e a réplica?**

Para manter os dois servidores com o mesmo estoque atualizado. Assim, a réplica pode ser usada quando o principal falhar.

### Questão 3

**O que significa tolerância a falhas e como ela aparece neste programa?**

É quando o sistema continua funcionando mesmo com a falha de um servidor. Aqui, a consulta usa a réplica quando o servidor principal fica offline.

### Questão 4

**Para que serve o Lock no programa e como ajuda a prevenir problemas de concorrência?**

O Lock protege o acesso ao estoque. Ele evita que duas threads alterem esse valor ao mesmo tempo.

### Questão 5

**A sincronização do estoque deve acontecer antes ou depois do processamento dos pedidos? Explique a relação de causalidade.**

Deve acontecer depois do processamento. Primeiro os pedidos alteram o estoque principal e, em seguida, a réplica recebe o valor atualizado.

## 8. Conclusão

Com esta atividade, aprendi como controlar pedidos simultâneos usando semáforo e Lock. Também entendi a importância de manter a réplica atualizada. A simulação mostrou como ela pode ajudar quando o servidor principal fica indisponível.

## 9. Entrega

**Aluno(a):** Renan dos Santos Carneiro
