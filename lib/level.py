import pygame
from .environment import Environment
# The level with all objects in it
class Level(object):

    def __init__(self, screen, levelNo, world):
        self.__screen = screen
        self.__environment = Environment(screen, levelNo, world)

        # Load the actual level composition
        with open("levels/"+levelNo+".txt", "r") as file:
            for line in file:
                properties = line.split(",")
                if properties[0] == "section":
                    self.__environment.appendSection(*properties[1:])


    def draw(self):
        self.__environment.draw()

    def collision(self, collider):
        return self.__environment.collision(collider)
