'''
utilizzare le code usando la push() e la pop(0) 
'''
class Coda():
    def __init__(self):
        self.lista = []
        
    def isEmpty(self):
        return self.lista == 0
        
    def Enqueue(self, valore):
        self.lista.append(valore)
    
    def Dequeue(self):
        if  not self.isEmpty():
           return self.lista.pop(0)
        else:
            return None
            
    def stampa(self):
        print(self.lista)
    
def main():
    coda = Coda()
    coda.Enqueue(10)
    coda.Enqueue(26)
    coda.stampa()
    coda.Dequeue()
    coda.stampa()
    
if __name__ == "__main__":
    main()