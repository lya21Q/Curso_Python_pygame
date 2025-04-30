class Configurations:
    """
    Clase que contine todas las configuraciones del juego
    """
    #Configuraciones de la pantala
    _screen_size = (1280, 720)
    _game_title = "Snake game en pygame"
    #_background = (234, 137, 154)
    _fps = 8 #fps del juego
    _game_over_screen_time=4

    #Configuraciones de la serpiente
    #Que sea un divisor común con en screen size ⬇️
    _snake_block_size = 45 #Tamaño del bloque de la serpiente
    _snake_head_color = (255, 233, 34)
    _snake_body_color = (0, 255, 0)

    #Configuracion de la manzana.
    _apple_color=(255,0,0)
    _apple_block_size=45

    #Las rutas de los archivos multimedias
    _background_image_path = "../Media/background_image.jpg"
    _apple_image_path="../Media/apple1.jpg"
    _snake_head_image_path="../Media/head1.png"
    _snake_body_image_path=["../Media/body1.png",
                            "../Media/body2.png",
                            "../Media/body3.png"]

    #@classmethod
    #def get_apple_color(cls)->tuple[int,int,int]:
      #  """
      #  Getter para _apple_color
    #    :return:
     #   """
   #     return cls._apple_color

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
    def get_background_image_path(cls):
        """
        Getter para _background_image_path
        :return:
        """
        return cls._background_image_path
    @classmethod
    def get_apple_image_path(cls):
        """
        Getter para _apple1
        :return:
        """
        return cls._apple_image_path

    @classmethod
    def get_apple_image_path(cls):
        """
        Getter para _apple1
        :return:
        """
        return cls._apple_image_path
    @classmethod
    def get_apple_head_image_path(cls):
        """
        Getter para _apple1
        :return:
        """
        return cls._snake_head_image_path
    @classmethod
    def get_apple_body_image_path(cls):
        """
        Getter para _apple1
        :return:
        """
        return cls._snake_body_image_path

