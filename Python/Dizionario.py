# dizionario: collezione di coppie chiave: valore
# il dizionario non ha indici, ma si indicizza
# per chiave
def main():
    dizionario = {"nome": "Mario", "cognome": "Rossi"}
    # lista = ["Mario", "Rossi"] <- scrittura analoga di dizionario
    print(dizionario["nome"])

    # aggiungo due elementi nuovi ai campi di dizionario
    dizionario["data di nascita"] = "01/01/1900"
    dizionario["età"] = 123

    # sovrascrivo l'elemento
    dizionario["nome"] = "Luca"
    print(dizionario)

    # ciclo sul dizionario
    # tipo 1
    for chiave in dizionario:
        print(f"{chiave} - valore: {dizionario[chiave]}")

    rubrica = {38249271: "Mario Rossi", 38241272: "Alice Verdi"}


if __name__ == "__main__":
    main()
