import pygame
import sys
import math

# make screen
screen = pygame.display.set_mode((500, 500))

#make title
pygame.display.set_caption("Title")

class Polygon:
    def __init__(self, colour, points, width):
        self.points = points
        self.colour = colour
        self.width = width
    def draw(self):
        pygame.draw.polygon(screen, self.colour, self.points, self.width)

def find_point_coordinates(radius, centre, sides):
    coordinates = []
    cx, cy = centre
    for side in range(sides):
        angle = (2 * math.pi * side) / sides
        px = cx + (radius * math.cos(angle))
        py = cy + (radius * math.sin(angle))
        coordinates.append((px,py))
        print(angle)
    return coordinates

triangle = Polygon("white", [(20,20),(178,320),(400,400)], 3)
pentagon = Polygon("red",find_point_coordinates(50,(100,100),5),0)
nonagon = Polygon("blue", find_point_coordinates(40,(200,250),9),0)
#triangle.draw()
pentagon.draw()
nonagon.draw()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()