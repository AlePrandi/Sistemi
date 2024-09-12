import socket
import threading
import time

MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096
TEMPO = 30
listaClienti = []

class Client_handler(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection

    def run(self):
        global listaClienti
        while True:
            cliente = self.connection.recv(BUFFER_SIZE)
            if cliente not in listaClienti:
                listaClienti.append(cliente.decode())
                self.connection.sendall(str(len(listaClienti)).encode())
            else:
                self.connection.sendall("Error".encode())
            print(listaClienti)
            
class RemoveElement(threading.Thread):
    def __init__(self):
        super().__init__()
        
    def run(self):
        while True:
            time.sleep(TEMPO)
            listaClienti.pop(0) if len(listaClienti) > 0 else print("Lista vuota")

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    while True:
        timer = RemoveElement()
        timer.start()
        s.listen()
        connection, client_address = s.accept()  # bloccante
        print(f"Il client {client_address} si è connesso")
        thread = Client_handler(connection)
        thread.start()


if __name__ == '__main__':
    main()