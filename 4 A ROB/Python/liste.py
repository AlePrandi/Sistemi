def print_list(l):
    for element in l:
        print(element, end=" ")
    print("\n")


def main():
    l = []
    num = 1
    while num > 0:
        num = int(input("inserisci un numero(num negativo per terminare): "))
        if num > 0:
            l.append(num)
    print_list(l)


if __name__ == "__main__":
    main()
