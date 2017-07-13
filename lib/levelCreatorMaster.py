import pygame
import globals
from environmentSection import EnvironmentSection
class LevelCreatorMaster:

    # function that opens a screen and sets up the level creator
    @classmethod
    def initCreator(cls, screenSize):
        # Init pygame
        pygame.init()

        # Set up the screen
        cls.__screen = pygame.display.set_mode(screenSize#, pygame.FULLSCREEN, 16
            )
        cls.__screenWidth = screenSize[0]
        cls.__screenHeight = screenSize[1]
        cls.__levelWidth = 1024
        cls.__levelHeight = 1024

        cls.__cameraPosition = (0,0)
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

    @classmethod
    def getLevelSize(cls):
        return (cls.__levelWidth,cls.__levelHeight)

    @classmethod
    def getCameraPosition(cls):
        return cls.__cameraPosition

    @classmethod
    def setCameraPosition(cls, position):
        maxX = cls.__levelWidth-cls.__screenWidth
        maxY = cls.__levelHeight-cls.__screenHeight
        if position[0] < 0:
            position = (0,position[1])
        elif position[0] > maxX:
            position = (maxX,position[1])
        if position[1] < 0:
            position = (position[0],0)
        elif position[1] > maxY:
            position = (position[0],maxY)
        cls.__cameraPosition = position

    @classmethod
    def getScreenPosition(cls):
        x,y = cls.__cameraPosition
        return [x,y,x+cls.__screenWidth,y+cls.__screenHeight]

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
                    x,y = section.getSection()
                    file.write(str(x)+","+str(y)+","+str(section.getLocation())+"\n")
        else:
            print "set a name"

    @classmethod
    def setLevelName(cls, name):
        cls.__name = name
