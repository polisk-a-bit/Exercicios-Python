import threading
import socket
import json

IP = "127.0.0.1"  # IP do cliente
port = 8080  # Porta de comunicação que será usada
addr = (IP, port)  # Endereço do cliente para conectar com o servidor
formato = "utf-8"  # Formato de codificação e decodificação de textos

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Cria um socket TCP para o cliente (AF_INET Especifica que o socket usará endereços IPv4 (o formato de endereço como 127.0.0.1);
# SOCK_STREAM Indica que o socket usará o protocolo TCP, que garante entrega confiável de dados, ideal para aplicações como um leilão,
# onde a ordem e a integridade dos lances são cruciais.)

client.connect(addr)  # Estabelece uma conexão com o servidor no endereço 127.0.0.1:8080


def dados():  # Funçõo para coleta e tratamento de dados
    nome = input("Digite seu nome: ")  # Recebe o nome do cliente
    client.send(("nome=" + nome).encode(formato))  # Envia o nome do cliente ao servidor
    while True:  # Loop para múltiplos lances do cliente
        lance = input("Digite seu lance (ou 'sair' para encerrar): ")
        # Recebe o lance do cliente

        if lance.lower() == "sair":
            # Quebra o loop caso o cliente queira para de dar lances
            break
        try:
            int(lance)  # Transforma a variável lance em um valor inteiro
            client.send(("lance=" + lance).encode(formato))  # Envia o lance ao servidor

            resposta = json.loads(client.recv(1024).decode("utf-8"))
            # Recebe a resposta do servidor quanto ao lance feito

            print(
                f"\nStatus: {resposta['status']},\nItem: {resposta['item']},\nLance atual: {resposta['lance_atual']},\nVencedor: {resposta['vencedor_atual']}\n"
            )
            # Printa a resposta do servidor

        except ValueError:
            # Tratamento de erros caso o valor do lance não seja um número aceitável (ou não seja um número)

            print("Por favor, digite um número válido.\n")
            # Printa uma mensagem caso o erro acima ocorra


def inicio():  # Função para a criação de uma thread
    thread1 = threading.Thread(target=dados)
    # Cria uma thread para o cliente e a direciona para a função de tratamento de dados

    thread1.start()  # Inicia a thread acima


if __name__ == "__main__":  # Inicia a funcão incial
    inicio()
