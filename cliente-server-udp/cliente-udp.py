import socket


# AF_INET ipv4

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("client Socket criado com sucesso")


host = "localhost"
port = 5432
message = "Hello Server!!!"


try:
    print('Cliente: ' + message)
    s.sendto(message.encode(), (host, port))

    data, server = s.recvfrom(4096)
    data = data.decode()
    print("clinte: " + data)
finally:
    print("Cliente: Fechando a conexao")
    s.close()
