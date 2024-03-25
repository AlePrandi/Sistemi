import pygame
from pygame.locals import *


def calc_pav():
    mat = []
    with open("percorso.csv", "r") as f:
        for riga in f.readlines():
            riga = riga.split(",")
            mat.append([int(c) for c in riga])
    return mat


def main():

    lato_x = 100
    lato_y = 100

    pavimento = calc_pav()
    n_y = len(pavimento)
    n_x = len(pavimento[0])
    matrice = [[-1 for _ in range(n_x)] for _ in range(n_y)]
    k = 1

    pygame.init()
    screen = pygame.display.set_mode((n_x * lato_x, n_y * lato_y))
    muro = pygame.image.load("./Muro.png")
    strada = pygame.image.load("./Pavimento.png")
    robot = pygame.image.load("./robot.png")
    font = pygame.font.Font(None, 36)

    for riga in pavimento:
        for casella in riga:
            surf1 = pygame.Surface((lato_x, lato_y))
            text = font.render(f"{k}", True, (0, 0, 0))
            if casella == 1:
                surf1.blit(muro, (0, 0))
                screen.blit(surf1, (lato_x - 100, lato_y - 100))
            else:
                surf1.blit(strada, (0, 0))
                text_pos = text.get_rect(center=(lato_x - 50, lato_y - 50))
                screen.blit(surf1, (lato_x - 100, lato_y - 100))
                screen.blit(text, text_pos)
                k += 1

            pygame.display.flip()
            lato_x += 100

        lato_x = 100
        lato_y += 100
        screen.blit(robot, (10, 10))

    diz = {}
    cont = 0
    for indice_riga, riga in enumerate(pavimento):
        for indice_colonne, casella in enumerate(riga):  # trova celle libere
            if casella == 0:
                cont = cont + 1
                matrice[indice_riga][indice_colonne] = cont
    print(matrice)

    diz = {}
    for indice_riga, riga in enumerate(matrice):
        for indice_colonna, casella in enumerate(riga):
            if casella != -1:
                adiacenti = []
                if (
                    indice_colonna + 1 < len(riga)
                    and matrice[indice_riga][indice_colonna + 1] != -1
                ):  # destra
                    adiacenti.append(matrice[indice_riga][indice_colonna + 1])
                if (
                    indice_colonna - 1 >= 0
                    and matrice[indice_riga][indice_colonna - 1] != -1
                ):  # sinistra
                    adiacenti.append(matrice[indice_riga][indice_colonna - 1])
                if (
                    indice_riga - 1 >= 0
                    and matrice[indice_riga - 1][indice_colonna] != -1
                ):  # sopra
                    adiacenti.append(matrice[indice_riga - 1][indice_colonna])
                if (
                    indice_riga + 1 < len(matrice)
                    and matrice[indice_riga + 1][indice_colonna] != -1
                ):  # sotto
                    adiacenti.append(matrice[indice_riga + 1][indice_colonna])
                diz[casella] = adiacenti

    print("dizionario caselle percorribili")
    print(diz)

    done = False
    while not done:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                done = True
    pygame.quit()


if __name__ == "__main__":
    main()
