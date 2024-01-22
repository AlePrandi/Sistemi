'''
 dato un numero n stampare una rombo di diagonale n a terminale
       *
      ***
     *****
      ***
       *
'''
def main():
    lung = int(input("inserire un numero: "))
    while lung % 2 == 0 or lung < 0:
        lung = int(input("inserire un numero: "))

    for k in range(1, lung + 2, 2):
        print(" " * ((lung - k) // 2) + "*" * k) # // corrisponde al DIV 

    for k in range(lung - 2, 0, -2):
        print(" " * ((lung - k) // 2) + "*" * k)


if __name__ == "__main__":
    main()
