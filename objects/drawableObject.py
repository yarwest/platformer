import pygame
class DrawableObject(pygame.sprite.Sprite):

    # Constructor that loads the sprite and initializes variables
    # Requires a location tuple to use as the default location of the sprite
    # Takes the screen for the sprite to be drawn on
    def __init__(self, location, screen, sprite):
        try:
            super(DrawableObject, self).__init__()
            self.__screen = screen
            self.__sprite = sprite

            # Location has to be on the actual screen to be valid
            if location[0] >= 0 and location[1] >= 0:
                self.__location = location
            else:
                raise ValueError("Please enter a valid location, default location was set to (0,0)")
        except ValueError as exp:
            print("Error", exp)
            self.__location = (0,0)

    # Draw an individual sprite on the set screen and on the set location
    def draw(self):
        self.__screen.blit(self.__sprite, self.__location)

    # Retrieve the current location of the object
    def getLocation(self):
        return self.__location

    # Set the location of the object
    def setLocation(self, location):
        self.__location = location
