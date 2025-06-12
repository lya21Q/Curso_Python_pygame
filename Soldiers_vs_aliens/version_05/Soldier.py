#datacamp.com
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
        self._is_shooting=False

        """LISTA QUE ALMACENA LOS FRAMES DEL SOLDADO"""
        self._frames=[]

        """CAMBIO. Ahora se carga la hoja, en lugar de una única imagen."""
        # Se carga la hoja que contiene los frames del soldado.
        sheet_path = Configurations.get_soldier_sheet_path()
        soldier_sheet = pygame.image.load(sheet_path)

        """NUEVO."""
        # Se obtienen los datos para "recortar" cada sprite de la hoja de sprites.
        sheet_frames_per_row = Configurations.get_frames_per_row()
        sheet_frames_per_columns=Configurations.get_soldier_frame_columns()
        sheet_width = soldier_sheet.get_width()#Anchura
        sheet_height = soldier_sheet.get_height()#Altura
        soldier_frame_width = sheet_width // sheet_frames_per_row
        soldier_frame_height = sheet_height//sheet_frames_per_columns


        # Se obtiene el tamaño para escalar cada frame.
        soldier_frame_size = Configurations.get_soldier_block_size()

        """NUEVO."""
        # Se recortan los sprites de la hoja, se escalan y se guardan en la lista de sprites.
        #for i in range(Configurations.get_soldier_frame_columns()):
            #for j in range(sheet_frames_per_row):
                #x = i * soldier_frame_width
                #y = j * soldier_frame_height
                #subsurface_rect = (x,y, soldier_frame_width, soldier_frame_height)
            #print(soldier_sheet.get_size())
            #frame =soldier_sheet.subsurface(subsurface_rect)
        for j in range(sheet_frames_per_columns):                # CAMBIO. Se agregó este segundo for.
            for i in range(sheet_frames_per_row):
                x = i * soldier_frame_width
                y = j * soldier_frame_height                    # CAMBIO. Aquí es donde se consideran las columnas.
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

        screen_rect=screen.get_rect()
        self.rect.center=screen_rect.center
        self.rect.right=screen_rect.right

        """NUEVO."""
        # Se incluyen los atributos para el movimiento.
        self._rect_y = float(self.rect.y)
        self._speed = Configurations.get_soldier_speed()

    def update_position(self,screen)->None:
        """

        :return:
        """
        # Se obtiene el rectángulo del borde de la pantalla
        screen_rect=screen.get_rect()

        if self.is_moving_up:
            self._rect_y-=self._speed
        elif self.is_moving_down:
            self._rect_y+=self._speed

        # Se verifica que el personaje no sobrepase los bordes de la pantalla.
        if self._rect_y < float(screen_rect.top):
            self._rect_y = float(screen_rect.y)

        elif self._rect_y > (screen_rect.bottom - self.image.get_height()):
            self._rect_y = float(screen_rect.bottom - self.image.get_height())
        # Se actualiza la posición del rectángulo de acuerdo a la posición.
        self.rect.y = int(self._rect_y)

    """NUEVO."""
    def update_animation(self) -> None:
        """
        Se utiliza para actualizar el frame visible del soldado, dando la impresión de animación.
        """
        current_time = pygame.time.get_ticks()
        if self._is_shooting:
            frame_delay=Configurations.get_soldier_frames_delay()
        else:
            frame_delay=Configurations.get_shot_frame_delay()
        needs_refresh=(current_time - self._last_update_time)>=frame_delay
        if needs_refresh:
            self.image = self._frames[self._frame_index]
            self._last_update_time = current_time
            self._frame_index += 1

            """CAMBIO. Se modificó la forma de verificar los índices dependiendo del estado del personaje."""
            sheet_frames_per_row = Configurations.get_frames_per_row()

            if (not self._is_shooting and self._frame_index >= sheet_frames_per_row or
                    self._is_shooting and self._frame_index >= 2 * sheet_frames_per_row):
                self._frame_index = 0

            elif self._is_shooting and self._frame_index == 1:
                self._is_shooting = False



    def shoots(self)->None:
        self._is_shooting=True



    def blit(self,screen:pygame.surface):
        """

        :param screen:
        :return:
        """
        screen.blit(self.image,self.rect)

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