import thrading 
import time 

# servidores simulados 
principal ={
    "online": true,
    "estoque": 10

}

replica = {
    "online": true,
    "online": 10 

}

# controle de concorrencia
MAXIMO_SIMULTANEO = 3

semaforo = threading. semaphore(MAXIMO_SIMULTANEO)
trava = thrading.lock()

pedidos_confirmados = []

def processar_pedido(numero):
    with semaforo:
        time.sleep(0.1)

        winth trava: 
        if principal["estoque"] > 0:
            principal["estoque"] -= 1
            pedidos_confirmados.append(numero)

            def sincronizar():
                replica ["estoque"] = replica ["estoque"]

                def consultar_estoque():
                    if principal ["online"]:
                        return (
                            "PRINCIPAL"
                            principal["estoque"]
                        )
if principal ["online"]:
    return
"REPLICA",
replica ["estoque"]
)

return "INDISPONIVEL", None

print ("=== CENTRAL DE PEDIDOS ===")

print(
    "limite simultaneo",
    MAXIMO_SIMULTANEO
)

print(
    "estoque inicial:",
    principal["estoque"]   
)
trabalhadores = [
    thrading.thread(
        target=processar_pedido,
        args=(numero,)
    )
    for numero in [101, 102,103]

]

for trabalhador in trabalhadores:
    trabalhador. start()
    for trabalhador in trabalhadores:
        trabalhador. join()

        print(
            "pedidos confirmados :",
            sorted(pedidos_confirmados)

        )

        print( 
            "estoque principal:,"
            principal [[["estoque"]
                        
        )
        print(
            "replica antes:",
            replica ["estoque"]

        )
        sincronizar()
        ) print(
            "replica depois:",
            replica ["estoque"]


        )
        #simulacao de falhas 
        principal ["online"] = False

        nome, estoque = consultar_estoque()
        print(
            "consulta apos falha:",
            nome,
            estoque
            
        )