class Quadrato:
    def __init__(self, lato):
        self.lato = lato

    def area(self):
        return self.lato ** 2

    def perimetro(self):
        return 4 * self.lato

    def isPuntoQuad(self, punto):
        x, y = punto
        semilato = self.lato / 2

        if -semilato <= x <= semilato and -semilato <= y <= semilato:
            return True
        else:
            return False

def main():

    quadrato = Quadrato(5)

    print("Area del quadrato:", quadrato.area())
    print("Perimetro del quadrato:", quadrato.perimetro())

    punto = (1, 2)
    appartiene = quadrato.isPuntoQuad(punto)
    if appartiene:
        print(f"Il punto {punto} appartiene al quadrato.")
    else:
        print(f"Il punto {punto} non appartiene al quadrato.")
