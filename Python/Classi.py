# in python non esistono gli attributi privati
# non si usa il get
# in python non si può fare l'overloading
class Quadrato:
    def __init__(self, lato):  # è il costruttore, è uguale per tutti
        self.lato = lato

    def calcolaArea(self):
        return self.lato**2
    
    def stampaLato(self):
        print(f"Il lato è {self.lato}")


def main():
    q = Quadrato(4)
    print(f"L'area del quadrato è {q.calcolaArea()}")
    print (q.lato)
    q.lato = 5

if __name__ == "__main__":
    main()
