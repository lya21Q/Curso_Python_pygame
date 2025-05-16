import pygame
from Configurations import Configurations
from game_funcionalites import game_events, screen_refresh
"""NUEVO."""
from snake import SnakeBlock

def run_game()->None:
    """
    Funcion principal del videojuego..
    :return:
    """

    pygame.init()

    #Se inicializa la pantalla.
    screen=pygame.display.set_mode(Configurations.get_screen_size())

    #Se configura el título del juego.
    pygame.display.set_caption(Configurations.get_game_title())
    """NUEVO."""
    clock = pygame.time.Clock()
    # Se crea el bloque inicial de la serpiente (cabeza) y se inicializa en un lugar aleatorio de la pantalla.
    snake_head = SnakeBlock(is_head = True)
    snake_head.snake_head_init()
    #Ciclo principal del videojuego
    game_over=False
    #Se verifican los eventos (teclado y ratón) del juego.
    while not game_over:
        game_over=game_events()
        """CAMBIO. Ahora recibe los objetos clock y snake_head."""
        # Función que administra los elementos de la pantalla.
        screen_refresh(screen, clock, snake_head)
    #Se cierran los recursos de pygame.
    pygame.quit()

if __name__ == "__main__":
    run_game()