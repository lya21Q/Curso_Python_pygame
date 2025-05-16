import pygame
from pygame.sprite import Sprite
from Configuration import Configurations
from random import randint



#_no_apples=0
class Apple(Sprite):
    _no_apples = 0
    #Tributo de clase pata l aplicacipon.
    #-No_Aplples=0
    def __init__(self):
        super().__init__()
        Apple._no_apples+=1

        self._apple_frames=[]
        apple_block_size = Configurations.get_apple_block_size()
        for i in range(len(Configurations.get_apple_images_path())):
            frame = pygame.image.load(Configurations.get_apple_images_path()[i])
            frame=pygame.transform.scale(frame,(apple_block_size,apple_block_size))
            self._apple_frames.append(frame)



        #self.image = pygame.image.load(Configurations.get_apple_image_path())
        #apple_block_size=Configurations.get_apple_block_size()
        #self.image=pygame.transform.scale(self.image,(apple_block_size,apple_block_size))
        #self.image.fill((Configurations.get_apple_color()))
        #apple_block_size=Configurations.get_apple_block_size()
        #self.rect = self.image.get_rect()
        self._last_update_time=pygame.time.get_ticks()
        self._frame_index=1
        self.image= self._apple_frames[0]

        self.rect = self.image.get_rect()
    def blit(self,screen:pygame.surface.Surface)->None:
        """
        Se utiliza para dibujar la manzana.
        :param screen:
        :return:
        """
        screen.blit(self.image,self.rect)
    def random_positions(self,snake_body:pygame.sprite.Group)->None:
        """
        Se utiliza para inicializar una ubicacion aleatoria d ela manzana
        :return:
        """
        repeat=True
        while repeat :
            #Se genera la posición aleatoria
            screen_width = Configurations.get_screen_size()[0]
            screen_height = Configurations.get_screen_size()[1]
            apple_block_size = Configurations.get_apple_block_size()

            self.rect.x = apple_block_size * randint(0,(screen_width // apple_block_size -1))
            self.rect.y = apple_block_size * randint(0,(screen_height // apple_block_size -1))
            #se verifia que n o se encuentre sobre el cuerpo de la serpiente.
            for snake_block in snake_body.sprites():
                if self.rect== snake_block.rect:
                    repeat = True
                    break
                else:
                    repeat = False
    @classmethod
    def get_no_apples(cls):
        return cls._no_apples

    def animate_apple(self)->None:
        """

        :param cls:
        :return:
        """
        current_time=pygame.time.get_ticks()
        #time_to_refresh=Configurations.get_time_to_refresh_apple_frames()
        time_to_refresh=1000

        needs_refresh= (current_time - self._last_update_time) >= time_to_refresh

        if needs_refresh:
            self.image = self._apple_frames[self._frame_index]

            self._last_update_time = current_time
            self._frame_index += 1

            if self._frame_index >= len(self._apple_frames):
                self._frame_index=0


