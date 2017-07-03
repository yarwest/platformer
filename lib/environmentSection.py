import pygame
from drawableObject import DrawableObject
class EnvironmentSection(DrawableObject):

    #
    def __init__(self, location, screen, sprite):
        super(EnvironmentSection, self).__init__(location,screen,sprite)
