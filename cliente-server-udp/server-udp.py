import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket criado com sucesso")


host = "localhost"
port = 5432


s.bind((host, port))

message = "Servidor: Hello Cliente How Are You?"


while 1:
    data, end = s.recvfrom(4096)
    print(data)
    print(end)
    if data:
        print("servidor enviando mensagem")
        s.sendto(data + (message.encode()), end)
