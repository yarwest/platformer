import pygame
class InterfaceController(pygame.sprite.Sprite):

    __fileName = "../sprites/interface.png"

    # Constructor that loads the sprite and initializes variables
    # Takes the screen for the sprite to be drawn on
    def __init__(self, screen):
        super(Object, self).__init__()
        self.__screen = screen

        # Initialize the sprite
        self.__sprite = pygame.image.load(__fileName)
        self.__sprite = pygame.transform.scale(self.__sprite, (self.__screen.get_width(),self.__screen.get_height())).convert_alpha()

    # Draw an individual sprite on the set screen and on the set location
    def draw(self):
        self.__screen.blit(self.__sprite, self.__location)
