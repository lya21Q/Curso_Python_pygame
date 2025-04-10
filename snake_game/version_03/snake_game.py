import pygame
from Configurations import configurations
from game_funcionalites import game_events, screen_refresh
from snake import  SnakeBlock

def run_game()->None:
    """
    Funcion principal del videojuego..
    :return:
    """

    pygame.init()

    #Se inicializa la pantalla.
    screen=pygame.display.set_mode(configurations.get_screen_size())

    #Se configura el título del juego.
    pygame.display.set_caption(configurations.get_game_title())

    snake_head=SnakeBlock()

    #Ciclo principal del videojuego
    game_over=False
    #Se verifican los eventos (teclado y ratón) del juego.
    while not game_over:
        game_over=game_events()
        #SE dibujam los elementos
        screen_refresh(screen,snake_head)
    #Se cierran los recursos de pygame.
    pygame.quit()

if __name__ == "__main__":
    run_game()