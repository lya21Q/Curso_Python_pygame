import pygame
from game_funcionalities import game_events,screen_refresh
from Media import Background
from configurations import Configurations
from Goldier import Soldier
from pygame.sprite import Group

def run_game():
    """Funcion principal del videojuego."""
    pygame.init()
    clock=pygame.time.Clock()
    #Se inicializa la pantalla.
    #screen_size=(1200,700)
    screen=pygame.display.set_mode(Configurations.get_screen_size())

    #Titulo del juego
    pygame.display.set_caption(Configurations.get_game_title())

    #Se crea el grupo para almacenar al soldado.
    soldier=Soldier()
    soldier=Group()
    soldier.add(soldier)

    background=Background()
    #Ciclo principal del juego.

    game_over=False
    while not game_over:
        game_over=game_events()
        if game_over:
            break
        screen_refresh(screen,clock,background,soldier)

    pygame.quit()



if __name__=="__main__":
    run_game()