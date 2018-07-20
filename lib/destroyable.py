import pygame
from drawableObject import DrawableObject
# A drawable object that can die
class Destroyable(DrawableObject):

    # Group of sprites used to detect collision between sprites
    __destroyableSprites = pygame.sprite.Group()

    # Constructor that loads the sprite and initializes Health variable
    # Requires a location tuple to use as the location of the object
    # Takes the screen for the sprite to be drawn on
    def __init__(self, location, screen, sprite, health):
        super(Destroyable, self).__init__(location, screen, sprite)

        # Add destroyable to collision group
        self.__destroyableSprites.add((self))

        try:
            # Health has to be positive to be valid
            if health > 0:
                self.__health = health
            else:
                raise ValueError("Please enter a valid health, default healt was set to 100")
        except ValueError as exp:
            print("Error", exp)
            self.__health = 100

    # Retrieve the current health of the object
    def getHealth(self):
        return self.__health

    # Update the health of the object based on a value
    def updateHealth(self, addition):
        self.__health = self.__health + addition
        if self.__health <= 0:
            self.__health = 0
            self.die()

    # Destroys the object in a fashionable way
    def die(self):
        print "died"
