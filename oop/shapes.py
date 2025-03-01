import pygame
import sys

# make screen
screen = pygame.display.set_mode((500, 500))

#make title
pygame.display.set_caption("Title")

class Rectangle:
    def __init__(self, rect_values, color):
        self.rect_values = rect_values
        self.color = color
    def draw(self):
       pygame.draw.rect(screen, self.color, self.rect_values)

class Circle:
    def __init__(self, center, radius, color, width):
        self.radius = radius
        self.color = color
        self.center = center
        self.width = width
    def draw(self):
        pygame.draw.circle(screen, self.color, self.center, self.radius, self.width)
    def grow(self):
        self.radius += 10
        self.draw()

rect = Rectangle((0,0,50,50),"red")
rect2 = Rectangle((100,100,50,100), "green")
rect.draw()
rect2.draw()

circle = Circle((300,300), 50, "yellow", 0)
circle.draw()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            circle.grow()
    pygame.display.update()