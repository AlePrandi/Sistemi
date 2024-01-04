import pygame
import random
from os.path import join

WIDTH = 800
HEIGHT = 600
MAX_PUNT = 5000

class Giocatore:
    def __init__(self, pos_x, pos_y, n_vite):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.n_vite = n_vite
        self.vel = 5  # Velocità del giocatore
        self.immagine = pygame.image.load(join("Immagini","Aereo.png"))
        self.imm_vite = pygame.image.load(join("Immagini","Cuore.png"))
        self.player = self.immagine.get_rect()
        self.player.width = 140
        self.player.height = 40
        self.player.x = pos_x
        self.player.y = pos_y

    def muovi(self, tasti):
        if tasti[pygame.K_LEFT] and self.player.x > -10:
            self.player.x -= self.vel
        if tasti[pygame.K_RIGHT] and self.player.x < 690:
            self.player.x += self.vel
        if tasti[pygame.K_UP] and self.player.y > -50:
            self.player.y -= self.vel
        if tasti[pygame.K_DOWN] and self.player.y < 495:
            self.player.y += self.vel

    def disegna_vite(self, screen):
        for i in range(self.n_vite):
            screen.blit(self.imm_vite, (10 + i * 30, 10))

    def get_X(self):
        return self.player.x

    def get_Y(self):
        return self.player.y

    def disegna(self, screen):
        screen.blit(self.immagine, (self.player.x, self.player.y))

    def setVite(self, n_vite):
        self.n_vite = n_vite

    def getVite(self):
        return self.n_vite

    def dimVite(self):
        self.n_vite -= 1


class Nemico:
    def __init__(self, vel):
        self.pos_x, self.pos_y = 800, random.randint(-5, 690)
        self.vel = vel
        self.immagine = pygame.image.load(join("Immagini","Missile.png"))
        self.nemico = self.immagine.get_rect()
        self.nemico.width = 70
        self.nemico.height = 20
        self.nemico.x = self.pos_x
        self.nemico.y = self.pos_y

    def get_X(self):
        return self.nemico.x

    def get_Y(self):
        return self.nemico.y

    def muovi(self):
        self.nemico.x -= self.vel

    def disegna(self, screen):
        screen.blit(self.immagine, (self.nemico.x, self.nemico.y))


class Moneta:
    random.seed(1234)

    def __init__(self):
        pos_x = random.randint(0, 400)
        pos_y = random.randint(-20, 470)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.immagine = pygame.image.load(join("Immagini","Coin.png"))
        self.moneta = self.immagine.get_rect()
        self.moneta.x = pos_x
        self.moneta.y = pos_y

    def reset_posizione(self):
        self.pos_x = random.randint(0, 400)
        self.pos_y = random.randint(-20, 470)
        self.moneta.x = self.pos_x
        self.moneta.y = self.pos_y

    def get_X(self):
        return self.moneta.x

    def get_Y(self):
        return self.moneta.y

    def disegna(self, screen):
        screen.blit(self.immagine, (self.moneta.x, self.moneta.y))


def menu_difficolta():
    tema = pygame.mixer.Sound(join("Suoni","Tema.mp3"))
    tema.play()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Gioco Prandi ale")
    font = pygame.font.Font(None, 36)
    done = False
    difficolta = None

    while not done:
        screen.fill((0, 0, 0))
        pulsante = pygame.mixer.Sound(join("Suoni","Pulsante.mp3"))
        
        text_intro = font.render("Benvenuto, seleziona una difficolta per iniziare a giocare: ", True, (255, 255, 255))
        text_facile = font.render("Facile (meno nemici, vite extra)", True, (255, 255, 255))
        
        text_medio = font.render("Medio (nemici standard, vite normali)", True, (255, 255, 255))
        
        text_difficile = font.render("Difficile (più nemici, vite ridotte)", True, (255, 255, 255))

        screen.blit(text_intro, (WIDTH // 2 - 350, HEIGHT // 2 - 100))
        screen.blit(text_facile, (WIDTH // 2 - 200, HEIGHT // 2 - 50))
        screen.blit(text_medio, (WIDTH // 2 - 200, HEIGHT // 2))
        screen.blit(text_difficile, (WIDTH // 2 - 200, HEIGHT // 2 + 50))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if WIDTH // 2 - 200 < mouse_pos[0] < WIDTH // 2 + 200:
                    if HEIGHT // 2 - 50 < mouse_pos[1] < HEIGHT // 2 - 20:
                        pulsante.play()
                        difficolta = "facile"
                        done = True
                    elif HEIGHT // 2 < mouse_pos[1] < HEIGHT // 2 + 30:
                        pulsante.play()
                        difficolta = "medio"
                        done = True
                    elif HEIGHT // 2 + 50 < mouse_pos[1] < HEIGHT // 2 + 80:
                        pulsante.play()
                        difficolta = "difficile"
                        done = True

    tema.stop()
    return difficolta

def vittoria(punteggio):
    win = pygame.mixer.Sound(join("Suoni","Win.mp3"))
    win.play()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Gioco Prandi ale")
    font = pygame.font.Font(None, 36)
    done = False

    while not done:
        screen.fill((0, 0, 0))
        
        text = font.render("Hai vinto!!", True, (255, 255, 255))
        text_punt = font.render(f"Punteggio finale: {punteggio}", True, (255, 255, 255))
        text_uscita = font.render("Premi ESC per terminare", True, (255, 255, 255))

        screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
        screen.blit(text_punt, (WIDTH // 2 - 150, HEIGHT // 2))
        screen.blit(text_uscita, (WIDTH // 2 - 150, HEIGHT // 2 + 200))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
    
    pygame.QUIT()
    
def sconfitta():
    morte = pygame.mixer.Sound(join("Suoni","Sconfitta.mp3"))
    morte.play()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Gioco Prandi ale")
    font = pygame.font.Font(None, 36)
    done = False

    while not done:
        screen.fill((0, 0, 0))
        
        text = font.render("Hai perso :(", True, (255, 255, 255))
        text_uscita = font.render("Premi ESC per terminare", True, (255, 255, 255))

        screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
        screen.blit(text_uscita, (WIDTH // 2 - 150, HEIGHT // 2 + 200))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
    
    pygame.QUIT()

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Gioco Prandi Ale")
    background = pygame.image.load(join("Immagini","Background.png"))
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    done = False

    player = Giocatore(WIDTH // 2, HEIGHT // 2, 3)
    moneta = Moneta()
    sound_moneta = pygame.mixer.Sound(join("Suoni","Moneta.mp3"))
    sound_esplosione = pygame.mixer.Sound(join("Suoni","Esplosione.mp3"))
    
    spawn_timer = 0
    Lista_nemici = []
    punteggio = 0
    n_nemici = 0
    vel = 0

    difficolta = menu_difficolta()
    if difficolta:
        if difficolta == "facile":
            player.setVite(5)
            inter_spawn = 10000
            n_nemici = 1
            vel = 1

        elif difficolta == "medio":
            player.setVite(3)
            inter_spawn = 7000
            n_nemici = 3
            vel = 3

        elif difficolta == "difficile":
            player.setVite(1)
            inter_spawn = 5000
            n_nemici = 5
            vel = 5

    while not done:
        
        screen.blit(background, (0, 0))
        tasti = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True

        player.muovi(tasti)
        player.disegna(screen)
        player.disegna_vite(screen)
        moneta.disegna(screen)

        # fa apparire i nemici
        current_time = pygame.time.get_ticks()
        if current_time - spawn_timer > inter_spawn:
            for _ in range(0, n_nemici):
                nemico = Nemico(vel)
                Lista_nemici.append(nemico)
            spawn_timer = current_time

        # esegue le funzioni per ogni nemico
        for nemico in Lista_nemici:
            nemico.muovi()
            nemico.disegna(screen)
            if nemico.nemico.colliderect(player.player):
                player.dimVite()
                sound_esplosione.play()
                Lista_nemici.remove(nemico)
            if nemico.nemico.x < -70:
                Lista_nemici.remove(nemico)

        # rileva se il player tocca la moneta
        if player.player.colliderect(moneta.moneta):
            sound_moneta.play()
            punteggio += 100
            moneta.reset_posizione()

        if player.getVite() <= 0:
            sconfitta()

        if punteggio >= MAX_PUNT:
            vittoria(punteggio)

        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {punteggio}", True, (255, 255, 255))
        screen.blit(text, (WIDTH - 150, HEIGHT - 40))

        pygame.display.update()

    pygame.QUIT()

if __name__ == "__main__":
    main()
