def main():
    #usare if
    #chiedi 2 numeri e stampa una stringa con i num in oridine decrescente
    #funzione main
    n1 = float(input ("Inserisci il primo numero: "))
    n2 = float(input ("Inserisci il secondo numero: "))

    if n2 > n1:
        n1, n2 = n2, n1 #inverte i numeri

    print (f"numero maggiore {n1} numero minore {n2}")

if __name__ == "__main__":
    main()