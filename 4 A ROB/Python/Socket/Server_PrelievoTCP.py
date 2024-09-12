import socket
import threading
import time
MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096


class Client_handler(threading.Thread):
    def _init_(self, connection, file):
        super()._init_()
        self.connection = connection
        self.file = file
        self.running = True

    def run(self):
        while self.running:
            message = self.connection.recv(BUFFER_SIZE)  # bloccante
            if message.decode() != "0":
                perc = float(message.decode())
                with open(self.file, 'r') as f:
                    saldo = float(f.readline())
                    if saldo > 0:
                        cifra = perc * (saldo / 100)
                        time.sleep(1)
                        saldo = saldo - cifra
                        with open(self.file, 'w') as f:
                            f.write(str(saldo))
                        print(f"il saldo aggiornato e': {saldo}")
                        time.sleep(2)
                        string = str(saldo)
                    else:
                        print(f"il saldo è in negativo")
                        self.running = False
                        string = "negativo"
                self.connection.sendall(string.encode())
            else:
                self.connection.sendall("chiusura in corso".encode())
                self.kill()
                self.connection.close()

    def kill(self):
        self.running = False


def main():
    nomeFile = "prelievo.csv"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()
    while True:
        connection, client_address = s.accept()  # bloccante
        print(f"il client {client_address} si è connesso")
        thread = Client_handler(connection, nomeFile)
        thread.start()
    s.close()


if __name__ == '__main__':
    main()
