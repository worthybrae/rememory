import pygame

def initialize_display(width, height):
    pygame.init()
    return pygame.display.set_mode((width, height))

def set_fullscreen_mode(screen):
    pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.FULLSCREEN)
