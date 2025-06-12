import pygame
from pygame.sprite import Sprite
from configurations import Configurations
from random import randint,choice

class Aliens(Sprite):
    """
    Clase que representa aliens.
    """
    def __init__(self,screen):
        """
        Constructor para aliens.
        """
        # Se llama al constructor de la clase padre.
        super().__init__()
        #Banderas de movimiento.
        self._is_moving_up = False
        self._is_moving_down = False
        self._is_shooting=False
        # Lista que almacena los frames del soldado.
        self._frames = []

        # Se carga la hoja que contiene los frames del disparo.
        sheet_path = choice(Configurations.get_aliens_path())
        alien_sheet = pygame.image.load(sheet_path)

        # Se obtienen los datos para "recortar" cada sprite de la hoja de sprites.
        sheet_frames_per_row = Configurations.get_alien_frames_per_row()
        sheet_width = alien_sheet.get_width()
        sheet_height = alien_sheet.get_height()
        shot_frame_width = sheet_width // sheet_frames_per_row
        shot_frame_height = sheet_height

        # Se obtiene el tamaño para escalar cada frame.
        alien_frame_size = Configurations.get_alien_size()

        # Se recortan los sprites de la hoja, se escalan y se guardan en la lista de sprites.
        for i in range(sheet_frames_per_row):
            x = i * shot_frame_width
            y = 0
            subsurface_rect = (x, y, shot_frame_width, shot_frame_height)
            frame = alien_sheet.subsurface(subsurface_rect)

            frame = pygame.transform.scale(frame, alien_frame_size)
            frame=pygame.transform.scale(frame,alien_frame_size)

            self._frames.append(frame)

        # Se incluyen los atributos para la animación.
        self._last_update_time = pygame.time.get_ticks()    # Se relaciona con el tiempo de actualización de cada frame.
        self._frame_index = 0                               # Índice de la lista.

        # Se selecciona la primera imagen a mostrar.
        self.image = self._frames[self._frame_index]
        self._frame_index = 1

        self.rect = self.image.get_rect()
        screen_rect=screen.get_rect()
        self.rect.right=screen_rect.right
        self.rect.left=screen_rect.left

        # Se obtiene el rectángulo que representa la posición del sprite.
        #self.rect = self.image.get_rect()

        # Se inicializa la posición inicial, en este caso, se alínea con la pistola del soldado.
        #self.rect.left = 0
        #self.rect.y = 0

        # Se incluyen los atributos para el movimiento.
        self._rect_x = float(self.rect.x)
        self._speed = Configurations.get_alien_speed()

    def alien_position(self):
        #self._rect_x -= self._speed
        self.rect.x += 10
        #self.rect.x = int(self._rect_x)


    def aliens_update_animation(self) -> None:
        """
        Se utiliza para actualizar el frame visible del disparo, dando la impresión de animación.
        """
        # Se verifica si el tiempo transcurrido es mayor o igual al tiempo establecido para actualizar el frame.
        current_time = pygame.time.get_ticks()
        frame_delay = Configurations.get_alien_frame_delay()
        needs_refresh = (current_time - self._last_update_time) >= frame_delay

        if needs_refresh:
            # En caso verdadero, se actualiza el frame por el siguiente en la lista.
            # Además, se actualizan los atributos para resetear el tiempo y actualizar el índice.
            self.image = self._frames[self._frame_index]
            self._last_update_time = current_time
            self._frame_index += 1
            # Finalmente, se verica si el índice ha recorrido todos los frames para volver al inicio de la lista.
            if self._frame_index >= len(self._frames):
                self._frame_index = 0


    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar el soldado en la pantalla.
        :param screen: Pantalla en donde se dibuja el bloque.
        """
        # Se dibuja sobre la pantalla.
        screen.blit(self.image, self.rect)