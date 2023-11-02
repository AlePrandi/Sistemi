def main():
    Ip = input("Inserisci un indirizzo Ip: ")
    lista = Ip.split('.')
    lista = [int(elemento) for elemento in lista]
    lista_bin = lista
    lista_bin = ['{0:08b}'.format(elemento) for elemento in lista_bin]
    print(f"Lista in decimale: {lista}")
    print(f"Lista in binario: {lista_bin}")
    
if __name__ == "__main__":
    main()