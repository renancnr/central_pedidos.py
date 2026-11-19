# P2 – SISTEMAS DISTRIBUÍDOS

**Aluno:** Renan dos Santos Carneiro  
**Semestre:** 3º semestre

## ETAPAS 1 E 2 – PROBLEMA AB

### Resultados

| Item | Resposta |
|---|---:|
| Estoque inicial | 10 unidades |
| Limite de pedidos simultâneos | 3 |
| Pedidos confirmados | 101, 102 e 103 |
| Estoque do servidor principal após os pedidos | 7 unidades |
| Estoque da réplica antes da sincronização | 10 unidades |
| Estoque da réplica depois da sincronização | 7 unidades |
| Consulta após a falha do servidor principal | `("REPLICA", 7)` |

**Explicação:** os três pedidos foram processados e consumiram uma unidade cada. Por isso, o estoque do servidor principal passou de 10 para 7. Antes da sincronização, a réplica ainda armazenava o valor antigo (10). Depois da sincronização, ela também passou a armazenar 7.

## ETAPA 3 – PROBLEMA A: IDENTIFICAÇÃO E CORREÇÃO DOS ERROS

**1. Qual variável define o limite de pedidos simultâneos?**

A variável é `MAXIMO_SIMULTANEO`, configurada com o valor **3**.

**2. Qual função realiza a sincronização entre o servidor principal e a réplica?**

A função é `sincronizar()`.

**3. Qual era o erro na instrução de sincronização e como deve ser corrigido?**

A instrução incorreta copiava o valor da réplica para ela mesma:

```python
replica["estoque"] = replica["estoque"]
```

A forma correta copia o estoque atualizado do servidor principal para a réplica:

```python
replica["estoque"] = principal["estoque"]
```

**4. O que a correção resolve?**

Ela permite que a réplica receba o valor atualizado do estoque. Após os três pedidos, o estoque do principal é 7 e, depois da sincronização, o estoque da réplica também passa a ser 7.

## ETAPA 4 – VALIDAÇÃO DO PROGRAMA

A sincronização correta é realizada pela função `sincronizar()`, que copia o estoque do servidor principal para a réplica:

```python
replica["estoque"] = principal["estoque"]
```

A sincronização ocorre após o término do processamento dos pedidos. Assim, a réplica recebe o valor atualizado. Quando o servidor principal fica indisponível, a função `consultar_estoque()` utiliza a réplica, desde que ela esteja online.

**Resultado da consulta após a falha do servidor principal:** `("REPLICA", 7)`.

## ETAPA 5 – ANÁLISE TÉCNICA

**1. Qual é a função do semáforo no programa?**

O semáforo controla o acesso concorrente e limita a quantidade de pedidos que podem ser processados simultaneamente. Neste programa, o limite configurado é de **3**.

**2. Qual é a importância da sincronização da réplica?**

A sincronização mantém a réplica atualizada com os dados do servidor principal. Dessa forma, ela pode ser utilizada como alternativa de consulta quando o servidor principal fica indisponível.

**3. O que significa tolerância a falhas neste contexto?**

É a capacidade de continuar oferecendo o serviço mesmo quando um componente apresenta falha. No programa, se o servidor principal ficar offline e a réplica estiver disponível, a consulta é realizada na réplica.

**4. Qual é a função do Lock?**

O Lock protege a região crítica que acessa e modifica o estoque. Ele garante que apenas uma thread por vez execute essa parte protegida, evitando condições de corrida e alterações conflitantes.

**5. Em que momento a sincronização deve acontecer?**

Após o término do processamento dos pedidos. Assim, a réplica recebe o valor final e atualizado do estoque do servidor principal.

---

**P2 – SISTEMAS DISTRIBUÍDOS**
