'''
Diffie-Hellman permette di condividere la chiave privata degli algoritmi simmetrici
'''
import numpy as np
from sympy import prime

def main():
    N = prime(np.random.randint(500,600))
    g = np.random.randint(1, N)

    a = np.random.randint(1, N)
    A = (g**a) % N

    b = np.random.randint(1, N)
    B = (g**b) % N

    B_der = (B**a) % N
    A_der = (A**b) % N

    print(f"Numero che arriva ad Alice = {B_der}, Numero che arriva a Bob = {A_der}")
    
if __name__ == "__main__":
    main()
    