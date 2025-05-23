import time
import pygame
from Media import Background
from configurations import Configurations
from Soldier import Soldier

def game_events()->bool:
    """
    Función para administrar.
    :return:
    """
    #Se declara la bandera en fin de juego.
    game_over=False
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
    return game_over

def screen_refresh(screen: pygame.surface.Surface,
                   clock:pygame.time.Clock,background:Background,soldier:pygame.sprite.Group) -> None:
    """
    Función que administra las funcionalidades.
    :param screen:
    :return:
    """
    #se dibuja el fondo
    background.blit(screen)
    soldier.draw(screen)
    pygame.display.flip()
    clock.tick(Configurations.get_fps())

def game_over_screen()->None:
    """
    Función que muestra con la parte del fin del jugo
    :return:
    """
    time.sleep(Configurations.get_game_over_screen_time())