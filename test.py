import pygame
import sys
import math

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Cube Rotation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define vertices of a cube
cube_position = [WIDTH // 2, HEIGHT // 2, 0]
side_length = 100
vertices = [
    [-side_length, -side_length, -side_length],
    [-side_length, -side_length, side_length],
    [-side_length, side_length, -side_length],
    [-side_length, side_length, side_length],
    [side_length, -side_length, -side_length],
    [side_length, -side_length, side_length],
    [side_length, side_length, -side_length],
    [side_length, side_length, side_length]
]

edges = [
    (0, 1),
    (0, 2),
    (0, 4),
    (1, 3),
    (1, 5),
    (2, 3),
    (2, 6),
    (3, 7),
    (4, 5),
    (4, 6),
    (5, 7),
    (6, 7)
]

angle = 0

def transform_3d_to_2d(x, y, z):
    """Simple perspective projection."""
    scale = 500 / (z + 500)
    return (int(x * scale + cube_position[0]), int(y * scale + cube_position[1]))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    # Rotation matrices
    rotation_x = [
        [1, 0, 0],
        [0, math.cos(angle), -math.sin(angle)],
        [0, math.sin(angle), math.cos(angle)]
    ]

    rotation_y = [
        [math.cos(angle), 0, -math.sin(angle)],
        [0, 1, 0],
        [math.sin(angle), 0, math.cos(angle)]
    ]

    rotated_vertices = []
    for vertex in vertices:
        # Rotate around X, then Y
        temp_vertex = [
            rotation_x[0][0] * vertex[0] + rotation_x[0][1] * vertex[1] + rotation_x[0][2] * vertex[2],
            rotation_x[1][0] * vertex[0] + rotation_x[1][1] * vertex[1] + rotation_x[1][2] * vertex[2],
            rotation_x[2][0] * vertex[0] + rotation_x[2][1] * vertex[1] + rotation_x[2][2] * vertex[2]
        ]

        rotated_vertex = [
            rotation_y[0][0] * temp_vertex[0] + rotation_y[0][1] * temp_vertex[1] + rotation_y[0][2] * temp_vertex[2],
            rotation_y[1][0] * temp_vertex[0] + rotation_y[1][1] * temp_vertex[1] + rotation_y[1][2] * temp_vertex[2],
            rotation_y[2][0] * temp_vertex[0] + rotation_y[2][1] * temp_vertex[1] + rotation_y[2][2] * temp_vertex[2]
        ]

        rotated_vertices.append(rotated_vertex)

    # Draw edges
    for edge in edges:
        pygame.draw.line(screen, WHITE, transform_3d_to_2d(*rotated_vertices[edge[0]]), transform_3d_to_2d(*rotated_vertices[edge[1]]))

    pygame.display.flip()
    pygame.time.wait(16)

    angle += 0.02
