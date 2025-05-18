from Configurations import Configurations
import pygame
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

def screen_refresh(screen:pygame.surface.Surface)->None:
    """
    Función que administra los elementos visuales del juego.
    :return:
    """
    # Se dibujan los elementos gráficos en la pantalla.
    screen.fill(Configurations.get_background())
    # SE actualiza la pantalla.
    pygame.display.flip()