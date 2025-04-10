import pygame
from pygame.sprite import Sprite
from Configurations import configurations
from random import randint
class SnakeBlock(Sprite):
    def __init__(self,is_head:bool=False):
        """
        Constructor de clase.
        """
        super().__init__()
        if is_head:
            color = configurations.get_snake_head_color()
        else:
            color=configurations.get_snake_body_color()
        snake_block_size=configurations.get_snake_block_size()
        self.image=pygame.Surface((snake_block_size,snake_block_size))#Largo y ancho
        self.image.fill(color)

        self.rect=self.image.get_rect()


    def blit(self,screen:pygame.surface.Surface)->None:
        """
            Se utiliza para dibujar el bloque de la serpiente.
        :param screen: Pantalla donde se dibujo.
        :return:
        """
        screen.blit(self.image,self.rect)

    def snake_head_init(self)->None:
        screen_width=configurations.get_screen_size()[0]
        screen_height=configurations.get_screen_size()[1]
        snake_block_size=configurations.get_snake_block_size()

        self.rect.x = snake_block_size*randint(0,(screen_width//snake_block_size)-1)
        self.rect.y= snake_block_size *randint(0,(screen_height//snake_block_size)-1)