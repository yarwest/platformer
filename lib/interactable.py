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
    def __init__(self, location, font, screen, sprite):
        sprite = pygame.transform.scale(sprite, (40, 109)).convert_alpha()
        self.__font = font
        self.__location = location
        self.__screen = screen
        super(Interactable, self).__init__(location, screen, sprite)

    # Get interacted with
    # Check script object
    def interact(self):
        print "interacted"
        if self.__interacting:
            self.__interacting = False
        else:
            self.__interacting = True

    # Wrapper around drawable draw method
    # When interacting, the script objects draw method is also called
    def draw(self):
        if self.__interacting:
            print "i'm interacting"
            text = self.__font.render(str("fuck off aight"), 1,(255,255,255))
            self.__screen.blit(text, (self.__location[0], self.__location[1] - 50))
        super(Interactable, self).draw()
