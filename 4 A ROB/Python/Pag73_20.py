def main():
    lista = [[i * k for i in range(1, 11)] for k in range(1, 11)]

    for k, tabellina in enumerate(lista):
        # tabellina è una lista
        # lista è una lista di liste
        # enumerate ritorna indice e elemento
        print(f"Tabellina del {k  + 1}: {tabellina}")
        
    file = open("TabellinaPita.txt", "w")
    for k, tabellina in enumerate(lista):
        file.write(f"Tabellina del {k  + 1}: {tabellina}\n")
    file.close()

if __name__ == "__main__":
    main()
