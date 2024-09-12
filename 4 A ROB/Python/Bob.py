import turtle
import random
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y     

def main():
    finestra = turtle.Screen()
    tarta = turtle.Turtle()
    lung = 10
    percorso = {0: Punto(0, 0)}
    for tempo in range(1, 60):
        # simulare movimenti casuali
        #disegnare percorso con turtle
        #BONUS fare un controllo se è passato più volte in un punto
        scelta = random.randint(0,3)
        if scelta == 0: # verso nord
            percorso[tempo] = Punto(percorso[tempo - 1].x, percorso[tempo - 1].y - lung)
        if scelta == 1: # verso est
            percorso[tempo] = Punto(percorso[tempo - 1].x + lung, percorso[tempo - 1].y)
        if scelta == 2: # verso sud
            percorso[tempo] = Punto(percorso[tempo - 1].x, percorso[tempo - 1].y + lung)
        if scelta == 3: # verso ovest
            percorso[tempo] = Punto(percorso[tempo - 1].x - lung, percorso[tempo - 1].y)
        
        for pos in range(0,tempo):
            if percorso[pos].x == percorso[tempo].x and percorso[pos].y == percorso[tempo].y:
                print(f"Bob è già passato nel punto {percorso[pos].x},{percorso[tempo].y}")
    
        tarta.pendown()
        tarta.goto((percorso[tempo].x, percorso[tempo].y))

    #scrittura su file
    #COLONNE: minuto, x, y
    with open("percorso.csv", "w") as file:
        #ciclo sul dizionario
        for minuto in percorso:
            posX = percorso[minuto].x
            posY = percorso[minuto].y
            file.write(f"minuto: {minuto}, x: {posX}, y: {posY}\n")  
    
    finestra.mainloop()

if __name__ == "__main__":
    main()
