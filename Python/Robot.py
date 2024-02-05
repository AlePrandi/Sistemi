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
            rig = []
            rig = [int(c) for c in riga[:-1]]
            mat.append(rig)
    print(mat)
    
    lato_x = 100
    lato_y = 100
    
    n_x = len(mat[0]) 
    n_y = len(mat)
    
    pygame.init()
    screen = pygame.display.set_mode(n_x * lato_x, n_y * lato_y)
    
    for riga in mat:
        for c in riga:
            surf1 = pygame.Surface(lato_x, lato_y)
            if c == 1:
                surf1.fill("white")
            else:
                surf1.fill("black")
            
            rect1 = surf1.get_rect()
            rect1.topleft(lato_x - 100, lato_y - 100)
            screen.blit(surf1, rect1)
            pygame.display.flip()
            lato_x += 100
        lato_y += 100

if __name__ == '__main__':
    main()