import turtle

def completa8bit(strbin):
    b = strbin[2:]
    l = len(b)
    return "0" * (8 - l) + b

def daAsciiaBin(stringa):
    lista_bin = []
    for char in stringa:
        valore_ascii = ord(char) # ord converte in ASCII
        if valore_ascii <= 255:
            valore_bin = bin(valore_ascii)
            lista_bin.append(completa8bit(valore_bin))
    return lista_bin

def disegnaCodice(lista_bin):
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()

    for valore_bin in lista_bin:
        for bit in valore_bin:
            if bit == '1':
                turtle.fillcolor('black')
            else:
                turtle.fillcolor('white')
            turtle.begin_fill()
            for _ in range(2):
                turtle.forward(4)
                turtle.right(90)
                turtle.forward(100)
                turtle.right(90)
            turtle.end_fill()
            turtle.forward(1)

    turtle.done()

def main():
    
    while True:
        stringa = input("Inserisci una stringa di 8 caratteri: ")
        if (len(stringa) <= 8):
            break

    val_bin = daAsciiaBin(stringa)
    print(val_bin)
    disegnaCodice(val_bin)
    
if __name__ == "__main__":
    main()
