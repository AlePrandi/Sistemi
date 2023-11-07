import turtle
PIX = 100

def Nord(tarta):
    tarta.setheading(90)
    tarta.forward(PIX)
    
def Est(tarta):
    tarta.setheading(0)
    tarta.forward(PIX)
    
def Sud(tarta):
    tarta.setheading(270)
    tarta.forward(PIX)
    
def Ovest(tarta):
    tarta.setheading(180)
    tarta.forward(PIX)
    
def main():
    finestra = turtle.Screen()
    tarta = turtle.Turtle()
    dizionario = {"N": Nord, "E": Est, "S": Sud, "O": Ovest}
    while True:
        direz = input("Inserisci la direzione: ")
        if direz in dizionario:

            dizionario[direz](tarta)
        finestra.mainloop()
        exit

if __name__ == "__main__":
    main()
