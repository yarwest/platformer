import pygame
from objects.player import Player
from objects.environment import Environment
class GameMaster:

    # Init function that loads the sprite and initializes variables
    @classmethod
    def initGame(cls, level, world, screenSize, levelSize):
        # Init pygame
        pygame.init()

        # Set up the screen
        cls.__screen = pygame.display.set_mode(screenSize#, pygame.FULLSCREEN, 16
            )
        cls.__screenWidth = screenSize[0]
        cls.__screenHeight = screenSize[1]
        cls.__levelWidth = levelSize[0]
        cls.__levelHeight = levelSize[1]
        cls.__environment = Environment(cls.__screen, level, world)

        # Init the player
        cls.__player = Player((130, 580), cls.__screen, 100, 10)
        cls.__moving = 0
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
        cls.__environment.draw()
        cls.__player.move(cls.__moving)
        cls.__player.draw()
        x,y = cls.__player.getLocation()
        cls.setCameraPosition((x-(cls.__screenWidth/2),y-(cls.__screenHeight/2)))
        pygame.display.flip()


    @classmethod
    def play(cls):
        # -------- Main Program Loop -----------
        while not cls.__done:
            cls.resetCanvas()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cls.__done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        cls.__moving = -1
                    elif event.key == pygame.K_d:
                        cls.__moving = 1
                    elif event.key == pygame.K_w or event.key == pygame.K_SPACE:
                        cls.__player.jump()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        cls.__moving = 0
                pygame.display.flip()
