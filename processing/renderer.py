import pygame

def render_art(screen, art):
    # Here, 'art' might be a surface or some drawable object.
    screen.blit(art, (0, 0))
    pygame.display.flip()
