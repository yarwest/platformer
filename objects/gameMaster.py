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
        cls.__levelWidth = levelSize[0]
        cls.__levelHeight = levelSize[1]
        cls.__environment = Environment(cls.__screen, level, world)

        # Init the player
        cls.__player = Player((130, 580), cls.__screen, 100, 10)
        cls.__moving = 0

        # Loop until the user clicks the close button.
        cls.__done = False

    @classmethod
    def getLevelSize(cls):
        return (cls.__levelWidth,cls.__levelHeight)

    @classmethod
    def resetCanvas(cls):
        cls.__screen.fill((84, 149, 255))
        cls.__environment.draw()
        cls.__player.move(cls.__moving)
        cls.__player.draw()
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
