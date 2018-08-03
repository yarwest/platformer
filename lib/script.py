import pygame
# An object for storing the script for any object that can talk
class Script(object):

    __repeating = False
    __interactions = []
    __currentInteraction = 0
    __currentLine = -1

    def __init__(self, baseLocation, screen, font, repeating, interactions):
        self.__screen = screen
        self.__font = font
        self.__baseLocation = baseLocation
        self.__interactions = interactions
        self.__repeating = repeating

    def nextInteraction(self):
        self.__currentLine = self.__currentLine + 1
        if self.__currentLine == self.__interactions[self.__currentInteraction].__len__():
            self.__currentInteraction = self.__currentInteraction + 1
            if self.__currentInteraction == self.__interactions.__len__():
                if self.__repeating:
                    self.__currentInteraction = 0
                else:
                    self.__currentInteraction = self.__currentInteraction - 1
                self.__currentLine = -1
                return False
            self.__currentLine = 0
        return True

    def draw(self):
        text = self.__font.render(
                str(self.__interactions[self.__currentInteraction][self.__currentLine]),
                1, (255,255,255)
            )
        self.__screen.blit(text, (self.__baseLocation[0], self.__baseLocation[1] - 50))
