import pygame
from destroyable import Destroyable
import globals
# An object that can move
class Moveable(Destroyable):

    __gravity = 10

    # Constructor that loads the sprite and initializes object variables
    # Requires a location tuple to use as the default location of the object
    # Takes the screen for the sprite to be drawn on
    # Takes the level that the object will be placed in
    # Takes the sprite that will be drawn
    # Takes a health value to pass to the Destroyable class
    # Takes a speed value to calculate movement
    # Takes a weight value to calculate gravity
    def __init__(self, location, screen, level, sprite, health, speed, weight):
        super(Moveable, self).__init__(location, screen, sprite, health)

        self.__level = level

        try:
            # Speed has to be positive to be valid
            if speed >= 0:
                self.__speed = speed
            else:
                raise ValueError("Please enter a valid speed, default speed was set to 0")
        except ValueError as exp:
            self.__speed = 0
            print("Error", exp)

        try:
            # Weight has to be positive to be valid
            if weight >= 0:
                self.__weight = weight
            else:
                raise ValueError("Please enter a valid weight, default weight was set to 1")
        except ValueError as exp:
            self.__weight = 1
            print("Error", exp)

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
    # Gravity is calculated based on the weight
    def move(self, direction = 1):
        try:
            if direction == 1 or direction == -1 or direction == 0:
                spriteX, spriteY = self.getLocation()
                newLocation = (spriteX + (direction * self.__speed), spriteY + (self.__weight * self.__gravity))
                self.setLocation(newLocation)

                # Check to see if there are collisions with level sections and adjust position if so
                collisions = self.__level.collision(self)
                if collisions:
                    spriteWidth, spriteHeight = self.getSize()
                    for collision in collisions:
                        collisionSection = collision.getSection()
                        if collisionSection != globals.BOTTOM_LEFT and collisionSection != globals.BOTTOM_MIDDLE and collisionSection != globals.BOTTOM_RIGHT:
                            collisionX, collisionY = collision.getLocation()
                            if collisionSection == globals.TOP_LEFT or collisionSection == globals.TOP_MIDDLE or collisionSection == globals.TOP_RIGHT:
                                newLocation = (newLocation[0], collisionY - spriteHeight)
                            elif collisionSection == globals.MIDDLE_LEFT:
                                newLocation = (collisionX - spriteWidth, newLocation[1])
                            elif collisionSection == globals.MIDDLE_RIGHT:
                                newLocation = (collisionX + globals.TILE_WIDTH, newLocation[1])
                    self.setLocation(newLocation)
            else:
                raise ValueError("Please enter a valid direction")
        except ValueError as exp:
            print("Error", exp)

    # Move the object up
    def jump(self):
        spriteX, spriteY = self.getLocation()
        newLocation = (spriteX, spriteY - 75)
        self.setLocation(newLocation)

        # Check to see if there are collisions with level sections and adjust position if so
        collisions = self.__level.collision(self)
        if collisions:
            for collision in collisions:
                collisionSection = collision.getSection()
                if collisionSection == globals.BOTTOM_LEFT or collisionSection == globals.BOTTOM_MIDDLE or collisionSection == globals.BOTTOM_RIGHT:
                    collisionX, collisionY = collision.getLocation()
                    newLocation = (newLocation[0], collisionY + globals.TILE_WIDTH - (self.__weight * self.__gravity))
            self.setLocation(newLocation)
