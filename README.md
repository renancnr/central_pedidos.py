
P2 – SISTEMAS DISTRIBUÍDOS

Aluno: Renan dos Santos Carneiro
Semestre: 3º semestre


ETAPA 1 E 2 – PROBLEMA AB

Resultados obtidos

Informação	Resultado
Estoque inicial	10
Limite de pedidos simultâneos	3
Pedidos confirmados	101, 102 e 103
Estoque do servidor principal	7
Estoque da réplica antes da sincronização	10
Estoque da réplica depois da sincronização	7
Consulta após falha do principal	("REPLICA", 7)

⸻

ETAPA 3 – PROBLEMA A: INVESTIGAÇÃO E CORREÇÃO DOS PROBLEMAS

A variável responsável por definir o limite de processamento simultâneo é MAXIMO_SIMULTANEO.

* Valor anterior: 3.
* Novo valor: 2.
* Também foram corrigidos os erros que impediam a execução do script.

Função responsável pela sincronização:

sincronizar()

Instrução correta para atualizar a réplica:

replica["estoque"] = principal["estoque"]

A réplica não recebia o valor atualizado porque a instrução original copiava o estoque dela mesma:

replica["estoque"] = replica["estoque"]

Dessa forma, o valor antigo permanecia inalterado.

A correção foi realizada para copiar o estoque atualizado do servidor principal para a réplica. Após o processamento dos três pedidos, ambos ficaram com 7 unidades.

⸻

ETAPA 4 – VALIDAÇÃO DO PROGRAMA

A função responsável pela replicação dos dados é sincronizar().

Foi identificado que a instrução original copiava o estoque da réplica para ela mesma, fazendo com que o valor antigo fosse mantido.

A instrução foi corrigida para:

replica["estoque"] = principal["estoque"]

Após a correção, a réplica passou a receber corretamente os dados atualizados do servidor principal, garantindo que o estoque permanecesse consistente.

⸻

ETAPA 5 – ANÁLISE TÉCNICA

1. Semáforo

O semáforo limita a quantidade de pedidos processados simultaneamente. No programa, esse limite é de três pedidos.

2. Sincronização

A sincronização mantém a réplica atualizada, garantindo que ela tenha o estoque correto caso o servidor principal apresente uma falha.

3. Tolerância a falhas

É a capacidade de um sistema continuar funcionando mesmo quando algum componente apresenta falha. No programa, quando o servidor principal fica offline, a consulta é realizada na réplica.

4. Bloqueio (Lock)

O bloqueio permite que apenas uma thread por vez altere ou consulte o estoque durante uma transação protegida, evitando conflitos entre pedidos simultâneos.

5. Momento da sincronização

A sincronização deve acontecer após o processamento dos pedidos, para copiar para a réplica o estoque já atualizado no servidor principal.

⸻

FIM DA AVALIAÇÃO – P2 SISTEMAS DISTRIBUÍDOS
