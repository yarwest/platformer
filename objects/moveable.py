import pygame
from destroyable import Destroyable
class Moveable(Destroyable):

    # Constructor that loads the sprite and initializes player variables
    # Requires a location tuple to use as the default location of the player
    # Takes the screen for the sprite to be drawn on
    def __init__(self, location, screen, fileName, spriteWidth, spriteHeigth, health, speed):
        try:
            super(Moveable, self).__init__(location, screen, fileName, spriteWidth, spriteHeigth, health)

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
                x, y = self.getLocation()
                self.setLocation((x + (direction * self.__speed), y)) #y+15 for gravity
            else:
                raise ValueError("Please enter a valid direction")
        except ValueError as exp:
            print("Error", exp)

    def jump(self):
        x, y = self.getLocation()
        self.setLocation((x,y-50))
