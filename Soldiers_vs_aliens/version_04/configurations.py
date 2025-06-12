class Configurations():
    _screen_size=(1280,700)
    _game_Title="Soldiers vs aliens"
    _fps=30
    #Tamaño del soldado
    _soldier_block_size=(142,76)
    """NUEVO."""
    _frames_per_row = 4  # Número de frames que contiene cada fila de la hoja de frames.
    _soldier_frame_delay = 300  # Tiempo de cada frame del personaje (en ms).
    _soldier_speed = 12.5  # Velocidad (en píxeles) del personaje.

    """Fondo de pantalla"""
    _background_image_path="../media/background_image.jpg"
    """IMAGEN SOLDADO"""
    _soldier_sheet_path= "../media/soldier-idle-sheet.png"
    _game_over_screen_time = 1
#__-------------------------METODOS DE ACCESO----------------
    @classmethod
    def get_screen_size(cls)->tuple[int,int]:
      """
      Getter pasa screen_siz
      :return:
      """
      return cls._screen_size

    @classmethod
    def get_game_title(cls)->str:
      """
      Getter pasa screen_siz
      :return:
      """
      return cls._game_Title

    @classmethod
    def get_fps(cls)->int:
        """
        Getter pasa screen_siz
        :return:
        """
        return cls._fps

    @classmethod
    def get_background_image_path(cls)->str:
      """
      Getter pasa screen_siz
      :return:
      """
      return cls._background_image_path
    @classmethod
    def get_soldier_block_size(cls)->tuple[int,int]:
        """
        getter para _soldier_block_size
        :return:
        """
        return cls._soldier_block_size
    @classmethod
    def get_game_over_screen_time(cls) -> int:
        """
        Getter para _fps
        :return:
        """
        return cls._game_over_screen_time

    @classmethod
    def get_soldier_speed(cls)->float:
        """

        :return:
        """
        return cls._soldier_speed

    """NUEVO."""
    @classmethod
    def get_frames_per_row(cls) -> int:
        """
        Getter para _soldier_frames_per_row.
        """
        return cls._frames_per_row

    """NUEVO."""
    @classmethod
    def get_soldier_frame_delay(cls) -> int:
        """
        Getter para _soldier_frame_delay.
        """
        return cls._soldier_frame_delay

    """NUEVO."""
    @classmethod
    def get_soldier_sheet_path(cls) -> str:
        """
        Getter para _soldier_sheet_path.
        """
        return cls._soldier_sheet_path