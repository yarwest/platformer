import pygame
from environmentSection import EnvironmentSection
import globals
class Environment(object):

    __needHitbox = [
        globals.TOP_LEFT,
        globals.TOP_MIDDLE,
        globals.TOP_RIGHT,
        globals.MIDDLE_LEFT,
        globals.MIDDLE_RIGHT,
        globals.BOTTOM_LEFT,
        globals.BOTTOM_MIDDLE,
        globals.BOTTOM_RIGHT
    ]

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
        self.__sprites = []

        # Load and adapt the tile images
        for i in range(13):
            self.__sprites.append(pygame.image.load("sprites/tiles/"+world+"/"+self.__positions[i]+".png"))

        self.__hitboxSection = []
        self.__sections = []

        with open("levels/"+levelNo+".txt", "r") as file:
            for line in file:
                sectionX,sectionY,sectionNo = line.split(",")
                sectionNo = int(sectionNo)
                section = EnvironmentSection((int(sectionX),int(sectionY)),self.__screen,self.__sprites[sectionNo],sectionNo)
                if sectionNo in self.__needHitbox:
                    self.__hitboxSection.append(section)
                self.__sections.append(section)

    # Draw an individual sprite on the set screen and on the set location
    def draw(self):
        for section in self.__sections:
            section.draw()

    # Function to check if there is any collision between an object and the sprite collection
    def collision(self, collider):
        return pygame.sprite.spritecollide(collider, self.__hitboxSection, False)
