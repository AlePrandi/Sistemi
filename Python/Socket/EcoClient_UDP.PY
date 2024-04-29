import socket

SERVER_ADDRESS = ("127.0.0.1", 9000)
BUFFER_SIZE = 4096 #byte
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    stringa = input("->")
    s.sendto(stringa.encode(), SERVER_ADDRESS)
    data, server_address = s.recvfrom(BUFFER_SIZE)
    print(f"Ricevuto {data.decode()} da {server_address}")
    if stringa == "EXIT":
        break