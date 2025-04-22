import pygame
from pygame.sprite import Sprite
from Configuration import Configurations

class Apple(Sprite):
    def __init__(self):
        super.__init__()

        self.image = pygame.Surface((10,10))
        self.image.fill((255,0,0,))

        self.rect = self.image.get_rect()

    def blit(self,screen:pygame.surface.surface)->None:
        """
        Se utiliza para dibujar la manzana.
        :param screen:
        :return:
        """
        screen.blit(self.image,self.rect)