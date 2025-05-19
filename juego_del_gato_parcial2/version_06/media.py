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
        #self.rect.topleft = (560,180)  # Puedes cambiar la posición
        self.rect.centerx = 1280 // 2  # Centrado horizontal
        self.rect.top = 20  # Posición vertical superior

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
        self.image = pygame.image.load(Configurations.get_creditos_image())
        self.image = pygame.transform.scale(self.image, (800, 300))
        screen_rect = pygame.display.get_surface().get_rect()
        self.rect = self.image.get_rect(bottom=screen_rect.bottom)

    def blit(self, screen: pygame.surface.Surface):

        screen.blit(self.image, self.rect)