import pygame
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

        # Loop until the user clicks the close button.
        cls.__done = False

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
        pygame.display.flip()

    @classmethod
    def play(cls):
        # -------- Main Program Loop -----------
        while not cls.__done:
            cls.resetCanvas()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cls.__done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print "mouse click"
                elif event.type == pygame.KEYDOWN:
                    print "key down"
                elif event.type == pygame.KEYUP:
                    print "key up"
                pygame.display.flip()
