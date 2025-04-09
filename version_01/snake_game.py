import pygame
def run_game()->None:
    """
    Funcion principal del videojuego..
    :return:
    """

    pygame.init()

    #Se inicializa la pantalla.
    screen_size=(1200,700)      #Resolución de la pantalla.
    screen=pygame.display.set_mode(screen_size)

    #SE configura el titulo del juego.
    game_title="Snake game en pygame"
    pygame.display.set_caption(game_title)

    #Ciclo principal del videojuego
    game_over=False
    #Se verifican los evenos (teclado y ratón) del juego.
    while not game_over:
        for event in pygame.event.get():
            #print(event)
            #Un clic en el juego
            if event.type == pygame.QUIT:#Cerrar ventana
                game_over = True

        #Se dibujan los elementos gráficos en la pantalla.
        backgroud =(255,153,204)  #Fondo de la pantallla.
        screen.fill(backgroud)

        #SE actualiza la pantalla.
        pygame.display.flip()
    #Se cierran los recursos de pygame.
    pygame.quit()

if __name__ == "__main__":
    run_game()