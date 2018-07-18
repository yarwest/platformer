import pygame
from destroyable import Destroyable
import globals
class Moveable(Destroyable):

    # Constructor that loads the sprite and initializes player variables
    # Requires a location tuple to use as the default location of the player
    # Takes the screen for the sprite to be drawn on
    def __init__(self, location, screen, environment, sprite, health, speed):
        try:
            super(Moveable, self).__init__(location, screen, sprite, health)

            self.__environment = environment

            # Speed has to be positive to be valid
            if speed >= 0:
                self.__speed = speed
            else:
                raise ValueError("Please enter a valid speed, default speed was set to 0")
        except ValueError as exp:
            print("Error", exp)
            self.__speed = 0

    # Retrieve the current speed of the object
    def getSpeed(self):
        return self.__speed

    # Set the speed of the object
    def setSpeed(self, speed):
        if speed < 0:
            speed = 0
        self.__speed = speed

    # Update the location of the player based on the direction
    # The direction is either a positive or negative 1 which is then multiplied with the objects speed
    # This determines if the object moves forward or backward
    def move(self, direction = 1):
        try:
            if direction == 1 or direction == -1 or direction == 0:
                spriteX, spriteY = self.getLocation()
                newLocation = (spriteX + (direction * self.__speed), spriteY + 15)
                spriteWidth, spriteHeight = self.getSize()
                collisions = self.__environment.collision(self)

                for collision in collisions:
                    collisionSection = collision.getSection()
                    if collisionSection != globals.BOTTOM_LEFT and collisionSection != globals.BOTTOM_MIDDLE and collisionSection != globals.BOTTOM_RIGHT:
                        collisionX, collisionY = collision.getLocation()
                        if collisionSection == globals.TOP_LEFT or collisionSection == globals.TOP_MIDDLE or collisionSection == globals.TOP_RIGHT:
                            newLocation = (newLocation[0], collisionY-spriteHeight)
                        elif collisionSection == globals.MIDDLE_LEFT:
                            newLocation = (collisionX-spriteWidth, newLocation[1])
                        elif collisionSection == globals.MIDDLE_RIGHT:
                            newLocation = (collisionX+globals.TILE_WIDTH, newLocation[1])
                self.setLocation(newLocation)
            else:
                raise ValueError("Please enter a valid direction")
        except ValueError as exp:
            print("Error", exp)

    def jump(self):
        spriteX, spriteY = self.getLocation()
        newLocation = (spriteX,spriteY-50)
        collisions = self.__environment.collision(self)
        for collision in collisions:
            if collision == globals.BOTTOM_LEFT or collision == globals.BOTTOM_MIDDLE or collision == globals.BOTTOM_RIGHT:
                collisionX, collisionY = collision.getLocation()
                newLocation = (newLocation[0], collision.collisionY+globals.TILE_WIDTH)
        self.setLocation(newLocation)
