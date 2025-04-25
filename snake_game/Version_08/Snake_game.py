"""
Fecha: 08/04/2025
Version 02:
-Se agregó la clase Configurations en el módulo Cnfigurations.py que va a incluir todas las
configuraciones del juego
-Se agregó el módul Game funcine que admiistra los eve
"""
import pygame
from Configuration import Configurations
from Game_Funcionalities import game_events,snake_movement,screen_refresh,check_collision,game_over_screen
from Snake import  SnakeBlock
from pygame.sprite import Group

from Apple import Apple


#from Snake_game.Version_0_5.Game_Functionalities import snake_movement


def run_game() -> None:
    """
    Función principal del videojuego
    """
    #Se inicializa el módulo pygame
    pygame.init()
    #Se configur EL RELOJ DEL JUEGO
    clock = pygame.time.Clock()

    #Se inicializa la pantalla
    #screen_size = (1280, 720) #Resolución de la pantalla (ancho, alto)
    screen = pygame.display.set_mode(Configurations.get_screen_size() )

    #Se configura el título del juego
    #game_title = "Snake game en pygame"
    pygame.display.set_caption(Configurations.get_game_title())
    #Se crea el bloque inicial de la serpiente (cabeza)
    snake_head = SnakeBlock(is_head= True)
    snake_head.snake_head_init()

    #Se crea un grupo para almacenar el cuerpo de la serpiente
    snake_body = Group()
    snake_body.add(snake_head)

    #se crea el bloque inicial de la manzana.
    apple = Apple()
    apple.random_positions(snake_body)


    #Se crea un grupo con las manzanas
    apples=Group()
    apples.add(apple)

    #Ciclo principal de videojuego
    game_over = False
    while not game_over:
        game_over = game_events()
        #Condicion de que cerro la ventana
        if game_over:
            break

        #Se administra el movimiento de la serpiente
        snake_movement(snake_body)
        #Se revisan las colisiones en el juego
        game_over=check_collision(screen,snake_body,apples)
        #Si ha perdido el jugador se llama a la pantalla de fin de juego.
        #se revisan las condicones del juego
        check_collision(screen,snake_body,apples)
        #Se dibujan los elementos gráficos en la pantalla
        screen_refresh(screen, clock, snake_body,apples)
        if game_over:
            game_over_screen()

#Se cierran los eventos
pygame.quit()

if __name__ == '__main__':
    run_game()