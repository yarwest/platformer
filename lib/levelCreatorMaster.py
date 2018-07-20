import pygame
import globals
from properties import Properties
from environmentSection import EnvironmentSection
from cameraController import CameraController
# Object handling all runtime logic used to create a level
class LevelCreatorMaster(object):

    # Function that opens a screen and sets up the level creator
    @classmethod
    def init(cls):
        # Init pygame
        pygame.init()

        Properties.init()
        cls.__resolution = Properties.getResolution()
        CameraController.init(cls.__resolution, (1024,1024))

        flags = 0
        if Properties.isFullscreen():
            flags = pygame.FULLSCREEN

        # Set up the screen
        cls.__screen = pygame.display.set_mode(cls.__resolution, flags#, 16
            )

        cls.__name = None

        cls.__sprites = [
            pygame.image.load("sprites/tiles/gras-dirt/center.png")
        ]

        cls.__sections = [
            EnvironmentSection((64,64),cls.__screen,cls.__sprites[0],globals.CENTER),
            EnvironmentSection((64,128),cls.__screen,cls.__sprites[0],globals.CENTER),
            EnvironmentSection((64,192),cls.__screen,cls.__sprites[0],globals.CENTER),
            EnvironmentSection((64,256),cls.__screen,cls.__sprites[0],globals.CENTER)
        ]

    # Method that redraws the screen and all its components
    @classmethod
    def resetCanvas(cls):
        cls.__screen.fill((84, 149, 255))
        for section in cls.__sections:
            section.draw()
        pygame.display.flip()

    # Saving the created level in a structured text file with the level name
    @classmethod
    def saveLevel(cls):
        if cls.__name:
            with open("levels/"+cls.__name+".txt", "a+") as file:
                for section in cls.__sections:
                    x,y = section.getLocation()
                    file.write(str(x)+","+str(y)+","+str(section.getSection())+"\n")
        else:
            print "set a name"

    # Change the name of the level
    @classmethod
    def setLevelName(cls, name):
        cls.__name = name
