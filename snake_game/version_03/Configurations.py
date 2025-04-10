import pygame
class configurations:
    """
    Clase que contiene todas las configuraciones del juego.
    atributos de instancia
    """
    #Configuraciones de la pantalla.
    _screen_size = (1280, 720)           # Resolución de la pantalla.
    #SE configura el titulo del juego.
    _game_title="Snake game en pygame"   #Titulo del juego
    _background = (255, 153, 204)

    #Configuración de la serpiente
    _snake_block_size=80        #Tamaño del bloque de la serpiente.
    _snake_head_color=(0,255,255)#Color del cuerpo
    _snake_body_color=(51,204,204)
    _fps=8


    # Fondo de la pantallla.

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

    @classmethod
    def get_fps(cls)->int:
        """
        Getter para _background
        """
        return cls._fps

    #Se crea el método de acceso
    @classmethod
    def get_snake_block_size(cls)->int:
        """
        Getter para _screen_size.
        :return:
        """
        return  cls._snake_block_size
    @classmethod
    def get_snake_head_color(cls)->tuple[int,int,int]:
        """
        Getter para _game_title.
        :return:
        """
        return cls._snake_head_color

    @classmethod
    def get_snake_body_color(cls)->tuple[int,int,int]:
        """
        Getter para _background
        """
        return cls._snake_body_color
