import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexao falhou")
        print("Error: {}".format(e))
        sys.exit()
    print("Socket criado com sucesso")

    host = input("Digite o host a ser conectado ___: ")
    port = input("Digite a porta a ser conectada___: ")
    try:
        s.connect((host, int(port)))
        print("Cliente TCP conectado com sucesso no host: " + host + ":" + port)
        s.shutdown(2)
    except socket.error as e:
        print("Error ao conectar com " + host + ":" + port)
        print("Error: {}".format(e))
        sys.exit()


if __name__ == "__main__":
    main()
