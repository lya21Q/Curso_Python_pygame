from Configurations import Configurations
import pygame
"""NUEVO."""
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

"""CAMBIO. Ahora recibe los objetos clock y snake_head."""
def screen_refresh(screen: pygame.surface.Surface, clock: pygame.time.Clock,
                   snake_head: SnakeBlock) -> None:
    """
    Función que administra los elementos de la pantalla.
    :param screen: Objeto con la pantalla.
    :param clock: Objeto con el reloj del videojuego.
    :param snake_head: Objeto con la cabeza de la serpiente.
    """
    # Se dibujan los elementos en la pantalla.
    screen.fill(Configurations.get_background())    # Fondo de la pantalla en formato RGB.
    """NUEVO."""
    snake_head.blit(screen)                         # Se dibuja la cabeza de la serpiente.

    # Se actualiza la pantalla, dando la impresión de movimiento.
    pygame.display.flip()

    """NUEVO."""
    # Se controla la velocidad de fotogramas (FPS) del videojuego.
    clock.tick(Configurations.get_fps())