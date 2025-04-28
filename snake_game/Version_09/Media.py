import pygame
from Configuration import Configurations

class Background:
    """
    Clase que contiene el fondo de pantalla
    """

    def __init__(self):
        background_image_path=Configurations.get_background_image_path()
        self.image=pygame.image.load(background_image_path)
        #Se reescala el tamaño de la pantalla
        screen_size= Configurations.get_screen_size()
        self.image = pygame.transform.scale(self.image,screen_size)
        self.rect = self.image.get_rect()


    def blit(self,screen:pygame.surface.Surface):
        """
        Se utiliza para dibujar el fono fe pantalla
        :param screen:
        :return:
        """
        screen.blit(self.image,self.rect)

class Apple:
    def __init__(self):
        apple_image_path = Configurations.get_apple1()
        self.image=pygame.image.load(apple_image_path)
        #Se reescala el tamaño de la pantalla
        head=Configurations.get_screen_size()
        self.image=pygame.transform.scale(self.image,head)

    def blit(self,head:pygame.surface.Surface):
        """
        Paraa dibujar la manzana...
        :param head:
        :return:
        """
        head.blit(self.image,self.rect)