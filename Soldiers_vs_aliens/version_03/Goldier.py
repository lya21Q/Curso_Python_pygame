import pygame
from pygame.sprite import Sprite
from configurations import Configurations

class Soldier:
    def __init__(self):
        soldier_image=Configurations.get_soldado_image_path()
        self.image=pygame.image.load(Configurations.get_soldado_image_path())