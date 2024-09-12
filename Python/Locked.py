import threading
import time

#crea un oggetto di tipo Lock, è un blocco
blocco = threading.Lock()

class Prelievo(threading.Thread):
    def __init__(self, file, percentuale):
        super().__init__()
        self.file = file
        self.percentuale = percentuale
        self.running = True

    def run(self):
        while self.running:
            with open(self.file, "r") as file:
                saldoStr = file.readline()
            saldo = float(saldoStr)
            if saldo > 0:
                cifra = self.percentuale * saldo / 100
                time.sleep(1) 
                saldo -= cifra
                blocco.acquire()
                with open(self.file, "w") as file:
                    file.write(str(saldo))
                blocco.release() 
                print(f"Il saldo aggiornato è: {saldo}")
                time.sleep(1)
            else:
                print("saldo in negativo")
                self.running = False
            
    def kill(self):
        self.running = False

def main():
    file = "saldo.txt"
    listaPrelievi = [5, -6]
    lista_thread = [Prelievo(file, n) for n in listaPrelievi]
    for t in lista_thread:
        t.start()
    time.sleep(60)
    for t in lista_thread:
        t.kill()
    for t in lista_thread:
        t.join()

if __name__ == "__main__":
    main()