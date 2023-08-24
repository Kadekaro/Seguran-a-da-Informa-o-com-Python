import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket Criado Com Sucesso!")
host = "localhost"
port = 5432
s.bind((host, port))
mensagem = "\nServidor: Oii Cliente, tudo certo por aqui, manda bala!"
while 1:
    dados, end = s.recvfrom(4096)
    if dados:
        print(f"Servidor enviando mensagem...")
        s.sendto(dados + (mensagem.encode()), end)
