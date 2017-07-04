import pygame
from drawableObject import DrawableObject
class EnvironmentSection(DrawableObject):

    #
    def __init__(self, location, screen, sprite, section):
        super(EnvironmentSection, self).__init__(location,screen,sprite)
        self.__section = section

    def getSection(self):
        return self.__section
