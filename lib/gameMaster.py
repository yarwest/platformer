import pygame
from player import Player
from environment import Environment
from cameraController import CameraController
class GameMaster(CameraController):

    # Init function that opens a screen, instantiates certain objects, and sets a few variables
    @classmethod
    def init(cls, level, world, screenSize, levelSize):
        # Init pygame
        pygame.init()

        super(GameMaster, cls).init(screenSize, levelSize)

        cls.__screenWidth = screenSize[0]
        cls.__screenHeight = screenSize[1]

        # Set up the screen
        cls.__screen = pygame.display.set_mode(screenSize#, pygame.FULLSCREEN, 16
            )
        cls.__environment = Environment(cls.__screen, level, world)

        # Init the player
        cls.__player = Player((130, 500), cls.__screen, cls.__environment, 100, 10)
        cls.__moving = 0

        # Loop until the user clicks the close button.
        cls.__done = False

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
