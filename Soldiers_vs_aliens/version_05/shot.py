import pygame
from pygame.sprite import Sprite
from configurations import Configurations

class Shot(Sprite):
    def __init__(self,soldier):
        super().__init__()

        """LISTA QUE ALMACENA LOS FRAMES DEL SOLDADO"""
        self._frames=[]

        """CAMBIO. Ahora se carga la hoja, en lugar de una única imagen."""
        # Se carga la hoja que contiene los frames del soldado.
        sheet_path = Configurations.get_shot_sheet()
        soldier_sheet = pygame.image.load(sheet_path)
        """NUEVO."""
        # Se obtienen los datos para "recortar" cada sprite de la hoja de sprites.
        sheet_frames_per_row = Configurations.get_frames_per_row()
        sheet_width = soldier_sheet.get_width()#Anchura
        sheet_height = soldier_sheet.get_height()#Altura
        soldier_frame_width = sheet_width // sheet_frames_per_row
        soldier_frame_height = sheet_height

        """NUEVO."""
        # Se obtiene el tamaño para escalar cada frame.
        soldier_frame_size = Configurations.get_shot_size()

        """NUEVO."""
        # Se recortan los sprites de la hoja, se escalan y se guardan en la lista de sprites.
        for i in range(sheet_frames_per_row):
            x = i * soldier_frame_width
            y = 0
            subsurface_rect = (x, y, soldier_frame_width, soldier_frame_height)
            frame = soldier_sheet.subsurface(subsurface_rect)

            frame = pygame.transform.scale(frame, soldier_frame_size)

            self._frames.append(frame)

        """NUEVO."""
        # Se incluyen los atributos para la animación.
        self._last_update_time = pygame.time.get_ticks()    # Se relaciona con el tiempo de actualización de cada frame.
        self._frame_index = 0                               # Índice de la lista.

        """NUEVO."""
        # Se selecciona la primera imagen a mostrar.
        self.image = self._frames[self._frame_index]
        self._frame_index = 1

        #Se obtiene el rectangulo que representa la posicion del sprite
        self.rect = self.image.get_rect()

        screen_rect= soldier.rect
        self.rect.right = screen_rect.right-145
        self.rect.centery = screen_rect.centery-10

        self._rect_x=float(self.rect.x)
        self.speed=Configurations.get_shot_speed()

    def shot_animation(self) -> None:
        """
        Se utiliza para actualizar el frame visible del soldado, dando la impresión de animación.
        """
        # Se verifica si el tiempo transcurrido es mayor o igual al tiempo establecido para actualizar el frame.
        current_time = pygame.time.get_ticks()
        frame_delay = Configurations.get_soldier_frames_delay()
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

                self._frame_index = 0
    def update_position(self):
        self.rect.right = self.rect.right-145


    def blit(self,screen:pygame.surface):
        """

        :param screen:
        :return:
        """
        screen.blit(self.image,self.rect)
