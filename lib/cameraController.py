import pygame
# Object that controls the sizing and position of the view
class CameraController(object):

    # Default camera position
    __cameraPosition = (0,0)

    # Initialize and set size of camera and size of total level
    @classmethod
    def init(cls, screenSize, levelSize):
        cls.__screenWidth = screenSize[0]
        cls.__screenHeight = screenSize[1]
        cls.__levelWidth = levelSize[0]
        cls.__levelHeight = levelSize[1]

    # Retrieve total level size
    @classmethod
    def getLevelSize(cls):
        return (cls.__levelWidth, cls.__levelHeight)

    # Get current camera position
    @classmethod
    def getCameraPosition(cls):
        return cls.__cameraPosition

    # Set camera position to new position
    # Level sizing limits the camera movement
    @classmethod
    def setCameraPosition(cls, position):
        maxX = cls.__levelWidth - cls.__screenWidth
        maxY = cls.__levelHeight - cls.__screenHeight
        if position[0] < 0:
            position = (0, position[1])
        elif position[0] > maxX:
            position = (maxX, position[1])
        if position[1] < 0:
            position = (position[0], 0)
        elif position[1] > maxY:
            position = (position[0], maxY)
        cls.__cameraPosition = position

    # Get the position of the camera based on the 4 corners
    @classmethod
    def getScreenPosition(cls):
        x,y = cls.__cameraPosition
        return [x, y, x + cls.__screenWidth, y + cls.__screenHeight]
