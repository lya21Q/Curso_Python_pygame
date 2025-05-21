import pygame
def run_game():
    """Funcion principal del videojuego."""
    pygame.init()

    #Se inicializa la pantalla.
    screen_size=(1200,700)
    screen=pygame.display.set_mode(screen_size)

    #Titulo del juego
    game_title=""
    game=pygame.display.set_caption(game_title)

    #Ciclo principal del juego.

    game_over=False
    while not game_over:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True

        bakground=(255,153,204)
        screen.fill(bakground)
        pygame.display.flip()
    pygame.quit()



if __name__=="__main__":
    run_game()