def main():
    n = int(input("Inserisci una cdr per la subnet(es. /24) senza /: "))
    lista = n * '1' + '0' * (32 - n)
    print(lista)
    group1 = int(lista[0:8], 2)
    group2 = int(lista[8:16], 2)
    group3 = int(lista[16:24], 2)
    group4 = int(lista[24:], 2)
    lista = [group1, group2, group3, group4]
    lista = [str(elemento) for elemento in lista]
    print('.'.join(lista))
    
if __name__ == '__main__':
    main()