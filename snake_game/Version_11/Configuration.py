class Configurations:
    """
    Clase que contine todas las configuraciones del juego
    """
    #Configuraciones de la pantala
    _screen_size = (1280, 720)
    _game_title = "Snake game en pygame"
    #_background = (234, 137, 154)
    _fps = 8 #fps del juego
    _game_over_screen_time=1

    #Configuraciones de la serpiente
    #Que sea un divisor común con en screen size ⬇️
    _snake_block_size = 45 #Tamaño del bloque de la serpiente
    _snake_head_color = (255, 233, 34)
    _snake_body_color = (0, 255, 0)

    #Configuracion de la manzana.
    _apple_color=(255,0,0)
    _apple_block_size=_snake_block_size

    #Las rutas de los archivos multimedias
    _background_image_path = "../Media/background_image.jpg"
    _apple_images_path=["../Media/apple1.png","../Media/apple2.png","../Media/apple3.png","../Media/apple4.png"]
    _snake_head_images_path=["../Media/head1.png","../Media/head2.png","../Media/head3.png","../Media/head4.png",
                            "../Media/head5.png","../Media/head6.png","../Media/head7.png","../Media/head8.png"]
    _snake_body_image_path=["../Media/body1.png",
                            "../Media/body2.png",
                            "../Media/body3.png"]
    """Nuevo"""
    #Configuracion de la musica del juego.
    _music_volume = 0.25                           # Volumen de la música de fondo (valor entre 0 y 1).
    _music_fadeout_time = _game_over_screen_time * 1000  # Duración del desvanecimiento de la música (en ms).

    """NUEVO."""
    # Rutas de los audios utilizados en la clase Audio.
    _music_path = "../Media/music.mp3"
    _start_sound_path = "../Media/start_sound.wav"
    _eats_apple_sound_path = "../Media/eats_apple_sound.wav"
    _game_over_sound_path = "../Media/game_over_sound.wav"

    @classmethod
    def get_apple_block_size(cls)->int:
        """
        Getter para _apple_block_size
        :return:
        """
        return cls._apple_block_size

    @classmethod
    def get_screen_size(cls) -> tuple[int, int]:
        """
        Getter para screen_size
        """
        return cls._screen_size

    @classmethod
    def get_game_title(cls) -> str:
        """
        Getter para get_game_title
        """
        return cls._game_title

    #@classmethod
    #def get_background(cls) -> tuple[int,int, int]:
    #   return cls._background

    @classmethod
    def get_fps(cls) -> int:
        """
        Getter para _fps
        :return:
        """
        return cls._fps

    @classmethod
    def get_game_over_screen_time(cls) -> int:
        """
        Getter para _fps
        :return:
        """
        return cls._game_over_screen_time

    @classmethod
    def get_snake_block_size(cls) -> int:
        return cls._snake_block_size

    @classmethod
    def get_snake_head_color(cls) -> tuple[int, int, int]:
        return cls._snake_head_color

    @classmethod
    def get_snake_body_color(cls) -> tuple[int, int, int]:
        return cls._snake_body_color

    @classmethod
    def get_background_image_path(cls)->str:
        """
        Getter para _background_image_path
        :return:
        """
        return cls._background_image_path
    @classmethod
    def get_apple_images_path(cls)->list:
        """
        Getter para _apple1
        :return:
        """
        return cls._apple_images_path

    @classmethod
    def get_head_images_path(cls)->list:
        """
        Getter para _apple1
        :return:
        """
        return cls._snake_head_images_path
    @classmethod
    def get_apple_body_image_path(cls)->list[str]:
        """
        Getter para _apple1
        :return:
        """
        return cls._snake_body_image_path


    """NUEVO. Se agregaron los métodos de acceso."""
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
    def get_start_sound_path(cls) -> str:
        """
        Getter para _start_sound_path.
        """
        return cls._start_sound_path

    @classmethod
    def get_eats_apple_sound_path(cls) -> str:
        """
        Getter para _eats_apple_sound_path.
        """
        return cls._eats_apple_sound_path

    @classmethod
    def get_game_over_sound_path(cls) -> str:
        """
        Getter para _game_over_sound_path.
        """
        return cls._game_over_sound_path

