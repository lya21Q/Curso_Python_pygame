import pygame
from configurations import Configurations
class Background:
    def __init__(self):
        background_image=Configurations.get_background_image_path()
        self.image=pygame.image.load(Configurations.get_background_image_path())
        self.image=pygame.image.load(Configurations.get_background_image_path())
        #Se reescala el tamaño de la pantalla.
        screen_size=Configurations.get_screen_size()
        self.image=pygame.transform.scale(self.image,screen_size)
        self.rect=self.image.get_rect()


    def blit(self,screen:pygame.surface.Surface):
        """

        :param screen:
        :return:
        """
        screen.blit(self.image,self.rect)

