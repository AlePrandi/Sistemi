class robot:
    def __init__(self,nome,massa,tipo):
        self.nome = nome
        if massa > 0:
            self.massa = massa
        else:
            self.massa = 1
        self.tipo = tipo
    
    def getNome(self):
        return self.nome
    
    def isPericolo(self):
        if(self.tipo == "umanoide") & (self.massa >= 100):
            return True
        else:
            return False
        
def main():
    robot1 = robot("UTF01", 122, "braccio")
    robot2 = robot("UTF02", 157, "umanoide")
    
    if robot1.isPericolo() == True:
        print(f"Il robot {robot1.getNome()} è pericoloso")
    else:
        print(f"Il robot {robot1.getNome()} non è pericoloso")
        
    if robot2.isPericolo() == True:
        print(f"Il robot {robot2.getNome()} è pericoloso")
    else:
        print(f"Il robot {robot2.getNome()} non è pericoloso")       
        
if __name__ == "__main__":
    main()