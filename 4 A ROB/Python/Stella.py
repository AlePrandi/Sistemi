#DISEGNARE UNA STELLA A N PUNTE
import turtle
import math

n = int(input("inserisci il numero di punte: "))
finestra = turtle.Screen()
tarta = turtle.Turtle()
lato = 100

if n != 0 and n !=1:
    if(n%2)!=0:
        for i in range(0, n):
            tarta.forward(lato)
            tarta.left(720/n)
    else:
        for k in range(0, int(n/2)):
            tarta.forward(lato)
            tarta.left(720/n)
        tarta.penup()
        tarta.forward(lato/2)
        tarta.right(90)
        tarta.forward(((lato/3)/math.sqrt(2))/(n/8))  #formula per  trovale cateto del mezzo triangolo che forma punta della stella
        tarta.left(360/n + 90)
        tarta.pendown()
        for j in range(0, int(n/2)):
            tarta.forward(lato)
            tarta.left(720/n)
else:
    print("il numero di punte inserito non è valido")

finestra.mainloop()