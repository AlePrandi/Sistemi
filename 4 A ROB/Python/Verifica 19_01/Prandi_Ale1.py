class Testo:
    def __init__(self, testo):
        self.testo = testo
        self.lista = []
        
    def lunghezza(self):
        print(f"Lunghezza del Testo: {len(self.testo)}") # uso il len per la lunghezza della stringa
        
    def lista_parola(self):
        self.lista = self.testo.split(" ") # creo una lista con elementi splittati 
        print(self.lista) # stampo gli elementi
        
    def lung_element_lista(self):
        # faccio un len degli elementi all'interno della lista
        lunghezza = [len(element) for element in self.lista] 
        print(lunghezza)
        
    def cerca_parola(self, parola):
        for i, _ in enumerate(self.testo[:-len(parola) + 1]):
            if self.testo[i : i + len(parola)] == parola:
                return True
            else:
                return False
            
    def salva_file(self, nomeFile):
        with open(nomeFile, 'w') as f:
            f.write(self.testo)
            
    def frequenza_parole(self):
        dizionario = {}
        for element in self.lista:
            if element not in dizionario:
                dizionario[element] = 1
            elif element in dizionario:
                dizionario[element] += 1         
        print(dizionario)


def main():
    testo = Testo("ciao come stai")
    testo.lunghezza()
    testo.lista_parola()
    testo.lung_element_lista()
    parola = "ciao"
    if(testo.cerca_parola(parola)):
        print(f"parola '{parola}' trovata nel testo")
    else:
        print(f"parola '{parola}' non presente nel testo")
        
    testo.salva_file("Prandi_Ale1.txt")    
    testo.frequenza_parole()
    
if __name__ == "__main__":
    main()