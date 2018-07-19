import pygame
class UIElement(pygame.sprite.Sprite):

    def __init__(self, location, font, screen, sprite = None):
        super(UIElement, self).__init__()
        self.__screen = screen
        self.__font = font
        if sprite != None:
            self.__sprite = sprite
        self.__location = location

    # Draw an individual sprite on the set screen and on the set location
    def draw(self, text = None):
        if text != None:
            text = self.__font.render(str(text), 1,(255,255,255))
            self.__screen.blit(text, self.__location)
        else:
            self.__screen.blit(self.__sprite, self.__location)
