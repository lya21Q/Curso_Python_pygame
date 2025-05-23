import pygame
from pygame.sprite import Sprite
from configurations import Configurations

class Soldier(Sprite):
    def __init__(self):
        super().__init__()

        self.image=pygame.image.load(Configurations.get_soldado_image_path())
        soldier_block_size=Configurations.get_soldier_block_size()
        self.image=pygame.transform.scale(self.image,(soldier_block_size,soldier_block_size))

        self.rect=self.image.get_rect()


    def blit(self,screen:pygame.surface):
        """

        :param screen:
        :return:
        """
        screen.blit(self.image.blit)