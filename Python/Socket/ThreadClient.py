import threading
import socket
import time

SERVER_ADDRESS = ("127.0.0.1", 9000)
BUFFER_SIZE = 4096  # byte


class ThreadInvio(threading.Thread):
    def __init__(self, s):
        super().__init__()
        self.s = s
        self.running = True
        self.mandato = False

    def run(self):
        while self.running:
            stringa = input("->")
            self.s.sendto(stringa.encode(), SERVER_ADDRESS)
            print("Inviato")
            self.mandato = True

    def kill(self):
        self.running = False


class ThreadRicevi(threading.Thread):
    def __init__(self, s):
        super().__init__()
        self.s = s
        self.running = True

    def run(self):
        print("Ricezione attiva")
        while self.running:
            data, server_address = self.s.recvfrom(BUFFER_SIZE)
            print(f"Ricevuto {data.decode()} da {server_address}")
            if data.decode() == "EXIT":
                self.kill()

    def kill(self):
        self.running = False


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    invio = ThreadInvio(s)
    ricevi = ThreadRicevi(s)

    invio.start()
    while True:
        if invio.mandato:
            ricevi.start()
            invio.mandato = False
            time.sleep(0.02)

    invio.join()
    ricevi.join()


if __name__ == "__main__":
    main()
