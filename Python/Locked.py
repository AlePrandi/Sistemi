import threading
import time
blocco = threading.Lock()
saldo = 1000

class Prelievo(threading.Thread):
    def __init__(self, percentuale):
        super().__init__()
        self.percentuale = percentuale
        
    def run(self):
        global saldo
        while True:
            cifra = self.percentuale * (saldo / 100)
            #Lock fa si che il primo thread che acquisisce la Lock sia l'unico a poter afire sulla parte
            #tra l'acquire e il release
            #mutex = mutuamente esclusivo 
            blocco.acquire() #acquisisce la lock
            saldo = saldo - cifra # esegue la zona critica 
            blocco.release() #rilascia la lock
            print(f"il saldo aggiornato è {saldo}")
            time.sleep(3)
            
def main():
    luca = Prelievo(5)
    mario = Prelievo(-2)
    luca.start()
    mario.start()
    
    #la sezione citica di un thread è la porzione di codice 
    #in cui il thread opera in scrittura sulla risorsa condivisa
    
    #avviene una race condition 
    
    #CONSEGNA !!
    #modificare in modo che il saldo sia un valore di un file, 
    #quindi ogni volta apro,modifico e chiudo il file
    #implementare meccanismo che impedisca al saldo di diventare negativo 
    #creare una lista di 10 thread ed eseguirli
    #implementare metodo kill 
    #il main thread lascia eseguire i thread per un minuto e poi fa la join
    
    
if __name__ == '__main__':
    main()