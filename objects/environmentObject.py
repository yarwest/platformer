import pygame
class EnvironmentObject(pygame.sprite.Sprite):

    # Constructor that loads the sprite and initializes variables
    # Requires a location tuple to use as the default location of the sprite
    # Takes the screen for the sprite to be drawn on
    def __init__(self, location, screen, section):
        try:
            super(EnvironmentObject, self).__init__()
            self.__screen = screen

            self.section = section

            # Location has to be on the actual screen to be valid
            x, y = self.__screen.get_size()
            if location[0] >= 0 and location[1] >= 0 and location[0] < x and location[1] < y:
                self.__location = location
            else:
                raise ValueError("Please enter a valid location, default location was set to (0,0)")
        except ValueError as exp:
            print("Error", exp)
            self.__location = (0,0)

    # Draw an individual sprite on the set screen and on the set location
    def draw(self, sprite):
        self.__screen.blit(sprite, self.__location)

    # Retrieve the current location of the object
    def getLocation(self):
        return self.__location

    # Set the location of the object
    # Requires a tuple of which the x-location value has to be on the screen
    # Whenever the x-location of the player is outside of the screen, the value is set to the edge
    def setLocation(self, location):
        x, y = self.__screen.get_size()
        if location[0] < 75:
            location = (75,location[1])
        elif location[0] > x-self.__spriteWidth-75:
            location = (x-self.__spriteWidth-75,location[1])
        self.__location = location
