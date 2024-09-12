class Testo:
    def __init__(self, stringa):
        self.stringa = stringa
        
    def numero_char(self):
        return len(self.stringa)
    
    def lista_parole(self):
        return self.stringa.split(" ")
    
    def lung_parole(self):
        return [len(parola) for parola in self.lista_parole()]
    
    def ricerca(self, parola):
        return parola in self.lista_parole()
    
    def salva(self, nomeFile):
        with open(nomeFile, 'w') as f:
            f.write(self.stringa)
            
    def frequenza_parole(self):
        dizionario = {}
        for element in self.lista_parole():
            if element not in dizionario:
                dizionario[element] = 1
            elif element in dizionario:
                dizionario[element] += 1         
        return dizionario
    
def main():
    prova = "ciao come stai ?"
    t = Testo(prova)
    print(t.numero_char())
    print(t.lista_parole())
    print(t.lung_parole())
    print(t.ricerca("mario"))
    print(t.ricerca("ciao"))
    #t.salva("Correzione.txt")
    print(t.frequenza_parole())
    
    
if __name__ == "__main__":
    main()