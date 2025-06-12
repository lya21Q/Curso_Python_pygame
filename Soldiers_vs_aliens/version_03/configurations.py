class Configurations():
    _screen_size=(1200,700)
    _game_Title="Soldiers_vs_aliens"
    #_background=(255,153,121)
    _fps=8
    #Tamaño del soldado
    _soldier_block_size=70
    """Fondo de pantalla"""
    _background_image_path= "../media/background_image.png"
    """IMAGEN SOLDADO"""
    _soldado_image_path= "../media/soldado.png"
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
    def get_soldado_image_path(cls)->str:
      """
      Getter pasa screen_siz
      :return:
      """
      return cls._soldado_image_path

    @classmethod
    def get_soldier_block_size(cls)->int:
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