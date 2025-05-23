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

    def uptade_position(self):
        """

        :return:
        """
        if(self.is_moving_up):
            self.rect.y-=10
        if(self._is_moving_down):
            self.rect.y+=10

    @property
    def is_moving_up(self)->int:
        return self._is_moving_up

    @is_moving_up.setter
    def is_movin_down(self,is_moving_upt:int)->None:
        self._is_moving_up=is_moving_upt

    @property
    def is_moving_down(self):
        return self._is_moving_down

    @is_moving_up.setter
    def is_movin_down(self,is_moving_downt:int)->None:
        self._is_moving_downt=is_moving_downt