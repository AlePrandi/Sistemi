import turtle

def comandi(l):
   finestra = turtle.Screen()
   tarta = turtle.Turtle()
   for element in l:
      if element == "R":
         tarta.right(90)
      elif element == "L":
         tarta.left(90)
      elif element == "F":
         tarta.forward(100)
      else:
         print("Comando non valido \n")


def main():
  com = []
  possibl = ["F", "L", "R"]
  while com in possibl:
      lett = input("inserisci una lettera( F = avanti, L = sinsitra, R =destra): ")
      if com in possibl:
        lett.append[com]
  comandi(com)

if __name__ == "__main__":
   main()
