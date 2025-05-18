from Configurations import Configurations
from Game_funcionalities import game_events, screen_refresh
import pygame
def run_game()->None:
    """
    Funcion principal del videojuego..
    :return:
    """
    pygame.init()
    #Se inicializa la pantalla.
    #screen_size=(1200,700)
    screen=pygame.display.set_mode(Configurations.get_screen_size())

    #SE configura el titulo del juego.
    pygame.display.set_caption(Configurations.get_game_title())

    #Ciclo principal del videojuego
    game_over=False
    #Se verifican los evenos (teclado y ratón) del juego.
    while not game_over:
        game_over=game_events()
        #Se dibujan los elementos.
        screen_refresh(screen)
    #Se cierran los recursos de pygame.
    pygame.quit()

if __name__=="__main__":
    run_game()