import pygame
from environmentSection import EnvironmentSection
import globals
# The level consisting of platforms and such
class Environment(object):

    # Environment sections that require a hitbox
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

    # Types of environment sections
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

    # Constructor that loads the sprites and initializes variables
    # Takes the screen for the sprites to be drawn on
    # Requires a level number to load the set up from a file
    # Requires a world to base all sprites on
    def __init__(self, screen, levelNo, world):
        self.__screen = screen
        self.__sprites = []

        # Load the tile images
        for i in range(13):
            self.__sprites.append(pygame.image.load("sprites/tiles/"+world+"/"+self.__positions[i]+".png"))

        self.__hitboxSection = []
        self.__sections = []

        # Load the actual level composition
        with open("levels/"+levelNo+".txt", "r") as file:
            for line in file:
                sectionX,sectionY,sectionNo = line.split(",")
                sectionNo = int(sectionNo)
                section = EnvironmentSection((int(sectionX),int(sectionY)),self.__screen,self.__sprites[sectionNo],sectionNo)
                if sectionNo in self.__needHitbox:
                    self.__hitboxSection.append(section)
                self.__sections.append(section)

    # Draw all sections
    def draw(self):
        for section in self.__sections:
            section.draw()

    # Function to check if there is any collision between an object and the environment sections
    def collision(self, collider):
        return pygame.sprite.spritecollide(collider, self.__hitboxSection, False)
