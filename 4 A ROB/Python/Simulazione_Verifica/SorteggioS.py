# il server TCP estrae un numero da 1 a 100
# si connettono almeno due client che provano ad indovinare
# il server può rispondere con "HAI VINTO", "TROPPO BASSO", "TROPPO ALTO" in base al numero scelto dal client
# vince solo un client e agli altri client viene comunicato "HAI PERSO"

import socket 
import random
import threading

MY_ADDRESS = ("127.0.0.1", 9090)
BUFFERSIZE = 4096
numero_server = random.randint(1, 100)
vincitore = False
lock = threading.Lock()

class RandomServer(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection

    def run(self):
        global vincitore
        while True:
            data = self.connection.recv(BUFFERSIZE)
            numero = int(data.decode())

            with lock:
                if not vincitore:
                    if numero < numero_server:
                        self.connection.sendall("TROPPO BASSO".encode())
                    elif numero > numero_server:
                        self.connection.sendall("TROPPO ALTO".encode())
                    else:
                        self.connection.sendall("HAI VINTO".encode())
                        vincitore = True
                        break
                else:
                    self.connection.sendall("HAI PERSO".encode())
                    break


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()

    while True:
        connection, client_address = s.accept()  # bloccante
        thread = RandomServer(connection)
        thread.start()

    s.close()

if __name__ == "__main__":
    main()