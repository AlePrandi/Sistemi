import turtle
DIM = 10
    
def main():
    finestra = turtle.Screen()
    tarta = turtle.Turtle()
    tarta.penup()
    tarta.goto(-100, 50)
    tarta.pendown()
    tarta.speed(0)
    for _ in range(0,4):
        for _ in range(0,4):
            for _ in range(0,4):
                tarta.forward(DIM)
                tarta.left(90)
            tarta.forward(DIM)
        tarta.penup()
        tarta.backward(DIM * 4)
        tarta.right(90)
        tarta.forward(DIM)
        tarta.left(90)
        tarta.pendown()
    turtle.done()
    
if __name__ == '__main__':
    main()