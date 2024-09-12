import socket 

SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFERSIZE = 4096 
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    print("Inserisci un numero da 1 a 100 \n")
    message = None
    while True:
        messaggio = input("-> ")
        s.sendall(messaggio.encode())
        message = s.recv(BUFFERSIZE) #bloccante
        message = message.decode()
        if message == "HAI VINTO" or message == "HAI PERSO":
            print(message)
            break
        else:
            print(message)
    s.close()
    

if __name__ == '__main__':
    main()