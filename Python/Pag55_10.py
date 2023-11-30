def main():
    lista = []
    voto = 1
    k = 0

    while True:
        voto = int(input("Inserisci un voto (-1 per interrompere): "))

        if (voto < 0) & k > 6:
            break

        lista.append(voto)
        k += 1

    print(f"Lista tranne primo e ultimo elemento: {lista[1:-1]}")
    lista[3] = 10
    print(f"I primi 3 voti sono: {lista[0:3]}")
