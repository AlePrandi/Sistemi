'''
RSA 

Algoritmo di crittografia più utilizzato 
RSA factoring challenge
'''
import math
from sympy import prime
from numpy import random
from random import randint


def mcm(a, b):
    return (a*b)/math.gcd(a, b)


def codificaNum(n, c):
    while 1:
        a = int(input("inserire un numero: "))
        if a < n and a >= 0:
            break

    return  (a**c) % n


def decodificaNum(b, d, n):
    return (b**d) % n

def codificaParola(n, c):
    l_parole = []
    parola = input("inserire una frase: ")
    for el in parola:
        l_parole.append((ord(el)**c) % n)

    return l_parole


def decodificaParola(l_parole, d, n):
    l_lett = []
    for el in l_parole:
        l_lett.append(chr((el**d) % n))

    return "".join(l_lett)

def main():
    # p e q numeri primi
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

    # FASE CODIFICA NUMERI

    #cod = codificaNum(n, c)
    #print(cod)
    #dec = decodificaNum(cod, d, n)
    #print(dec)
    
    # FASE CODIFICA PAROLE
    parola_cod = codificaParola(n,c)
    print(parola_cod)
    parola_decod = decodificaParola(parola_cod,d,n)
    print(parola_decod)

if __name__ == "__main__":
    main()
