import pygame
from processing import display, renderer
from generation import random_rectangles, distorted_cube

# Initialize display
pygame.init()
screen = display.initialize_display(800, 600)
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    frame = distorted_cube.generate_frame(800, 600)  # Generate the current frame
    screen.blit(frame, (0, 0))
    pygame.display.flip()

    clock.tick(60)  # 60 FPS

pygame.quit()
