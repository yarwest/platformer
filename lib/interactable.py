import pygame
from drawableObject import DrawableObject
# A drawable object that can be interacted with by a player
class Interactable(DrawableObject):

    __interacting = False

    # Constructor
    # font to display text in
    # Requires a location tuple to use as the location of the object
    # Takes the screen for the sprite to be drawn on
    # Sprite to be loaded and drawn
    def __init__(self, location, script, screen, sprite):
        sprite = pygame.transform.scale(sprite, (40, 109)).convert_alpha()
        self.__script = script
        self.__location = location
        self.__screen = screen
        super(Interactable, self).__init__(location, screen, sprite)

    # Get interacted with
    # Check script object
    def interact(self):
        self.__interacting = self.__script.nextInteraction()

    # Wrapper around drawable draw method
    # When interacting, the script objects draw method is also called
    def draw(self):
        if self.__interacting:
            self.__script.draw()
        super(Interactable, self).draw()
