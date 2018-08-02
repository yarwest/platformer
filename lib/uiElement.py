import pygame
# Element that is drawn at a static location on a screen
class UIElement(pygame.sprite.Sprite):

    # Create UI element
    # with location within the screen
    # font to display text in
    # screen to display element on
    # (optional) sprite to draw on screen
    def __init__(self, location, font, screen, sprite = None):
        super(UIElement, self).__init__()
        self.__screen = screen
        self.__font = font
        if sprite != None:
            self.__sprite = sprite
        self.__location = location

    # Draw an individual sprite (or text if provided) on the set screen and on the set location
    def draw(self, text = None):
        if text != None:
            text = self.__font.render(str(text), 1,(255,255,255))
            self.__screen.blit(text, self.__location)
        else:
            self.__screen.blit(self.__sprite, self.__location)
