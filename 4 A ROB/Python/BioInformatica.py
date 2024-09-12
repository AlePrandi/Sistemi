def leggiFile(file):
    with open(file, "r") as file:
        righe = file.readlines()
    dizNucleo = {"A": 0, "C": 0, "T": 0, "G": 0}
    genoma = ""
    sequenza = "ATGTTTGTTTTT"

    for riga in righe:
        genoma = genoma + riga[:-1]

    for char in genoma:
        dizNucleo[char] += 1

    print(genoma)

    for i, _ in enumerate(genoma[:-len(sequenza)]):
        if genoma[i : i + len(sequenza)] == sequenza:
            print(f"Sequenza trovata in posizione: {i}")

    print(dizNucleo)

def main():
    nomefile = "covid-19_gen1.txt"
    leggiFile(nomefile)

if __name__ == "__main__":
    main()
