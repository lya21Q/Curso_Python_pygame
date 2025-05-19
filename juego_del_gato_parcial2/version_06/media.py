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
class Turnlmage:
    def __init__(self):
        pygame.init()
        self.image_X = pygame.image.load("../media/turnX.png")
        self.image_O = pygame.image.load("../media/turnO.png")
        self.image=self.image_X
        self.cambiar_imagen="X"

        # Escalar las imágenes a tamaño adecuado
        self.turnX = pygame.transform.scale(self.image_X, (800, 180))
        self.turnO = pygame.transform.scale(self.image_O, (800, 180))

        # Inicialmente muestra el turno X
        self.image = self.turnX
        self.rect = self.image.get_rect()
        #self.rect.topleft = (560,180)  # Puedes cambiar la posición
        self.rect.centerx = 1280 // 2  # Centrado horizontal
        self.rect.top = 20  # Posición vertical superior

    def change_turn(self,current_turn:str):
        if current_turn == "X":
            self.image = self.image_O  # Cambiar a ⭘
        else:
            self.image = self.image_X  # Cambiar a x

    def blit(self, screen: pygame.surface.Surface):
        screen.blit(self.image, self.rect)


