class Quadrato:
    
    def __init__(self, lato):
        self.lato = lato

    def area(self):
        return self.lato ** 2

    def perimetro(self):
        return 4 * self.lato

    def isPuntoQuad(self, punto):
        x, y = punto

        if x > 0 and x < self.lato and y > 0 and y < self.lato:
            return True
        else:
            return False

def main():

    quadrato = Quadrato(5)

    print(f"Area del quadrato: {quadrato.area()}")
    print(f"Perimetro del quadrato: {quadrato.perimetro()}")

    punto = (4, 5)
    appartiene = quadrato.isPuntoQuad(punto)
    if appartiene:
        print(f"Il punto {punto} appartiene al quadrato.")
    else:
        print(f"Il punto {punto} non appartiene al quadrato.")

if __name__ == "__main__":
    main()