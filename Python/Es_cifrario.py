'''
CIFRARIO DI VERNAM

Usiamo l'alfabeto italiano <- 21 lettere 

funzione .lower(char) per convertire in minuscolo

a = 0
b = 1
c = 2
d = 3
etc...

si memorizza con una lista o un dizionario

Nel cifrario di Vernam codifichiamo le stringhe tramite una chiave lunga almeno quanto il testo

il primo passo è tradurre i numeri in stringhe ciao -> 2 8 0 13 chiave -> 0 1 2 3 otteniamo la somma 2 9 2 15
solo che così può andare oltre alla z e quindi si fa % 21 
'''

class Testo():
    def __init__(self, stringa, chiave, cifrato):
        self.lettere = "abcdefghijklmnopqrstuvwxyz ?!"
        self.stringa = stringa.lower() 
        self.chiave = chiave.lower() 
        self.cifrato = cifrato #bool
        self.testo_chiaro = ""
        self.testo_criptato = ""
                
    def cifra_cod(self, lett2num, num2lett):
        if self.cifrato == False:
            for lettera_testo, lettera_chiave in zip(self.stringa, self.chiave):
                numero = (lett2num[lettera_testo] + lett2num[lettera_chiave]) % len(self.lettere)
                self.testo_criptato = self.testo_criptato + num2lett[numero]
            print(f"il testo '{self.testo_chiaro}' diventa '{self.testo_criptato}'.")
            self.cifrato = True
        else:
            print("la stringa è già cifrata")
    
    def decifra_cod(self, lett2num, num2lett):
        if self.cifrato == True:
            for lettera_testo, lettera_chiave in zip(self.testo_criptato, self.chiave):
                numero = (lett2num[lettera_testo] - lett2num[lettera_chiave]) % len(self.lettere)
                self.testo_chiaro = self.testo_chiaro + num2lett[numero]
            print(f"il testo '{self.testo_criptato}' è tornato '{self.testo_chiaro}'.")
            self.cifrato = False
        else:
            print("la stringa è già decifrata")
        
def main():
    lettere = "abcdefghijklmnopqrstuvwxyz ?!"
    lett2num = {}
    num2lett = {}
    for posizione, lettera in enumerate(lettere):
        num2lett[posizione] = lettera 
        lett2num[lettera] = posizione
        
    parola = input("inserisci una parola: ")
    chiave = "itisdelpozzoqwretrytuygihijdnvaioghqerbv"
    testo = Testo(parola, chiave , False)
    testo.cifra_cod(lett2num,num2lett)
    testo.decifra_cod(lett2num,num2lett)

if __name__ == "__main__":
    main()
