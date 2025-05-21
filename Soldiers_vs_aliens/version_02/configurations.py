class Configurations():
    _scren_size=(1200,700)
    _game_Title=""
    _bacground=(255,153,121)

#__-------------------------METODOS DE ACCESO----------------
    @classmethod
    def get_screen_size(cls):
      """
      Getter pasa screen_siz
      :return:
      """
      return cls._scren_size

    @classmethod
    def get_game_title(cls):
      """
      Getter pasa screen_siz
      :return:
      """
      return cls._game_Title
    @classmethod
    def get_background(cls):
      """
      Getter pasa screen_siz
      :return:
      """
      return cls._bacground
