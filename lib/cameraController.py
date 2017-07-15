import pygame
class CameraController:

    __cameraPosition = (0,0)

    @classmethod
    def init(cls, screenSize, levelSize):
        cls.__screenWidth = screenSize[0]
        cls.__screenHeight = screenSize[1]
        cls.__levelWidth = levelSize[0]
        cls.__levelHeight = levelSize[1]

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
