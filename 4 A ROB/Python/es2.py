def main():
    a = float(input("inserisci un numero: "))
    print(f"il tipo di a è {type(a)}")
    if a > 5:
        print(f"a è maggiore di 5")
    elif  (a <= 5) and (a >= 0):
        print(f"a è maggiore o uguale di 0 e minore di 5")
    else:
        print(f"a è minore o uguale di 5")


if __name__ == '__main__':
    main()