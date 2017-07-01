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
    def __init__(self, location, screen, health, speed):
        super(Player, self).__init__(location, screen, self.__defaultFileName, self.__spriteWidth, self.__spriteHeigth, health, speed)
        self.__screen = screen
