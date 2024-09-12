import math

def isNarcisista(numero):
    # creo la lista con i numeri riconvertiti a int già elevati ^3 
    lista_num = [math.pow(int(c), 3) for c in str(numero)] 
    somma = sum(lista_num) # sommo gli elementi della lista
    if somma == numero: # confronto i due numeri
        print(f"Il numero '{numero}' è narcisista")

def main():
    for num in range(1, 1000): # ciclo per i numeri
        isNarcisista(num)

if __name__ == '__main__':
    main()