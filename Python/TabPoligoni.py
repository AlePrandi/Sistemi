import turtle #modulo built-in

finestra = turtle.Screen() #creazione finestra
tarta = turtle.Turtle() #creazione tartaruga
nlati = 3

tarta.speed(5)
tarta.penup()
tarta.left(90)
tarta.forward(110)
tarta.right(90)
tarta.backward(275)
tarta.pendown()

for j in range(0, 3):
    for k in range(0, 3):

        for i in range(0, nlati):
            if nlati <= 5:
                tarta.forward(100)
            else:
                tarta.forward(50)
            tarta.left(360/nlati)
        nlati += 1
        tarta.penup()
        tarta.forward(200)
        tarta.pendown()
    tarta.penup()    
    if nlati <= 8:
        tarta.back(575)
    else:
        tarta.back(600)
    tarta.right(90)
    if nlati <= 8:
        tarta.forward(150)
    else:
        tarta.forward(200)
    tarta.left(90)
    tarta.pendown()

finestra.mainloop() #gestione finestra