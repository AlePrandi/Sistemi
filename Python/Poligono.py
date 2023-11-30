import turtle #modulo built-in

finestra = turtle.Screen() #creazione finestra
tarta = turtle.Turtle() #creazione tartaruga
nlati = int( input("Inserisci un numero di lati per il poligono: "))

tarta.speed(5)

tarta.begin_fill()
for i in range(0, nlati):
    tarta.color('red')
    tarta.forward(100)
    tarta.left(360/nlati)
tarta.end_fill()

finestra.mainloop() #gestione finestra