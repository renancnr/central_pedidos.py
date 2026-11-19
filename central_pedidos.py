import threading
import time

# Servidores simulados
principal = {
    "online": True,
    "estoque": 10,
}

replica = {
    "online": True,
    "estoque": 10,
}

# Controle de concorrencia
MAXIMO_SIMULTANEO = 3
semaforo = threading.Semaphore(MAXIMO_SIMULTANEO)
trava = threading.Lock()

pedidos_confirmados = []


def processar_pedido(numero):
    """Processa um pedido respeitando o limite de concorrencia e o estoque."""
    with semaforo:
        # Simula o tempo de processamento do pedido.
        time.sleep(0.1)

        # A regiao critica protege a leitura e a alteracao do estoque.
        with trava:
            if principal["estoque"] > 0:
                principal["estoque"] -= 1
                pedidos_confirmados.append(numero)
                return True

            return False


def sincronizar():
    """Copia o estoque do servidor principal para a replica."""
    with trava:
        replica["estoque"] = principal["estoque"]


def consultar_estoque():
    """Consulta o principal ou utiliza a replica em caso de falha."""
    with trava:
        if principal["online"]:
            return "PRINCIPAL", principal["estoque"]

        if replica["online"]:
            return "REPLICA", replica["estoque"]

        return "INDISPONIVEL", None


def main():
    print("=== CENTRAL DE PEDIDOS ===")
    print("Limite simultaneo:", MAXIMO_SIMULTANEO)
    print("Estoque inicial:", principal["estoque"])

    numeros_pedidos = [101, 102, 103]
    trabalhadores = [
        threading.Thread(target=processar_pedido, args=(numero,))
        for numero in numeros_pedidos
    ]

    # Inicia todas as threads antes de aguardar a conclusao de cada uma.
    for trabalhador in trabalhadores:
        trabalhador.start()

    for trabalhador in trabalhadores:
        trabalhador.join()

    print("Pedidos confirmados:", sorted(pedidos_confirmados))
    print("Estoque principal:", principal["estoque"])
    print("Replica antes:", replica["estoque"])

    # Atualiza a replica somente depois do processamento dos pedidos.
    sincronizar()
    print("Replica depois:", replica["estoque"])

    # Simula a falha do servidor principal e testa a consulta de contingencia.
    principal["online"] = False
    nome_servidor, estoque = consultar_estoque()
    print("Consulta apos falha:", (nome_servidor, estoque))


if __name__ == "__main__":
    main()
