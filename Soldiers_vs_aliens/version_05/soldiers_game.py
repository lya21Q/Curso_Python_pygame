import pygame
from game_funcionalities import game_events,screen_refresh
from Media import Background
from configurations import Configurations
from Soldier import Soldier
from shot import Shot
from pygame.sprite import Group

def run_game():
    """Funcion principal del videojuego."""

    #Se inicializa el módulo de pygame...
    pygame.init()
    screen_size=Configurations.get_screen_size()
    screen=pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()#Se utiliza para la velocidad de fotogramas(FPS).

    #Título del juego
    game_title=Configurations.get_game_title()
    pygame.display.set_caption(game_title)

    #Se crea el objeto de fondo de pantalla.
    background = Background()

    #Se crea el objeto del soldado.
    soldier=Soldier(screen)

    shots=Group()

    #Ciclo principal del juego.
    game_over=False
    while not game_over:
        game_over=game_events(soldier,shots)
        screen_refresh(screen,clock,background,soldier,shots)
    pygame.quit()


if __name__=="__main__":
    run_game()