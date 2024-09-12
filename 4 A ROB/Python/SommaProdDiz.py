def somma(a, b):
    return a + b #quando non fa niente si usa il pass
    
def prodotto(a, b):
    return a * b

def sottrazione(a, b):
    return a - b

def divisione(a, b):
    return a / b if b != 0 else 0

def main():
    # print(somma) somma è un oggetto, quindi funziona ma stampa l'indirizzo
    dizionario = {"+": somma, "*": prodotto, "-": sottrazione, "/": divisione}
    operazione = input("Inserisci l'operazione: ")
    a = float(input("Inserisci il primo numero: "))
    b = float(input("Inserisci il secondo numero: "))
    print(dizionario[operazione](a, b))
    
if __name__ == "__main__":
    main()