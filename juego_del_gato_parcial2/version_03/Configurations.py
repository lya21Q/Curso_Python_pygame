class Configurations():
    """
    Clase que contiene todas las configuraciones del juego.
    atributos de instancia
    """
    #Configuraciones de la pantalla.
    _screen_size = (1200, 700)  # Resolución de la pantalla.
    #SE configura el titulo del juego.
    _game_title="Juego del gato."   #Título del juego
    #_background = (255, 153, 204)   # Fondo de la pantalla.
    _fps=8

    """Nuevo"""
    _background_image_path="../media/background_image.png"

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


    #@classmethod
    #def get_background(cls)->tuple[int,int,int]:
     #   """
      #  Getter para _background
       # """
        #return cls._background
    """Nuevo"""
    @classmethod
    def get_fps(cls)->int:
        """
        getter para fps
        :return:
        """
        return cls._fps

    @classmethod
    def get_background_image_path(cls)->str:
        """
        getter para imagen background
        :return:
        """
        return cls._background_image_path