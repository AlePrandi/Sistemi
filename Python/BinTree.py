class Node:
    def __init__(self, valore):
        self.valore = valore
        self.sinistro = None
        self.destro = None

    def inserisci(self, valore):
        if self.valore != valore:
            if self.valore is not None:
                if valore < self.valore:
                    if self.sinistro is None:
                        self.sinistro = Node(valore)
                    else:
                        self.sinistro.inserisci(valore)
                else:
                    if self.destro is None:
                        self.destro = Node(valore)
                    else:
                        self.destro.inserisci(valore)
            else:
                self.valore = valore
        else:
            print("Non possono esserci valori uguali")

    def print_tree(self):
        if self.valore is not None:
            print(self.valore)
            if self.sinistro is not None:
                self.sinistro.print_tree()
            if self.destro is not None:
                self.destro.print_tree()

    def search_val(self, val):
        if self.valore is not None:
            if val == self.valore:
                return True
            elif val < self.valore and self.sinistro is not None:
                return self.sinistro.search_val(val)
            elif val > self.valore and self.destro is not None:
                return self.destro.search_val(val)
            else:
                return False
        else:
            return False

    def altezza(self):
        if self.valore is None:
            return 0
        else:
            if self.sinistro is not None:
                altezza_sinistro = self.sinistro.altezza()
            else:
                altezza_sinistro = 0
            if self.destro is not None:
                altezza_destro = self.destro.altezza()
            else:
                altezza_destro = 0
            return max(altezza_sinistro, altezza_destro) + 1

    def isBilanciato(self):
        if self.valore is None:
            return True
        else:
            if self.sinistro is not None:
                altezza_sinistro = self.sinistro.altezza()
            else:
                altezza_sinistro = 0
            if self.destro is not None:
                altezza_destro = self.destro.altezza()
            else:
                altezza_destro = 0
            diff_altezze = abs(altezza_sinistro - altezza_destro)
            
            if diff_altezze <= 1:
                if self.sinistro is not None:
                    sinistro_bilanciato = self.sinistro.isBilanciato()
                else:
                    sinistro_bilanciato = True
                if self.destro is not None:
                    destro_bilanciato = self.destro.isBilanciato()
                else:
                    destro_bilanciato = True
                if sinistro_bilanciato and destro_bilanciato:
                    return True
            return False


def AlberoBil(lista, n):
    if not lista:
        return None

    mid = len(lista) // 2
    if mid != 0:
        n.inserisci(lista[mid])
        listaSx = lista[0:mid]
        listaDx = lista[mid + 1 :]
        if len(listaSx) > 0:
            AlberoBil(listaSx, n)
        if len(listaDx) > 0:
            AlberoBil(listaDx, n)
    else:
        return None


def main():
    n1 = Node(None)
    lista = [1, 7, 5, 3, 9, 2, 6, 18, 21]
    lista.sort()
    AlberoBil(lista, n1)
    n1.print_tree()
    if n1.isBilanciato():
        print("L'albero è bilanciato.")
    else:
        print("L'albero non è bilanciato.")


if __name__ == "__main__":
    main()
