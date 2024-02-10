'''
simulare un robot che si sposta su un pavimento, bisogna definire una mappa con un file csv
traduciamo in 0 se la piastrella è libera e 1 se è occupata, in un file csv
'''
import pygame

def main():
    file = "mappa.csv"
    mat = []
    with open(file, 'r') as f:
        for riga in f.readlines():
            mat.append([int(valore) for valore in riga.strip().split(",")])
    print(mat)
    
    lato_x = 100
    lato_y = 100
    
    n_x = len(mat[0]) 
    n_y = len(mat)
    casella = pygame.image.load()
    
    pygame.init()
    screen = pygame.display.set_mode((n_x * lato_x, n_y * lato_y))
    
    for riga in mat:
        for c in riga:
            surf1 = pygame.Surface((lato_x, lato_y))
            if c == 1:
                surf1.blit(casella, (0,0))
                screen.blit(surf1, (lato_x - 100, lato_y - 100))
            else:
                screen.blit()
            
            rect1 = surf1.get_rect()
            rect1.topleft = (lato_x - 100, lato_y - 100)
            screen.blit(surf1, rect1)
            lato_x += 100
        lato_y += 100
        lato_x = 100
    
    pygame.display.flip() 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

if __name__ == '__main__':
    main()