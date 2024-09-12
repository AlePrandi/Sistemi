import turtle


class Barcode:
    def __init__(self, stringa):
        self.stringa = stringa
        self.lista_bin = []

    def completa8bit(self, strbin):
        b = strbin[2:]
        l = len(b)
        return "0" * (8 - l) + b

    def daAsciiaBin(self):
        for char in self.stringa:
            valore_ascii = ord(char)  # ord converte in ASCII
            if valore_ascii <= 255:
                valore_bin = bin(valore_ascii)
                self.lista_bin.append(self.completa8bit(valore_bin))

    def disegnaCodice(self):
        finestra = turtle.Screen()
        tarta = turtle.Turtle()
        tarta.speed(0)
        tarta.hideturtle()
        tarta.penup()

        for valore_bin in self.lista_bin:
            for bit in valore_bin:
                if bit == "1":
                    tarta.fillcolor("black")
                else:
                    tarta.fillcolor("white")
                tarta.begin_fill()
                for _ in range(2):
                    tarta.forward(4)
                    tarta.right(90)
                    tarta.forward(100)
                    tarta.right(90)
                tarta.end_fill()
                tarta.forward(1)
        turtle.done()


def main():
    while True:
        stringa = input("Inserisci una stringa con meno di 8 caratteri: ")
        if len(stringa) <= 8:
            break

    CodiceBarre = Barcode(stringa)
    CodiceBarre.daAsciiaBin()
    CodiceBarre.disegnaCodice()


if __name__ == "__main__":
    main()
