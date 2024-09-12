import math
num = int(input("Inserisci un numero positivo: "))
esp = int(math.log2(num))
lista = [2**i for i in range(0, esp + 1)]
print(f"Potenze di 2 da 0 a {num}: {lista}")