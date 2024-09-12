import math


class Node():
    def __init__(self, valore):
        self.valore = valore
        self.sinistro = None
        self.destro = None

    def inserisci(self, valore):
        if self.valore is not None:
            if self.valore > valore:
                if self.sinistro == None:
                    self.sinistro = Node(valore)
                else:
                    self.sinistro.inserisci(valore)

            elif self.valore < valore:
                if self.destro == None:
                    self.destro = Node(valore)
                else:
                    self.destro.inserisci(valore)

        else:
            self.valore = valore

    def print_tree(self):
        print(self.valore)

        if self.sinistro != None:
            self.sinistro.print_tree()

        if self.destro != None:
            self.destro.print_tree()

    def cercaVal(self, valore):
        if self.valore is not None:
            if valore == self.valore:
                return True
            elif valore < self.valore:
                if self.sinistro != None:
                    return self.sinistro.cercaVal(valore)

            elif valore > self.valore:
                if self.destro != None:
                    return self.destro.cercaVal(valore)

            else:
                return False
        else:
            return False

    def contaNodi(self, contNodi):
        contNodi += 1
        if self.sinistro is not None:
            contNodi = self.sinistro.contaNodi(contNodi)
        if self.destro is not None:
            contNodi = self.destro.contaNodi(contNodi)

        return contNodi

    def altezza(self, altDx, altSx):
        if self.sinistro is not None:
            altSx = self.sinistro.altezza(altDx, altSx + 1)
        if self.destro is not None:
            altDx = self.destro.altezza(altDx + 1, altSx)

        return max(altDx, altSx)

    def isBilanciato(self):
        return self.altezza(0, 0) == int(math.log2(self.contaNodi(0)))


def alberoBil(lista, n):
    mid = len(lista)//2
    n.inserisci(lista[mid])
    if mid != 0:
        listaSx = lista[0: mid]
        listaDx = lista[mid+1:]
        if len(listaSx) > 0:
            alberoBil(listaSx, n)
        if len(listaDx) > 0:
            alberoBil(listaDx, n)
    else:
        return None


def main():
    n = Node(4)
    n.inserisci(1)
    n.inserisci(2)
    n.inserisci(3)
    n.inserisci(5)
    n.inserisci(6)
    n.inserisci(7)
    n.print_tree()
    """
    if (n.cercaVal(7)):
        print("Trovato")
    else:
        print("Non trovato")

    if (n.cercaVal(3)):
        print("Trovato")
    else:
        print("Non trovato")

    n1 = Node(None)
    lista = [5, 6, 2, 20, 28, 16]
    lista.sort()
    alberoBil(lista, n1)
    n1.print_tree()
    """

    print("Numero nodi: " + str(n.contaNodi(0)))
    print("Altezza dell'albero: " + str(n.altezza(0, 0)))
    if n.isBilanciato() == True:
        print("è bilanciato")
    else:
        print("non è bilanciato")


if __name__ == "__main__":
    main()
