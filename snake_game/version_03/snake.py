import pygame
from pygame.sprite import Sprite

class SnakeBlock(Sprite):
    def __init__(self):
        """
        Constructor de clase.
        """
        super().__init__()

        color = (255,128,128)

        self.image=pygame.Surface((40,40))#Largo y ancho
        self.image.fill(color)

        self.rect=self.image.get_rect()


    def blit(self,screen:pygame.surface.Surface)->None:
        """
            Se utiliza para dibujar el bloque de la serpiente.
        :param screen: Pantalla donde se dibujo.
        :return:
        """
        screen.blit(self.image,self.rect)