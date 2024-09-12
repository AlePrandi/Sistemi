import socket
import threading


class Client_handler(threading.Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection

    def run(self):
        messaggio = self.connection.recv(BUFFER_SIZE)
        print(messaggio.decode())
        self.connection.sendall(messaggio)


MY_ADDRESS = ("192.168.1.112", 9090)
BUFFER_SIZE = 4096


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()
    while True:
        connection, client_address = s.accept()  # bloccante
        print(f"Il client {client_address} si è connesso")
        thread = Client_handler(connection)
        thread.start()


if __name__ == '__main__':
    main()
