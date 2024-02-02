import networkx as nx


def prettyPrint(matrice):
    for riga in matrice:
        print(" ".join(str(x) for x in riga))


"""def matr2diz(matrice):
    d = {}
    for riga in matrice:
            
    print(d)"""


def main():
    d = {0: [2, 3], 1: [2, 4], 2: [0, 1, 3], 3: [0, 2, 4], 4: [1, 3]}
    n = len(d)
    matrice = [[0] * n for _ in range(n)]

    # ciclo su dizionario con chiave e valore in parallelo
    for k, v in d.items():
        for h in v:
            matrice[k][h] = 1

    prettyPrint(matrice)
    # matr2diz(matrice)


# Create an empty directed graph
G = nx.DiGraph()

# Add nodes
G.add_nodes_from(range(5))

# Create an adjacency matrix
adj_matrix = matrice

# Set the graph's edge weights based on the adjacency matrix
for i in range(5):
    for j in range(5):
        if adj_matrix[i][j] == 1:
            G.add_edge(i, j, weight=1)

# Draw the graph
nx.draw(G, with_labels=True)
plt.show()

if __name__ == "__main__":
    main()


