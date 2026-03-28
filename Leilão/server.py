import threading
import socket
import random
import json

server_IP = "127.0.0.1"  # IP do servidor
port = 8080  # Porta de comunicação que será usada
addr = (server_IP, port)  # Endereço do servidor
formato = "utf-8"  # Formato de codificação e decodificação de textos

with open("itens.json", "r", encoding=formato) as lista_itens:
    # Abre o arquivo .json e lê seu conteúdo

    itens_leilao = json.load(lista_itens)
    # Carrega o conteúdo do arquivo em uma variável

itens = itens_leilao["itens"]  # Recebe um conteúdo específico do arquivo
item_leilao = random.sample(itens, 1)
# Seleciona um item aleatório da lista do arquivo .json para ser o item do leilão

valor = random.randint(1, 1000000)
# Recebe um número aleatório dentro dos números determinados para servir como valor do item do leilão
vencedor_atual = "Ninguém"  # Variável com o nome do vencedor atual

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Cria um socket TCP para o servidor (AF_INET Especifica que o socket usará endereços IPv4 (o formato de endereço como 127.0.0.1);
# SOCK_STREAM Indica que o socket usará o protocolo TCP, que garante entrega confiável de dados, ideal para aplicações como um leilão,
# onde a ordem e a integridade dos lances são cruciais.)

server.bind(addr)  # Vincula o socket ao endereço 127.0.0.1 (localhost) e porta 8080


def calcular_lance(nome, lance):  # Função para calcular o lance do cliente
    global valor, vencedor_atual  # Torna as variáveis globais
    if lance >= valor:  # IF para caso o lance seja maior do que o valor do item
        vencedor_atual = nome  # Torna o cliente o vencedor atual
        valor = lance  # Torna o lance do cliente o novo valor do item
        print(f"O cliente {vencedor_atual} deu o maior lance no valor de {valor}.\n")
        # Printa o lance do cliente

        resposta = {
            "status": "LANCE ACEITO",
            "item": item_leilao,
            "lance_atual": valor,
            "vencedor_atual": vencedor_atual,
        }
        # Resposta que será enviada ao cliente

        print(f"Vencedor atual:{vencedor_atual}.\nNovo preço do item:{valor}")
        # Printa o estado atual do leilão

    elif lance < valor:  # ELIF para caso o lance seja menor do que o valor do item
        print(f"O cliente {nome} fez um lance com valor insuficiente.\n")
        # Printa o lance do cliente

        resposta = {
            "status": "LANCE INSUFICIENTE",
            "item": item_leilao,
            "lance_atual": valor,
            "vencedor_atual": vencedor_atual,
        }
        # Resposta que será enviada ao cliente

        print(f"Vencedor atual:{vencedor_atual}.\nNovo preço do item:{valor}\n")
        # Printa o estado atual do leilão

    return resposta  # Retorna a resposta para onde a função foi chamada


def handle_clients(conn, addr):  # Função para gerenciar os clientes
    print(f"Um usuário se conectou pelo endereço {addr}\n")
    # Printa uma mensagem toda vez que um novo cliente se conecta

    nome = None  # Variável que receberá o nome do cliente
    lance = None  # Variável que receberá o lance do cliente

    try:
        while True:  # Loop para receber os dados do cliente
            dados = conn.recv(1024).decode(formato)
            # Recebe os dados enviados pelo cliente

            if not dados:  # Quebra o loop caso não haja dados
                break
            if dados.startswith("nome="):
                # Recebe e formata o nome do cliente para uma forma específica

                nome_sep = dados.split("=")
                # Cria uma lista com o dado recebido e separa seu conteúdo no '='

                nome = nome_sep[1]
                # Recebe somente o nome do cliente que está contido na lista

            elif dados.startswith("lance="):
                # Recebe e formata o lance do cliente para uma forma específica

                lance_sep = dados.split("=")
                # Cria uma lista com o dado recebido e separa seu conteúdo no '='

                lance = int(lance_sep[1])
                # Recebe somente o lance do cliente, que está contido na lista, e transforma-o em um valor inteiro

                resposta = calcular_lance(nome, lance)
                # Envia o lance e o nome do cliente para a variável de calcular o lance, e recebe o resultado
                conn.send(json.dumps(resposta).encode(formato))
                # Envia uma resposta ao cliente
    except:
        print(f"Cliente {addr} desconectou.\n")
        # Mensagem caso o cliente se desconecte
    finally:
        conn.close()  # Fecha a conexão com o cliente


def start():  # Função que inicia o leilão
    print(
        f"Início do Leilão.\nO item de hoje é um(a) {item_leilao} no valor de {valor}.\nAguardando Clientes.\n"
    )
    # Mensagem de boas vindas
    server.listen()  #'Escuta' caso haja algum cliente tentando se conectar
    try:
        while True:  # Loop para aceitar novos clientes
            conn, addr = server.accept()  # Aceita novos clientes
            thread = threading.Thread(target=handle_clients, args=(conn, addr))
            # Cria uma thread para cada cliente

            thread.start()  # Incia a thread
    except KeyboardInterrupt:  # Caso o servidor seja interrompido com CTRL+C
        print("\nEncerrando servidor...")  # Mensagem de encerramento do servidor
    finally:
        server.close()  # Fecha o serrvidor


if __name__ == "__main__":  # Inicia o servidor
    start()
