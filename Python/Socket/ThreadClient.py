import threading
import socket
import time

SERVER_ADDRESS = ("192.168.1.120", 9000)
BUFFER_SIZE = 4096  # byte
NICKNAME = "Prandi"

class ThreadInvio(threading.Thread):
    def __init__(self, s):
        super().__init__()
        self.s = s
        self.running = True
        self.mandato = False

    def run(self):
        while self.running:
            message = input("->")
            dest = input("inserire il nome del destinatario: ")
            packet = f"{message}|{NICKNAME}|{dest}"
            self.s.sendto(packet.encode(), SERVER_ADDRESS)
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
        while self.running:
            data, server_address = self.s.recvfrom(BUFFER_SIZE)
            print(f"\nRicevuto da {server_address}: {data.decode()}")
            if data.decode() == "EXIT":
                self.kill()

    def kill(self):
        self.running = False


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("192.168.1.132", 8000))
    invio = ThreadInvio(s)
    ricevi = ThreadRicevi(s)

    invio.start()
    while True:
        if invio.mandato:
            ricevi.start()
            time.sleep(5)

    invio.join()
    ricevi.join()


if __name__ == "__main__":
    main()
