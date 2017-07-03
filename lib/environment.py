import pygame
from environmentSection import EnvironmentSection
class Environment():

    __positions = [
        "top-left",
        "top-middle",
        "top-right",
        "middle-left",
        "center",
        "middle-right",
        "bottom-left",
        "bottom-middle",
        "bottom-right",
        "inner-bottom-left",
        "inner-bottom-right",
        "inner-top-left",
        "inner-top-right"
    ]

    # Constructor that loads the sprite and initializes variables
    # Requires a location tuple to use as the default location of the sprite
    # Takes the screen for the sprite to be drawn on
    def __init__(self, screen, levelNo, world):
        self.__screen = screen

        self.__sections = []
        self.__sprites = []

        # Load and adapt the tile images
        for i in range(13):
            self.__sprites.append(pygame.image.load("sprites/tiles/"+world+"/"+self.__positions[i]+".png"))
            #self.__sprites.append(pygame.transform.scale(sprite, (128,128)).convert_alpha())

        with open("levels/"+levelNo+".txt", "r") as file:
            for line in file:
                x,y,section = line.split(",")
                self.__sections.append(EnvironmentSection((int(x),int(y)),self.__screen,self.__sprites[int(section)]))

    # Draw an individual sprite on the set screen and on the set location
    def draw(self):
        from gameMaster import GameMaster
        minX,minY,maxX,maxY = GameMaster.getScreenPosition()
        for section in self.__sections:
            x,y = section.getLocation()
            if x+64 >= minX and y+64 >= minY and x < maxX and y < maxY:
                section.draw()