Ip = input("Inserisci un indirizzo Ip: ")
lista = Ip.split('.')
lista = [int(elemento) for elemento in lista]
lista_bin = lista
lista_bin = ['{0:08b}'.format(elemento) for elemento in lista_bin]
print(f"Lista in deciamale: {lista}")
print(f"Lista in binario: {lista_bin}")