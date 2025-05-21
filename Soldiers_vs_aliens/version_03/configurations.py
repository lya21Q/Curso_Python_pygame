class Configurations():
    _screen_size=(1200,700)
    _game_Title="Soldiers_vs_aliens"
    #_background=(255,153,121)
    _fps=8
    """Fondo de pantalla"""
    _background_image_path="../media/fondo.png"
    """IMAGEN SOLDADO"""
    _soldado_image_path= "../media/soldado.png"
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