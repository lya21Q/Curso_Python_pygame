import pygame
class Configurations():
    """
    Clase que contiene todas las configuraciones del juego.
    atributos de instancia
    """
    #Configuraciones de la pantalla.
    _screen_size = (1200, 700)  # Resolución de la pantalla.
    #SE configura el titulo del juego.
    _game_title="Juego del gato."   #Título del juego
    _background = (255, 153, 204)   # Fondo de la pantalla.

    #Se crea el método de acceso
    @classmethod
    def get_screen_size(cls)->tuple[int,int]:
        """
        Getter para _screen_size.
        :return:
        """
        return  cls._screen_size
    @classmethod
    def get_game_title(cls)->str:
        """
        Getter para _game_title.
        :return:
        """
        return cls._game_title

    @classmethod
    def get_background(cls)->tuple[int,int,int]:
        """
        Getter para _background
        """
        return cls._background