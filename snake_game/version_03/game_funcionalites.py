from pygame.examples.go_over_there import clock

from Configurations import configurations
import pygame

from snake import SnakeBlock

def game_events()->bool:
    """
    Función que administra los eventos del juego.
    :return: La bandera del fin del juego.
    """
    #Se declara la bandera en fin del juego.
    game_over = False
    #SE verifican los eventos (teclado y raton )
    for event in pygame.event.get():
        # print(event)
        # Un clic en el juego
        if event.type == pygame.QUIT:  # Cerrar ventana
            game_over = True

    return game_over

def screen_refresh(screen:pygame.surface.Surface,snake_head:SnakeBlock)->None:
    """
    Función que administra los elementos visuales del juego.
    :return:
    """
    # Se dibujan los elementos gráficos en la pantalla.
    screen.fill(configurations.get_background())
    #Se dibuja la cabeza de la serpiente.
    snake_head.blit(screen)
    # SE actualiza la pantalla.
    pygame.display.flip()

    #Se controla la velocidad
    clock.tick(configurations.get_fps())