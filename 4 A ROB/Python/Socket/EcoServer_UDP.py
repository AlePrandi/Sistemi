import socket

#lanciare sempre prima il Server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MY_ADDRESS = ("127.0.0.1", 9000)#identifica il processo
BUFFER_SIZE = 4096 #byte
s.bind(MY_ADDRESS)

while True:
    data, sender_address = s.recvfrom(BUFFER_SIZE)
    print(f"Ricevuto {data.decode()} da {sender_address}")
    s.sendto(data, sender_address)
    if data.decode() == "EXIT":
        break