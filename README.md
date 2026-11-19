# P2 – SISTEMAS DISTRIBUÍDOS

**Aluno:** Renan dos Santos Carneiro  
**Semestre:** 3º semestre

## ETAPAS 1 E 2 – PROBLEMA AB

### Resultados esperados

| Informação | Resultado |
|---|---:|
| Estoque inicial | 10 |
| Limite de pedidos simultâneos | 3 |
| Pedidos confirmados | 101, 102 e 103 |
| Estoque do servidor principal | 7 |
| Estoque da réplica antes da sincronização | 10 |
| Estoque da réplica depois da sincronização | 7 |
| Consulta após falha do principal | `("REPLICA", 7)` |

## ETAPA 3 – PROBLEMA A: INVESTIGAÇÃO E CORREÇÃO DOS PROBLEMAS

A variável responsável por definir o limite de processamento simultâneo é `MAXIMO_SIMULTANEO`.

- Limite utilizado no programa: **3 pedidos simultâneos**.
- Os erros de sintaxe, importação, indentação e estrutura das funções foram corrigidos.
- O limite foi mantido em 3 para corresponder aos resultados registrados nas Etapas 1 e 2.

A função responsável pela sincronização é `sincronizar()`.

A instrução correta para atualizar a réplica é:

```python
replica["estoque"] = principal["estoque"]
```

A instrução incorreta copiava o estoque da réplica para ela mesma:

```python
replica["estoque"] = replica["estoque"]
```

Assim, o valor antigo permanecia inalterado. A correção faz com que o estoque atualizado do servidor principal seja copiado para a réplica. Após os três pedidos, ambos ficam com 7 unidades.

## ETAPA 4 – VALIDAÇÃO DO PROGRAMA

A função responsável pela replicação dos dados é `sincronizar()`.

A instrução original copiava o estoque da réplica para ela mesma, impedindo a atualização. Ela foi corrigida para copiar o valor do servidor principal:

```python
replica["estoque"] = principal["estoque"]
```

A sincronização é executada depois que todas as threads terminam o processamento dos pedidos. Dessa forma, a réplica recebe o estoque atualizado do servidor principal.

O programa também simula a falha do servidor principal. Quando isso acontece, a função `consultar_estoque()` consulta a réplica, que retorna o valor sincronizado.

## ETAPA 5 – ANÁLISE TÉCNICA

### 1. Semáforo

O semáforo limita a quantidade de pedidos que podem estar em processamento simultaneamente. Neste programa, o limite é de três threads.

### 2. Sincronização

A sincronização mantém a réplica atualizada. Ela copia o estoque do servidor principal depois do processamento dos pedidos, permitindo que a réplica seja utilizada em caso de falha do principal.

### 3. Tolerância a falhas

É a capacidade de um sistema continuar oferecendo determinado serviço mesmo quando um componente falha. No programa, quando o servidor principal fica offline, a consulta utiliza a réplica, desde que ela esteja disponível.

### 4. Bloqueio (Lock)

O bloqueio protege a região crítica que acessa e altera o estoque. Assim, apenas uma thread por vez executa essa operação protegida, evitando condições de corrida.

### 5. Momento da sincronização

A sincronização acontece depois que todas as threads concluem os pedidos. Isso permite copiar para a réplica o estoque já atualizado no servidor principal.

---

## COMO EXECUTAR

É necessário ter Python 3 instalado. O programa utiliza apenas bibliotecas padrão do Python.

No terminal, dentro da pasta do projeto, execute:

```bash
python central_pedidos.py
```

## RESULTADO ESPERADO

```text
=== CENTRAL DE PEDIDOS ===
Limite simultaneo: 3
Estoque inicial: 10
Pedidos confirmados: [101, 102, 103]
Estoque principal: 7
Replica antes: 10
Replica depois: 7
Consulta apos falha: ('REPLICA', 7)
```

**Observação:** este projeto é uma simulação didática de concorrência, replicação de estoque e tolerância a falhas. Os servidores principal e réplica são estruturas em memória, não servidores distribuídos reais.

---

**P2 – SISTEMAS DISTRIBUÍDOS**
