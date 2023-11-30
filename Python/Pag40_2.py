def main():
    
    n = int(input("Inserisci un numero divisibile per 2 3 e 5: "))    

    if n  % 2 == 0:
        print("Il numero è divisibile per 2")
    elif n % 3 == 0:
        print("Il numero è divisibile per 3")
    elif n % 5 == 0:
        print("Il numero è divisibile per 5")
    else:
        print("Il numero non è divisibile per 2, 3 o 5")

if __name__ == '__main__':
    main()