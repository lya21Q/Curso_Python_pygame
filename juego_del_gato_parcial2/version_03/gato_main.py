import pygame

from Configurations import Configurations
from Game_funcionalities import game_events, screen_refresh
from media import Background

def run_game()->None:
    """
    Funcion principal del videojuego.
    :return:
    """
    #Se inicializa el módulo de pygame.
    pygame.init()
    #Se configura el reloj del juego.
    clock=pygame.time.Clock()

    #Se inicializa la pantalla.
    #screen_size=(1200,700)

    screen=pygame.display.set_mode(Configurations.get_screen_size())

    #SE configura el titulo del juego.
    pygame.display.set_caption(Configurations.get_game_title())

    """nUEVO"""
    background=Background()

    # Ciclo principal del videojuego
    game_over=False
    while not game_over:
        game_over=game_events()
        if game_over:
            break
        #Se dibujan los elementos gráficos de la pantalla.
        screen_refresh(screen,clock,background)

    #Se cierran los recursos de pygame.
    pygame.quit()

if __name__=="__main__":
    run_game()