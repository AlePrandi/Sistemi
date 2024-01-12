#dato un numero n stampare una rombo di diagonale n a terminale
#       *
#      ***
#     *****
#      ***
#       *
def diagonal(n):
    for i in range(n):
        for j in range(n):
            print("")

def main():
    n = int(input("Inserisci un numero di lati: "))
    diagonal(n)
    
if __name__ == "__main__":
    main()