import pygame
class DrawableObject(pygame.sprite.Sprite):

    # Constructor that loads the sprite and initializes variables
    # Requires a location tuple to use as the default location of the sprite
    # Takes the screen for the sprite to be drawn on
    def __init__(self, location, screen, sprite):
        try:
            super(DrawableObject, self).__init__()
            from gameMaster import GameMaster
            self.__screen = screen
            self.__sprite = sprite

            # Location has to be in the actual level to be valid
            x,y = GameMaster.getLevelSize()
            if location[0] >= 0 and location[1] >= 0 and location[0] < x and location[1] < y:
                self.__location = location
            else:
                raise ValueError("Please enter a valid location, default location was set to (0,0)")
        except ValueError as exp:
            print("Error", exp)
            self.__location = (0,0)

    # Draw an individual sprite on the set screen and on the set location
    def draw(self):
        from gameMaster import GameMaster
        x,y = self.__location
        cameraX, cameraY = GameMaster.getCameraPosition()
        self.__screen.blit(self.__sprite, (x-cameraX, y-cameraY))

    # Retrieve the current location of the object
    def getLocation(self):
        return self.__location

    # Set the location of the object
    def setLocation(self, location):
        from gameMaster import GameMaster
        x = GameMaster.getLevelSize()[0]
        if location[0] < 0:
            location = (0,location[1])
        elif location[0] > x-self.__sprite.get_size()[0]:
            location = (x-self.__sprite.get_size()[0],location[1])
        self.__location = location
