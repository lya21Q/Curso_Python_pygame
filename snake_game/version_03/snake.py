import pygame
from pygame.sprite import Sprite
from Configurations import Configurations
from random import randint

class SnakeBlock(Sprite):
    """
    Clase que representa un bloque del cuerpo de la serpiente.
    Hereda de la clase Sprite para utilizar grupos de sprites y detectar colisiones entre sprites.
    Sus atributos son: image (apariencia) y rect (posición y tamaño).
    Sus métodos son: blit() (dibujar), snake_head_init() (inicializa en una posición aleatoria).
    """
    def __init__(self, is_head: bool = False):
        """
        Constructor de la serpiente, en donde se llama al constructor padre de Sprite.
        :param is_head: Indica si el bloque es o no la cabeza de la serpiente.
        """
        # Se llama al constructor de la clase padre.
        super().__init__()

        # Se selecciona el color dependiendo de si es o no la cabeza de la serpiente.
        if is_head:
            color = Configurations.get_snake_head_color()
        else:
            color = Configurations.get_snake_body_color()

        # Se crea una imagen para el sprite (superficie cuadrada del tamaño del bloque de la serpiente),
        # rellenándola con el color correspondiente a si es la parte de la cabeza o del cuerpo.
        self.image = pygame.Surface((Configurations.get_snake_block_size(), Configurations.get_snake_block_size()))
        self.image.fill(color)

        # Se obtiene el rectángulo que representa la posición del sprite.
        self.rect = self.image.get_rect()


    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar el bloque de la serpiente en la pantalla.
        :param screen: Pantalla en donde se dibuja el bloque.
        """
        screen.blit(self.image, self.rect)


    def snake_head_init(self):
        screen_width = Configurations.get_screen_size()[0]
        screen_height = Configurations.get_screen_size()[1]
        snake_block_size = Configurations.get_snake_block_size()
        self.rect.x = snake_block_size * randint(0, (screen_width // snake_block_size - 1))
        self.rect.y = snake_block_size * randint(0, (screen_height // snake_block_size - 1))