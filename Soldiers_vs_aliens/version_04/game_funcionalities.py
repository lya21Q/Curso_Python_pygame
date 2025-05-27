import pygame
from Media import Background
from configurations import Configurations
from Soldier import Soldier

def game_events(soldier:Soldier)->bool:
    """
    Función para administrar.
    :return:
    """
    # Se declara la bandera de fin del juego que se retorna.
    game_over = False
    # Se verifican los eventos (teclado y ratón) del juego.
    for event in pygame.event.get():
        # El evento es un clic para cerrar el juego.
        if event.type == pygame.QUIT:
            game_over = True
        #Se verifica el evento de presionar una tecla.
        if event.type == pygame.KEYDOWN:
            #Se verifican las teclas del movimiento.
            if event.key == pygame.K_UP:
                Soldier.is_moving_up = True

            if event.key == pygame.KEYDOWN:
                Soldier.is_moving_down = True
        #Ahora se verifica el evento de soltar una tecla.
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                soldier.is_moving_up=False
        if event.type==pygame.KEYDOWN:
            soldier.is_moving_up=False

    return game_over

def screen_refresh(screen: pygame.surface.Surface,
                   clock:pygame.time.Clock,
                   background:Background,soldier:Soldier) -> None:
    """
    Función que administra las funcionalidades.
    :param screen:
    :return:
    """
    # Se dibuja el fondo de la pantalla.
    background.blit(screen)
    # Se actualiza la posición del soldado, se anima su sprite y se dibuja en la pantalla.
    soldier.update_position(screen)
    soldier.blit(screen)

    # Se actualiza la pantalla, dando la impresión de movimiento.
    pygame.display.flip()

    # Se controla la velocidad de fotogramas (FPS) del videojuego.
    clock.tick(Configurations.get_fps())
