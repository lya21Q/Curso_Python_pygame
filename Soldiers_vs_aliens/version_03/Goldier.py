import pygame
from pexpect.screen import screen
from pygame.sprite import Sprite
from configurations import Configurations

class Soldier(Sprite):
    def __init__(self,sprite:Sprite):
        super().__init__()
        soldier_image=Configurations.get_soldado_image_path()
        self.image=pygame.image.load(Configurations.get_soldado_image_path())


    def blit(self,screen:pygame.surface):
        """

        :param screen:
        :return:
        """
        screen.blit(self.image.blit())