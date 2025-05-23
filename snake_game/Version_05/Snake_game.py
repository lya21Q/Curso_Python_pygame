"""
Fecha: 08/04/2025
Version 02:
-Se agregó la clase Configurations en el módulo Cnfigurations.py que va a incluir todas las
configuraciones del juego
-Se agregó el módul Game funcine que admiistra los eve
"""
import pygame
from Configuration import Configurations
from Game_Funcionalities import game_event, screen_refresh, snake_movement
from Snake import  SnakeBlock
from pygame.sprite import Group

#from Snake_game.Version_0_5.Game_Functionalities import snake_movement


def run_game() -> None:
    """
    Función principal del videojuego
    """
    #Se inicializa el módulo pygame
    pygame.init()
    screen =pygame.display.set_mode(Configurations.get_screen_size())
    pygame.display.set_caption(Configurations.get_game_title())
    clock = pygame.time.Clock()

    #Se crea el bloque inicial de la serpiente (cabeza)
    snake_head = SnakeBlock(is_head= True)
    snake_head.snake_head_init()

    #Se crea un grupo para almacenar el cuerpo de la serpiente
    snake_body = Group()
    snake_body.add(snake_head)

    #Ciclo principal de videojuego
    game_over = False

    while not game_over:
        game_over = game_event()

        #Se administra el movimiento de la serpiente
        snake_movement(snake_body)

        #Se dibujan los elementos gráficos en la pantalla
        screen_refresh(screen, clock, snake_body)

    #Se cierran los eventos
    pygame.quit()

if __name__ == '__main__':
    run_game()