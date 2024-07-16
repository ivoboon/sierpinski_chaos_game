import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame
import math
import random

# Initialising PyGame
pygame.init()

# Triangle coordinates
ax = 0
ay = 0
bx = 1000
by = 0
cx = bx / 2
cy = math.sqrt((bx - ax) ** 2 - cx ** 2)
A = (ax, ay)
B = (bx, by)
C = (cx, cy)

# Making surface
surface = pygame.display.set_mode((bx, cy))
pygame.display.set_caption('Sierpiński Triangle Chaos Game')

def random_triangle(vert1, vert2, vert3):
    """
    returns a uniformly distributed random point on a triangle
    """
    x, y = random.random(), random.random()
    q = abs(x - y)
    s, t, u = q, 0.5 * (x + y - q), 1 - 0.5 * (q + x + y)
    return (int(s * vert1[0] + t * vert2[0] + u * vert3[0]), int(s * vert1[1] + t * vert2[1] + u * vert3[1]))

# Making initial surface
background_colour = (0, 0, 0)
triangle_line_colour = (255, 0, 0)
triangle_line_width = 3
point_colour = (0, 255, 0)
new_line_colour = (255, 255, 0)
initial_point_colour = (255, 0, 0)
initial_point_radius = 5
current_point = random_triangle(A, B, C)

surface.fill(background_colour)
pygame.draw.line(surface, triangle_line_colour, A, B, triangle_line_width)
pygame.draw.line(surface, triangle_line_colour, A, C, triangle_line_width)
pygame.draw.line(surface, triangle_line_colour, B, C, triangle_line_width)
pygame.draw.circle(surface, initial_point_colour, current_point, initial_point_radius)
pygame.display.flip()

def Sierpiński(xy, A, B, C):
    random_list = ['a', 'b', 'c']
    target = random.choice(random_list)
    if target == 'a':
        x = (xy[0] + A[0]) / 2
        y = (xy[1] + A[1]) / 2
    elif target == 'b':
        x = (xy[0] + B[0]) / 2
        y = (xy[1] + B[1]) / 2
    else:
        x = (xy[0] + C[0]) / 2
        y = (xy[1] + C[1]) / 2
    return (int(x), int(y))


# PyGame loop
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    new_point = Sierpiński(current_point, A, B, C)
    surface.set_at(new_point, point_colour)
    current_point = new_point
    
    pygame.display.flip()