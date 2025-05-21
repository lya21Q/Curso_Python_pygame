from configurations import Configurations
import pygame
def game_events()->bool:
    """
    Función para administrar.
    :return:
    """
    "Se declara la bandera en fin de juego."
    game_over=False
    for event in pygame.event.get():
        game_over=True
    return game_over

def screen_refrrsh(screen:pygame.surface.Surface):
    """
    Función que administra las funcionalidades.
    :param screen:
    :return:
    """
    screen.fill(Configurations.get_background())
    pygame.display.flip()

