import pygame
from objects.player import Player
from objects.environment import Environment
class GameMaster():

    # Constructor that loads the sprite and initializes variables
    # Requires a location tuple to use as the default location of the sprite
    # Takes the screen for the sprite to be drawn on
    @staticmethod
    def __init__(self, level, world, screenSize, levelSize):
        # Init pygame
        pygame.init()

        # Set up the screen
        self.__screen = pygame.display.set_mode(screenSize#, pygame.FULLSCREEN, 16
            )
        self.__levelWidth = levelSize[0]
        self.__levelHeight = levelSize[1]
        self.__environment = Environment(self.__screen, level, world)

        # Init the player
        self.__player = Player((130, 580), self.__screen, 100, 10)
        self.__moving = 0

        # Loop until the user clicks the close button.
        self.__done = False


    @staticmethod
    def getLevelSize():
        return (self.__levelWidth,self.__levelHeight)

    def resetCanvas():
        self.__screen.fill((84, 149, 255))
        self.__environment.draw()
        self.__player.move(moving)
        self.__player.draw()
        pygame.display.flip()


    @staticmethod
    def play():

        # -------- Main Program Loop -----------
        while not done:
            self.resetCanvas()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.__moving = -1
                    elif event.key == pygame.K_d:
                        self.__moving = 1
                    elif event.key == pygame.K_w or event.key == pygame.K_SPACE:
                        self.__player.jump()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        self.__moving = 0
                pygame.display.flip()
