import pygame
from moveable import Moveable
class Player(Moveable):
    # The file name for the sprite to be drawn
    __defaultFileName = "sprites/player.png"

    __spriteWidth = 40
    __spriteHeigth = 109

    # Constructor that loads the sprite and initializes player variables
    # Requires a location tuple to use as the default location of the player
    # Takes the screen for the sprite to be drawn on
    def __init__(self, location, screen, environment, health, speed, weight):
        # Initialize the sprite
        self.__sprite = pygame.image.load(self.__defaultFileName)
        self.__sprite = pygame.transform.scale(self.__sprite, (self.__spriteWidth,self.__spriteHeigth)).convert_alpha()

        super(Player, self).__init__(location, screen, environment, self.__sprite, health, speed, weight)
