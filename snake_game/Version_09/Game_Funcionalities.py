import time

import pygame

from Configuration import Configurations
from Snake  import  SnakeBlock
from Apple import Apple
from Media import Background



def game_events() -> bool:
    """
    Función que administra fps en eventos del juego
    return: La bandera del fin del juego
    """

    #Se declara la bandera del fin del juego
    game_over = False

    #Se verifican los eventos de
    for event in pygame.event.get():
        #Un clic en cerrar el juego
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                SnakeBlock.set_is_moving_right(True)
                SnakeBlock.set_is_moving_left(False)
                SnakeBlock.set_is_moving_up(False)
                SnakeBlock.set_is_moving_down(False)


            if event.key == pygame.K_LEFT:
                SnakeBlock.set_is_moving_right(False)
                SnakeBlock.set_is_moving_left(True)
                SnakeBlock.set_is_moving_up(False)
                SnakeBlock.set_is_moving_down(False)

            if event.key == pygame.K_UP:
                SnakeBlock.set_is_moving_right(False)
                SnakeBlock.set_is_moving_left(False)
                SnakeBlock.set_is_moving_up(True)
                SnakeBlock.set_is_moving_down(False)

            if event.key == pygame.K_DOWN:
                SnakeBlock.set_is_moving_right(False)
                SnakeBlock.set_is_moving_left(False)
                SnakeBlock.set_is_moving_up(False)
                SnakeBlock.set_is_moving_down(True)

    #Se regresa la bandera
    return game_over


def snake_movement(snake_body: pygame.sprite.Group) -> None:
    """
    Funcion que gestiona el movimient del cuerpo de la serpiente

    :param snake_body:
    :return:
    """
    "Nuevo"
    body_size =len(snake_body.sprites()) -1
    for i in range(body_size,0, -1):
        snake_body.sprites()[i].rect.x = snake_body.sprites()[i - 1].rect.x
        snake_body.sprites()[i].rect.y = snake_body.sprites()[i-1].rect.y

    head = snake_body.sprites()[0]

    if SnakeBlock.get_is_moving_right():
        head.rect.x += Configurations.get_snake_block_size()
    elif SnakeBlock.get_is_moving_left():
        head.rect.x -= Configurations.get_snake_block_size()
    elif SnakeBlock.get_is_moving_up():
        head.rect.y -= Configurations.get_snake_block_size()
    elif SnakeBlock.get_is_moving_down():
        head.rect.y += Configurations.get_snake_block_size()

def check_collision(screen: pygame.surface.Surface,
                    snake_body: pygame.sprite.Group,
                    apples:pygame.sprite.Group)->bool:
    """
    Funcion que revisa las colisiones del juego:
    *cabeza de la serpiente con el cuerpo
    *cabza de la serpiente con el borde de la pantalla
    *cabeza de la serpiente con la mazana
    :param screen: Pantalla
    :param snake_body: Grupod con las manzanas
    :param apples: La bandea d efin de juego
    :return:
    """
    #Se declara la bandera de fin de juego.
    game_over=False

    head = snake_body.sprites()[0]

    #e revisa la cndicion de la cabeza  conla serpiente con r
    screen_rect=screen.get_rect()
    #borde de la pantalla
    if head.rect.right > screen_rect.right or head.rect.left < screen_rect.left or head.rect.bottom > screen_rect.bottom or head.rect.top < screen_rect.top:
        game_over=True
        return game_over
    #Se revisan la condición de la cabeza de la serpiente con el cuerpo de la serpiente.
    head_body_collisions=pygame.sprite.spritecollide(head,snake_body,dokill=False)

    if len(head_body_collisions) > 1:
        game_over=True

    #SE revisa la condicion de la cabeza de la serpiente con la de la manzana
    head_apples_collisions=pygame.sprite.spritecollide(head,apples,dokill=True)
    if len(head_apples_collisions) > 0:
        new_snake_block=SnakeBlock()#crea una nueva serpiente
        new_snake_block.rect.x=snake_body.sprites()[-1].rect.x
        new_snake_block.rect.y=snake_body.sprites()[-1].rect.y
        snake_body.add(new_snake_block)#añade al bloque
        new_apple=Apple()
        new_apple.random_positions(snake_body)
        apples.add(new_apple)
    return game_over


def screen_refresh(screen: pygame.surface.Surface,
                   clock: pygame.time.Clock,
                   snake_body: pygame.sprite.Group,apples:pygame.sprite.Group,background:Background) -> None:
    """
    Función que administrar los elementos visuales del juego
    """
    #Se dibuja el fondo
    background.blit(screen)

    #Fondo de la pantaña
    #screen.fill(Configurations.get_background())

    #Se dibuja el cuerpo de la serpiente
    for snake_block in reversed(snake_body.sprites()):
        snake_block.blit(screen)

    #se dibuja la manzana
    apples.draw(screen)

    pygame.display.flip()

    #Se controla la velocidad de FPS
    clock.tick(Configurations.get_fps())

def game_over_screen()->None:
    """
    Función que muestra con la parte del fin del jugo
    :return:
    """
    time.sleep(Configurations.get_game_over_screen_time())