import pygame
from moveable import Moveable
class Player(Moveable):
    # The file name for the sprite to be drawn
    __defaultFileName = "sprites/player.png"
    #__attackFileName = "sprites/playerAttack.png"
    __spriteWidth = 81
    __spriteHeigth = 220

    # Constructor that loads the sprite and initializes player variables
    # Requires a location tuple to use as the default location of the player
    # Takes the screen for the sprite to be drawn on
    def __init__(self, location, screen, health, speed):
        super(Player, self).__init__(location, screen, self.__defaultFileName, self.__spriteWidth, self.__spriteHeigth, health, speed)
        self.__screen = screen

        # Initialize the sprites
        #self.__sprite = pygame.image.load(self.__attackFileName)
        #self.__sprite = pygame.transform.scale(self.__sprite, (self.__spriteWidth,self.__spriteHeigth)).convert_alpha()

    # Checks if this object collides with another destroyable that is not himself
    # Updates health of destroyable when colliding
    def attack(self):
        collisions = self.collision(self)
        for collision in collisions:
            if collision != self:
                collision.updateHealth(-10)
