import networkx as nx
import matplotlib.pyplot as plt


def prettyPrint(matrice):
    for riga in matrice:
        print(" ".join(str(x) for x in riga))


def matr2diz(matrice):
    """
    diz = {int(chiave): [] for chiave in range(len(matrice))}
    for k, riga in enumerate(matrice):
        for j,num in enumerate(riga):
            if num != 0:
                diz[k].append(j)
    """
    diz = {
        i: [j for j, n in enumerate(matrice[i]) if n != 0] for i in range(len(matrice))
    }
    print(diz)


def disegnaGrafo(matrice):
    G = nx.Graph()

    for i in range(len(matrice)):
        G.add_node(i)

    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] == 1:
                G.add_edge(i, j)

    pos = nx.spring_layout(G)
    nx.draw(
        G,
        pos,
        with_labels=True,
        font_weight="bold",
        node_size=700,
        node_color="skyblue",
        font_color="black",
        font_size=8,
        edge_color="gray",
        linewidths=1,
        alpha=0.7,
    )

    plt.show()


def main():
    d = {0: [2, 3], 1: [2, 4], 2: [0, 1, 3], 3: [0, 2, 4], 4: [1, 3]}
    n = len(d)
    matrice = [[0] * n for _ in range(n)]

    for k, v in d.items():
        for h in v:
            matrice[k][h] = 1

    prettyPrint(matrice)
    matr2diz(matrice)
    disegnaGrafo(matrice)


if __name__ == "__main__":
    main()
