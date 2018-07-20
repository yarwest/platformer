import pygame
from drawableObject import DrawableObject
# A section of the level
class EnvironmentSection(DrawableObject):

    # Constructor that initializes drawable
    # Takes the location of the section within the level
    # Takes the screen for the sprite to be drawn on
    # Takes the sprite to be drawn
    # Takes the section identifier
    def __init__(self, location, screen, sprite, section):
        super(EnvironmentSection, self).__init__(location,screen,sprite)
        self.__section = section

    # Get the section identifier, which is a number indicating the type of section
    def getSection(self):
        return self.__section
