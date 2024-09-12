import turtle
import socket

MY_ADDRESS = ("127.0.0.1", 9000)  # identifica il processo
BUFFER_SIZE = 4096  # byte


def avanti(tarta):
    pass


def ndaré(tarta):
    pass


def destra(tarta):
    pass


def snistra(tarta):
    pass


def main():
    tarta = turtle.Turtle()
    screen = turtle.Screen()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(MY_ADDRESS)
    cumand  = {"W ": avanti(tarta), "S": ndaré(tarta), "A": snistra(tarta), "D": destra(tarta)}
    while True:
        data, sender_address = s.recvfrom(BUFFER_SIZE)
        stringa = data.decode()
        print(f"Chestì {sender_address} la mandà su sì: {stringa}")
        cumand[stringa]
        if stringa == "EXIT":
            break


if __name__ == '__main__':
    main()
