#client
import socket

SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFERSIZE = 4096

def codificaParola(mess,n, c):
    l_parole = []
    parola = mess
    for el in parola:
        l_parole.append((ord(el)**c) % n)

    return l_parole

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    s.sendall("request_chiave".encode())
    message = s.recv(BUFFERSIZE) #bloccante
    print(f"Ricevuto <{message.decode()}> dal server")
    n, c = message.decode().split('|')
    mess = input("Inserisci un messaggio: ")
    parola_cod = codificaParola(mess,n, c)
    s.sendall(parola_cod.encode())
    s.close()


if __name__ == '__main__':
    main()
