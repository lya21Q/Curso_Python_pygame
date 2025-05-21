import time
from Media import Background
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
        if event.type==pygame.QUIT:
            game_over=True
    return game_over

def screen_refresh(screen:pygame.surface.Surface,clock:pygame.time.Clock,background:Background)->None:
    """
    Función que administra las funcionalidades.
    :param screen:
    :return:
    """
    background.blit(screen)
    #screen.fill(Configurations.get_background_image_path())
    pygame.display.flip()
    clock.tick(Configurations.get_fps())

