class Configurations():
    _screen_size=(1280,700)
    _game_Title="Soldiers vs aliens"
    _fps=20
    #Tamaño del soldado
    _soldier_block_size=(142,76)
    _frames_per_row = 4  # Número de frames que contiene cada fila de la hoja de frames.
    """NUEVO."""
    _soldier_frames_columns=2
    _soldier_frame_delay = 300  # Tiempo de cada frame del personaje (en ms).

    _soldier_shooting_frame_delay=34
    _soldier_speed=12.5

    """Configuracion del disparo"""
    _shot_speed=32.5
    _shot_size=(30,30)
    _shot_frame_per_row=4
    _shot_frame_delay = 100

    """Fondo de pantalla"""
    _background_image_path="../media/background_image.jpg"
    """IMAGEN SOLDADO"""
    _soldier_sheet_path = "../media/soldier-idle_shooting_sheet.png"
    _game_over_screen_time = 1

    _shot_sheet_path= "../media/shot-sheet.png"

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
    def get_shot_size(cls)->tuple[int,int]:
        """
        getter para _soldier_block_size
        :return:
        """
        return cls._shot_size
    """NUEVO."""
    @classmethod
    def get_frames_per_row(cls) -> int:
        """
        Getter para _soldier_frames_per_row.
        """
        return cls._frames_per_row

    """NUEVO."""
    @classmethod
    def get_soldier_frame_columns(cls) -> int:
        """
        Getter para _soldier_frames_per_row.
        """
        return cls._soldier_frames_columns
    """NUEVO."""
    @classmethod
    def get_soldier_frames_delay(cls) -> int:
        """
        Getter para _soldier_frame_delay.
        """
        return cls._soldier_frame_delay
    """NUEVO."""
    @classmethod
    def get_soldier_shooting_frame_delay(cls)->float:
        """

        :return:
        """
        return cls._soldier_shooting_frame_delay
    @classmethod
    def get_soldier_speed(cls)->float:
        """

        :return:
        """
        return cls._soldier_speed
    @classmethod
    def get_game_over_screen_time(cls) -> int:
        """
        Getter para _fps
        :return:
        """
        return cls._game_over_screen_time

    @classmethod
    def get_shot_speed(cls)->float:
        """

        :return:
        """
        return cls._shot_speed
    """NUEVO."""
    @classmethod
    def get_soldier_sheet_path(cls) -> str:
        """
        Getter para _soldier_sheet_path.
        """
        return cls._soldier_sheet_path

    """NUEVO."""
    @classmethod
    def get_shot_sheet(cls) -> str:
        """
        Getter para _soldier_sheet_path.
        """
        return cls._shot_sheet_path

    """NUEVO."""
    @classmethod
    def get_shot_frame_delay(cls)->float:
        """

        :return:
        """
        return cls._shot_frame_delay
    @classmethod
    def get_shot_frame_per_row(cls)->int:
        """
        :return:
        """
        return cls._shot_frame_per_row

