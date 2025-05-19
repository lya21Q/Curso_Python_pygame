import pygame
from Configurations import Configurations
class Background:
    """
    Clase que contiene el fondo de pantalla.
    """

    def __init__(self):
        background_image_path = Configurations.get_background_image_path()
        self.image = pygame.image.load(background_image_path)

        # Se escala la imagen al tamaño de pantalla.
        screen_size = Configurations.get_screen_size()
        self.image = pygame.transform.scale(self.image,screen_size)

        self.rect = self.image.get_rect()


    def blit(self,screen: pygame.surface.Surface):
        """
        Se utiliza para dibujar el fondo de pantalla.
        """
        screen.blit(self.image, self.rect)
class TurnImage:
    def __init__(self):
        pygame.init()
        self.turnX = pygame.image.load("../media/turnX.png")
        self.turnO = pygame.image.load("../media/turnO.png")

        # Escalar las imágenes a tamaño adecuado
        self.turnX = pygame.transform.scale(self.turnX, (800, 180))
        self.turnO = pygame.transform.scale(self.turnO, (800, 180))

        # Inicialmente muestra el turno X
        self.image = self.turnX
        self.rect = self.image.get_rect()
        self.rect.centerx = 1280 // 2
        self.rect.top = 20

    def change_turn(self,current_turn:str):
        if current_turn == "X":
            self.image = self.turnO  # Cambiar a ⭘
        else:
            self.image = self.turnX  # Cambiar a x

    def blit(self, screen: pygame.surface.Surface):
        screen.blit(self.image, self.rect)

class ResultsImage:
    def __init__(self,resultado):
        if resultado == 'X':
            self.image = pygame.image.load(Configurations.get_winX_image())
        elif resultado == 'O':
            self.image = pygame.image.load(Configurations.get_winO_image())
        else:
            self.image = pygame.image.load(Configurations.get_draw_image())

       # self.image = pygame.transform.scale(pygame.image.load(self.image), (800, 200))
        self.rect = self.image.get_rect(center=(640, 360))


    def blit(self, screen):
        screen.blit(self.image, self.rect)

class CreditsImage:
    def __init__(self):
        """
        Carga la imagen de los créditos.
        """
        self.image = pygame.image.load(Configurations.get_credits_image())
        self.image = pygame.transform.scale(self.image, (800, 300))
        self.rect = self.image.get_rect(center=(640,580))

    def blit(self, screen: pygame.surface.Surface):

        screen.blit(self.image, self.rect)

class Audio:
    def __init__(self):
        """
        Para cargar el Audio..
        """
        pygame.mixer.music.load(Configurations.get_music_path())
        #El sonido del inicio del juego
        self._results_sound=pygame.mixer.Sound(Configurations.get_results_sound())
        self._keyboard_sound=pygame.mixer.Sound(Configurations.get_keyboad_sound())

    @classmethod
    def play_music(cls, volume) -> None:
        """
        Se utiliza para reproducir la música en bucle.
        """
        pygame.mixer.music.play(loops=-1)   # Un -1 indica que la música se reproduce en bucle.
        pygame.mixer.music.set_volume(volume)

    @classmethod
    def music_fadeout(cls, time) -> None:
        """
        Se utiliza para realizar un desvanecimiento de la música del juego hasta parar.
        :param time: Tiempo de desvanecimiento de la música (en ms).
        """
        pygame.mixer.music.fadeout(time)

    def results_sounds(self):
        """

        :return:
        """
        self._results_sound.play()

    def keyboard_sound(self):
        """

        :return:
        """
        self._keyboard_sound.play()





