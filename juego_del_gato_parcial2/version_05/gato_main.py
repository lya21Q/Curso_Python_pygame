"""
Nombre: ROSALINDA Aquino Perez
Fecha: [Agrega la fecha aquí]
Juego: Gato
Versión: 0.1
"""
import pygame
from pygame.sprite import Group
from Configurations import Configurations
from Game_funcionalities import screen_refresh, game_events
from media import Background,TurnImage

def run_game() -> None:
    """
    Función principal del videojuego del gato.
    """
    pygame.init()

    screen = pygame.display.set_mode(Configurations.get_screen_size())
    pygame.display.set_caption(Configurations.get_game_title())
    ##Reloj del juego
    clock = pygame.time.Clock()

    #Imagen de fondo
    background = Background()
    #imagen de turno.
    turn_image=TurnImage()
    #Grupo para las marcas
    marks = Group()

    game_over = False
    while not game_over:
        game_over = game_events(marks,turn_image)
        screen_refresh(screen, clock, background, marks,turn_image)

    pygame.quit()

if __name__ == '__main__':
    run_game()