import pygame
from pygame.sprite import Sprite
from configurations import Configurations

class Soldier(Sprite):
    def __init__(self,screen:pygame.surface.Surface):
        super().__init__()
        """NUEVO..."""
        #Banderas de movimiento.
        self._is_moving_up = False
        self._is_moving_down = False
        """NUEVO."""
        # Lista que almacena los frames del soldado.
        self._frames = []

        self.image=pygame.image.load(Configurations.get_soldado_image_path())
        soldier_block_size=Configurations.get_soldier_block_size()
        self.image=pygame.transform.scale(self.image,(soldier_block_size,soldier_block_size))

        self.rect=self.image.get_rect()
        """Nuevo"""
        # Se inicializa la posición inicial, en este caso, a la derecha de la pantalla.
        screen_rect = screen.get_rect()
        self.rect.right = screen_rect.right
        self.rect.centery = screen_rect.centery
        """NUEVO."""
        # Se incluyen los atributos para el movimiento.
        self._rect_y = float(self.rect.y)
        self._speed = Configurations.get_soldier_speed()

    def update_position(self,screen:pygame.surface.Surface)->None:
        """

        :return:
        """
        # Se obtiene el rectángulo del borde de la pantalla
        screen_rect=screen.get_rect()
        if self.is_moving_up:
            self.rect.y-=self._speed
        elif self.is_moving_down:
            self.rect.y+=self._speed

        # Se verifica que el personaje no sobrepase los bordes de la pantalla.
        if self._rect_y < float(screen_rect.top):
            self._rect_y = float(screen_rect.y)

        elif self._rect_y > (screen_rect.bottom - self.image.get_height()):
            self._rect_y = float(screen_rect.bottom - self.image.get_height())

        # Se actualiza la posición del rectángulo de acuerdo a la posición.
        self.rect.y = int(self._rect_y)

    def blit(self,screen:pygame.surface):
        """

        :param screen:
        :return:
        """
        screen.blit(self.image.blit)


    @property
    def is_moving_up(self)->bool:
        return self._is_moving_up

    @is_moving_up.setter
    def is_moving_up(self,value:bool)->None:
        self._is_moving_up=value

    @property
    def is_moving_down(self):
        return self._is_moving_down

    @is_moving_down.setter
    def is_moving_down(self,value:bool)->None:
        self._is_moving_down=value