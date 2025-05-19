import pygame

class Configurations:
    """
    Clase que contiene las configuraciones del juego.
    """

    _screen_size = (1280,720)
    _game_title = "Juego del gato"
    _background = (20, 30, 50)
    _fps = 8
    _game_over_screen_time=5

    _background_image_path = "../media/background_image.png"
    #_markO_image_path = "../media/markO.png"
    #_markX_image_path = "../media/markX.png"
    _turnO_image = "../media/turnO.png"
    _turnX_image = "../media/turnX.png"


    _winX_image = "../media/winX.png"
    _winO_image = "../media/winO.png"


    _draw_image="../media/draw.png"
    _credits_image="../media/credits_image.png"

    """Nuevo"""
    #Configuracion de la musica del juego.
    _music_volume = 0.25                           # Volumen de la música de fondo (valor entre 0 y 1).
    _music_fadeout_time = _game_over_screen_time * 1000  # Duración del desvanecimiento de la música (en ms).

    _keyboad_sound= "..//media/keyboard_sound.mp3"
    _results_sound= "..//media/results_sound.mp3"
    _music_path= "..//media/music.mp3"

    # Posiciones de acuerdo a las teclas.
    _key_to_cell = {
        pygame.K_q: 1, pygame.K_w: 2, pygame.K_e: 3,
        pygame.K_a: 4, pygame.K_s: 5, pygame.K_d: 6,
        pygame.K_z: 7, pygame.K_x: 8, pygame.K_c: 9
    }

    # Posiciones de las marcas en el tablero.
    _cell_positions = {
        1: (500, 330), 2: (640, 330), 3: (780, 330),
        4: (500, 450), 5: (640, 450), 6: (780, 450),
        7: (500, 580), 8: (640, 580), 9: (780, 580),
    }


#---------------------MÉTODOS DE ACCESO
    @classmethod
    def get_screen_size(cls) -> tuple[int, int]:
        return cls._screen_size

    @classmethod
    def get_game_title(cls) -> str:
        return cls._game_title

    @classmethod
    def get_background(cls) -> tuple[int, int, int]:
        return cls._background

    @classmethod
    def get_fps(cls) -> int:
        return cls._fps
#------------------------------Audio---------------------------#
    @classmethod
    def get_music_volume(cls) -> float:
        """
        Getter para _music_volume.
        """
        return cls._music_volume

    @classmethod
    def get_music_fadeout_time(cls) -> int:
        """
        Getter para _music_fadeout_time.
        """
        return cls._music_fadeout_time

    @classmethod
    def get_music_path(cls) -> str:
        """
        Getter para _music_path.
        """
        return cls._music_path

    @classmethod
    def get_keyboad_sound(self):
        return self._keyboad_sound

    @classmethod
    def get_results_sound(self):
        return self._results_sound


    @classmethod
    def get_background_image_path(cls) -> str:
        return cls._background_image_path

    @classmethod
    def get_game_over_screen_time(cls) -> int:
        """
        Getter para _fps
        :return:
        """
        return cls._game_over_screen_time

#--------------Imagen ganador-----------------------
    @classmethod
    def get_winX_image(cls)->str:
        return cls._winX_image

    @classmethod
    def get_winO_image(cls)->str:
        return cls._winO_image
    #Empate
    @classmethod
    def get_draw_image(cls)->str:
        return cls._draw_image

    @classmethod
    def get_credits_image(cls)->str:
        return cls._credits_image
    @classmethod
    def get_key_to_cell(cls) -> dict:
        """
        Retorna el diccionario que relaciona teclas con casillas del tablero.
        """
        return cls._key_to_cell

    @classmethod
    def get_position(cls, cell: int) -> tuple[int, int]:
        """
        Retorna la posición (x, y) de la casilla en pantalla, según el número de celda.

        :param cell: número de la celda (1 a 9)
        :return: coordenadas (x, y) de la celda
        """
        return cls._cell_positions.get(cell, (0, 0))


