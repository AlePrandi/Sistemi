import sys
import heapq


def calc_pav():
    mat = []
    with open("mappa.csv", "r") as f:
        for riga in f.readlines():
            riga = riga.split(",")
            mat.append([int(c) for c in riga])
    return mat


def scelta_nodo(nonVis, label):
    min_label = sys.maxsize
    min_nodo = None
    for nodo in nonVis:
        label_nodo = label[nodo]
        if label_nodo < min_label:
            min_label = label_nodo
            min_nodo = nodo

    return min_nodo


def dijkstra(sorgente, matrice):
    n_nodi = len(matrice)
    nonVis = set([i for i in range(0, n_nodi)])
    label = {i: sys.maxsize for i in range(0, n_nodi)}
    label[sorgente] = 0
    predecessore = [] 
    while len(nonVis) > 0:
        nodo_corrente = scelta_nodo(nonVis, label)
        nonVis.remove(nodo_corrente)
        for nodoVicino, peso in enumerate(matrice[nodo_corrente]):
            if peso > 0:
                nuovaLabel = label[nodo_corrente] + peso
                if nuovaLabel < label[nodoVicino]:
                    predecessore.append(nodo_corrente)
                    label[nodoVicino] = nuovaLabel
    return label,predecessore
 
 
def main():
    '''pavimento = calc_pav()
    n_y = len(pavimento)
    n_x = len(pavimento[0])
    matrice = [[-1 for _ in range(n_x)] for _ in range(n_y)]

    diz = {}
    cont = 0
    for indice_riga, riga in enumerate(pavimento):
        for indice_colonne, casella in enumerate(riga):  # trova celle libere
            if casella == 0:
                cont = cont + 1
                matrice[indice_riga][indice_colonne] = cont

    for indice_riga, riga in enumerate(matrice):
        for indice_colonna, casella in enumerate(riga):
            if casella != -1:
                adiacenti = []
                if (indice_colonna + 1 < len(riga) and matrice[indice_riga][indice_colonna + 1] != -1):  # destra
                    adiacenti.append((indice_riga, indice_colonna + 1))
                if (indice_colonna - 1 >= 0 and matrice[indice_riga][indice_colonna - 1] != -1):  # sinistra
                    adiacenti.append((indice_riga, indice_colonna - 1))
                if (indice_riga - 1 >= 0 and matrice[indice_riga - 1][indice_colonna] != -1):  # sopra
                    adiacenti.append((indice_riga - 1, indice_colonna))
                if (indice_riga + 1 < len(matrice) and matrice[indice_riga + 1][indice_colonna] != -1):  # sotto
                    adiacenti.append((indice_riga + 1, indice_colonna))
                diz[(indice_riga, indice_colonna)] = adiacenti
'''
    part = 0
    mat = [[0, 4, 0], [4, 0, 3], [0, 3, 0]]
    ris, prede = dijkstra(part, mat)
    print("Distanze minime da", part, ":")
    print(ris)
    print("Percorso: ")
    print(prede)


if __name__ == "__main__":
    main()
