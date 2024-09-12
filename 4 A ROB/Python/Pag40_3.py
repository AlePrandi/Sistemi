def main():
    for i in range(0,3):
        segno = int(input("Inserisci segno: "))
        num1 = int(input("Inserisci numero: "))
        num2 = int(input("Inserisci numero: "))

        if segno == 0:#somma
            print(f"ris: {num1+num2}")            
        elif segno == 1:#sottrazione
            print(f"ris: {num1-num2}")  
        elif segno == 2:#moltiplicazione
            print(f"ris: {num1*num2}")  
        elif segno == 3:#divisione
            print(f"ris: {num1/num2}")
        else:
            print(f"il segno non è riconosciuto")


if __name__ == "__main__":
    main()