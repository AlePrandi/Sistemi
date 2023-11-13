def main():
    rubrica = {}
    fp = open("Rubrica.csv", "r")
    righe = fp.readlines()

    for riga in righe:
        campi = riga.split(", ")  # strip toglie \n
        nome = campi[0]
        numero = int(campi[1].replace("\n", ""))
        rubrica[nome] = numero
    #for chiave in rubrica:
    #   print(f"{chiave}: {rubrica[chiave]}")
    fp.close()
    
    scelta = int(input("Inserisci il tipo di ricerca che vuoi fare(1 per nome, 2 per numero): "))
    
    if scelta == 1:
        nome = input("Inserisci il nome da cercare: ")
        if nome in rubrica:
            print(f"il numero di {nome} è {rubrica[nome]}")
        else:
            print(f"non hai un contatto con questo nome")
            
    if scelta == 2:
        numero = int(input("Inserisci il numero da cercare: "))
        for chiave in rubrica:
            if numero == rubrica[chiave]:
                print(f"il numero {numero} appartiene a {chiave}")

if __name__ == "__main__":
    main()
