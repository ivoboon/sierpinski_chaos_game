import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame
import math
import random

def random_triangle(vert1, vert2, vert3):
    """
    returns a uniformly distributed random point on a triangle
    """
    x, y = random.random(), random.random()
    q = abs(x - y)
    s, t, u = q, 0.5 * (x + y - q), 1 - 0.5 * (q + x + y)
    return (int(s * vert1[0] + t * vert2[0] + u * vert3[0]), int(s * vert1[1] + t * vert2[1] + u * vert3[1]))


def Sierpiński(xy, A, B, C):
    """
    Chooses a vertex randomly and returns the coordinate halfway between the input coordinate and the vertex's
    """
    random_list = ['a', 'b', 'c']
    target = random.choice(random_list)
    if target == 'a':
        x = (xy[0] + A[0]) / 2
        y = (xy[1] + A[1]) / 2
        target = A
    elif target == 'b':
        x = (xy[0] + B[0]) / 2
        y = (xy[1] + B[1]) / 2
        target = B
    else:
        x = (xy[0] + C[0]) / 2
        y = (xy[1] + C[1]) / 2
        target = C
    return (int(x), int(y)), target

def main():
    """
    Main function
    """
    # Input variables
    target_fps = 60
    background_colour = (0, 0, 0)
    triangle_line_colour = (255, 0, 0)
    triangle_line_width = 3
    point_colour = (0, 255, 0)
    new_line_colour = (255, 255, 0)
    new_point_colour = (255, 0, 255)
    new_point_radius = 5

    # Triangle coordinates
    ax = 0
    ay = 0
    bx = 1000
    by = 0
    cx = bx / 2
    cy = math.sqrt((bx - ax) ** 2 - cx ** 2)

    # Flip coordinates because coordinate system is flipped in PyGame
    A = (bx - ax, cy - ay)
    B = (bx - bx, cy - by)
    C = (bx - cx, cy - cy)

    # Making screen and surfaces
    pygame.init()
    screen = pygame.display.set_mode((bx, cy))
    pygame.display.set_caption('Sierpiński Triangle Chaos Game')
    points_surface = pygame.Surface((bx, cy))
    lines_surface = pygame.Surface((bx, cy), pygame.SRCALPHA)

    # Generating a random starting point
    current_point = random_triangle(A, B, C)

    # Drawing the outer triangle
    points_surface.fill(background_colour)
    pygame.draw.line(points_surface, triangle_line_colour, A, B, triangle_line_width)
    pygame.draw.line(points_surface, triangle_line_colour, A, C, triangle_line_width)
    pygame.draw.line(points_surface, triangle_line_colour, B, C, triangle_line_width)

    # PyGame loop
    run = True

    while run:
        # Quit PyGame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Removing previously drawn elements
        lines_surface.fill((0, 0, 0, 0))

        # Retrieves information about the new point and its target vertex
        new_point, target = Sierpiński(current_point, A, B, C)

        # Draws the target point, and draws a line from the current point to the target, with circles at each point
        points_surface.set_at(new_point, point_colour)
        pygame.draw.aaline(lines_surface, new_line_colour, current_point, target)
        pygame.draw.circle(lines_surface, new_point_colour, current_point, new_point_radius)
        pygame.draw.circle(lines_surface, new_point_colour, target, new_point_radius)
        pygame.draw.circle(lines_surface, new_point_colour, new_point, new_point_radius)
        current_point = new_point
        
    	# Copy surfaces onto screen, and update screen
        screen.blit(points_surface, (0, 0))
        screen.blit(lines_surface, (0, 0))
        pygame.display.flip()

        # Changes fps
        pygame.time.Clock().tick(target_fps)


if __name__ == "__main__":
    main()