import pygame
from properties import Properties
from player import Player
from environment import Environment
from cameraController import CameraController
from uiElement import UIElement
# Object handling all runtime logic used to play a normal level
class GameMaster(object):

    # Init function that opens a screen
    # also instantiates a level, a player and the UI
    @classmethod
    def init(cls, level, world, levelSize):
        # Init pygame and camera
        pygame.init()

        Properties.init()
        cls.__resolution = Properties.getResolution()
        CameraController.init(cls.__resolution, levelSize)

        cls.__screenWidth = cls.__resolution[0]
        cls.__screenHeight = cls.__resolution[1]

        flags = 0
        if Properties.isFullscreen():
            flags = pygame.FULLSCREEN

        # Set up the screen
        cls.__screen = pygame.display.set_mode(cls.__resolution, flags #, 16
            )

        # Set up font and initialize UI
        cls.__font = pygame.font.Font(None,30)
        cls.__uiElements = []
        cls.__uiElements.append(UIElement((0,0), cls.__font, cls.__screen))

        # Load level
        cls.__environment = Environment(cls.__screen, level, world)

        # Init the player
        cls.__player = Player((130, 500), cls.__screen, cls.__environment, 100, 10, 1)
        cls.__moving = 0

        # Loop until the user clicks the close button.
        cls.__done = False

    # Method that redraws the screen
    @classmethod
    def resetCanvas(cls):
        cls.__screen.fill((84, 149, 255))

        # Move player and update camera accordingly
        cls.__player.move(cls.__moving)
        x, y = cls.__player.getLocation()
        CameraController.setCameraPosition((x-(cls.__screenWidth/2),y-(cls.__screenHeight/2)))

        # Redraw all components
        cls.__environment.draw()
        cls.__player.draw()
        for element in cls.__uiElements:
            element.draw(cls.__player.getHealth())
        pygame.display.flip()


    # -------- Main Program Loop -----------
    @classmethod
    def play(cls):
        while not cls.__done:

            # Always redraw the canvas
            cls.resetCanvas()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Break loop on quit
                    cls.__done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        cls.__done = True
                    # Alter movement based on key input
                    elif event.key == pygame.K_a:
                        cls.__moving = -1
                    elif event.key == pygame.K_d:
                        cls.__moving = 1
                    elif event.key == pygame.K_w or event.key == pygame.K_SPACE:
                        cls.__player.jump()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        # Reset movement
                        cls.__moving = 0
                pygame.display.flip()
