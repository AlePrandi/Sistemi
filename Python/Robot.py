import pygame

def draw_map(screen, mappa, lato_quad, pavimento, muro, font, mat):
    k = 0
    diz = {}
    for y, riga in enumerate(mappa):
        for x, cell in enumerate(riga):
            if cell == 1:
                screen.blit(muro, (x * lato_quad, y * lato_quad))
            else:
                screen.blit(pavimento, (x * lato_quad, y * lato_quad))
                testo = font.render(f"{k}", True, (255, 255, 255))
                text_rect = testo.get_rect(
                    center=(x * lato_quad + lato_quad - 15, y * lato_quad + 15)
                )
                screen.blit(testo, text_rect)
                mat[x][y] = k
                k += 1

    for y, riga in enumerate(mappa):
        for x, cell in enumerate(riga):
            if cell == 0:
                if y >= 0 and y <= len(mappa[0]) and x >= 0 and x <= len(mappa):
                    if mat[x + 1][y] != -1:
                        diz[mat[x][y]] = mat[x][y]
                    if mat[x - 1][y] != -1:
                        diz[mat[x][y]] = mat[x][y]
                    if mat[x][y + 1] != -1:
                        diz[mat[x][y]] = mat[x][y]
                    if mat[x][y - 1] != -1:
                        diz[mat[x][y]] = mat[x][y]


def main():
    pygame.init()
    lato_quad = 100
    mappa = []

    pavimento = pygame.image.load("Pavimento.png")
    pavimento = pygame.transform.scale(pavimento, (lato_quad, lato_quad))
    muro = pygame.image.load("Muro.png")
    muro = pygame.transform.scale(muro, (lato_quad, lato_quad))

    with open("mappa.csv", "r") as f:
        for riga in f.readlines():
            riga = riga.split(",")
            riga_int = [int(c) for c in riga]
            mappa.append(riga_int)

    num_colonne = len(mappa[0])
    num_righe = len(mappa)
    screen_width = num_colonne * lato_quad
    screen_height = num_righe * lato_quad
    matrice = [[-1 for _ in range(num_righe)] for _ in range(num_colonne)]

    screen = pygame.display.set_mode((screen_width, screen_height))
    font = pygame.font.SysFont(None, 30)

    pygame.display.set_caption("Mappa")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_map(screen, mappa, lato_quad, pavimento, muro, font, matrice)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
