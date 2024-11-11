#server
import socket
import math
from sympy import prime
from numpy import random
from random import randint

MY_ADDRESS = ("0.0.0.0", 9000) 
BUFFER_SIZE = 4096 

def mcm(a, b):
    return (a*b)/math.gcd(a, b)

def decodificaParola(l_parole, d, n):
    l_lett = []
    for el in l_parole:
        l_lett.append(chr((el**d) % n))

    return "".join(l_lett)

def main():
    p = prime(randint(1, 20))
    q = prime(randint(1, 20))
    n = p * q
    c = None
    m = int(mcm(p-1, q-1))
    d = None

    for i in range(2, m):
        if (math.gcd(i, m) == 1):
            c = i
            break

    for a in range(0, m):
        if ((c * a) % m) == 1:
            d = a
            break

    print(f"chiavi pubbliche: n = {n}   c = {c}")

    print(f"chiavi private: p = {p}   q = {q}   m = {m}     d = {d}")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(MY_ADDRESS)
    s.listen()
    while True:
        connection, client_address = s.accept()  # bloccante
        print(f"Il client {client_address} si è connesso")
        messaggio = connection.recv(BUFFER_SIZE)
        if messaggio.decode() == "request_chiave":
            pacchetto = f"{n}|{c}"
            connection.sendall(pacchetto)
        else:
            parola = messaggio.decode()
            parola_dec = decodificaParola(parola, d, n)
            print(parola_dec)
        
       

if __name__ == "__main__":
    main()