import socket

SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFERSIZE = 4096
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    while True:
        messaggio = input("-> ")
        s.sendall(messaggio.encode())
        message = s.recv(BUFFERSIZE) #bloccante
        message = message.decode()
        if message != "Error":
            print(f"Attualmente sei in posizione {message} in coda")
        else:
            print("Errore persona già presente")
    s.close()


if __name__ == '__main__':
    main()