import socket

SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFERSIZE = 4096
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    s.sendall("ciao sciula".encode())
    message = s.recv(BUFFERSIZE) #bloccante
    print(f"Ricevuto <{message.decode()}> dal server")
    s.close()


if __name__ == '__main__':
    main()
