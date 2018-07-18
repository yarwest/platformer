import pygame
import globals
from environmentSection import EnvironmentSection
from cameraController import CameraController
class LevelCreatorMaster(CameraController):

    # function that opens a screen and sets up the level creator
    @classmethod
    def init(cls, screenSize):
        # Init pygame
        pygame.init()

        super(LevelCreatorMaster, cls).init(screenSize, (1024,1024))

        # Set up the screen
        cls.__screen = pygame.display.set_mode(screenSize#, pygame.FULLSCREEN, 16
            )

        cls.__name = None

        cls.__sprites = [
            pygame.image.load("sprites/tiles/gras-dirt/center.png")
        ]

        cls.__sections = [
            EnvironmentSection((64,64),cls.__screen,cls.__sprites[0],globals.CENTER, cls),
            EnvironmentSection((64,128),cls.__screen,cls.__sprites[0],globals.CENTER, cls),
            EnvironmentSection((64,192),cls.__screen,cls.__sprites[0],globals.CENTER, cls),
            EnvironmentSection((64,256),cls.__screen,cls.__sprites[0],globals.CENTER, cls)
        ]

    @classmethod
    def resetCanvas(cls):
        cls.__screen.fill((84, 149, 255))
        for section in cls.__sections:
            section.draw()
        pygame.display.flip()

    @classmethod
    def saveLevel(cls):
        if cls.__name:
            with open("levels/"+cls.__name+".txt", "a+") as file:
                for section in cls.__sections:
                    x,y = section.getLocation()
                    file.write(str(x)+","+str(y)+","+str(section.getSection())+"\n")
        else:
            print "set a name"

    @classmethod
    def setLevelName(cls, name):
        cls.__name = name
