def push(pila, elemento):
    pila.append(elemento)


def pop(pila):
    if len(pila) == 0:
        x = None
    else:
        x = pila.pop()
    return x


def main():
    """
    pila = [1,2,3,4]
    pila.append(5) #corrisponde al push in C
    print (pila)
    x = pila.pop() #corrisponde al pop
    print (x)
    print (pila)
    x = pop(pila)
    """
    stringa = "{1 + [2 + 3] * 5}"
    dizionario = {"{": "}", "[": "]", "(": ")"}
    par_ap = ["{", "[", "("]
    par_ch = ["}", "]", ")"]
    pila = []
    pos = None
    errore = False
    for k, c in enumerate(stringa):
        if c in par_ap:
            push(pila, c)
        if c in par_ch:
            parentesi = pop(pila)
            if parentesi != None:
                if dizionario[parentesi] != c:
                    pos = k
                    errore = True
                    break
            else:
                pos = k
                errore = True
    if errore:
        print(f"Errore in posizione {pos} !!")
    else:
        print("Corretto!!")


if __name__ == "__main__":
    main()
