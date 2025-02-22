import pygame
import sys

# make screen
screen = pygame.display.set_mode((500, 500))

#make title
pygame.display.set_caption("Title")

class Rectangle:
    def __init__(self, rect_values, colour):
        self.rect_values = rect_values
        self.colour = colour
    def draw(self):
       pygame.draw.rect(screen, self.colour, self.rect_values)

class Circle: #TODO: homework
    pass

rect = Rectangle((0,0,50,50),"red")
rect2 = Rectangle((100,100,50,100), "green")
rect.draw()
rect2.draw()

pygame.draw.circle(screen, "white", (200,200),30, width=2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
    pygame.display.update()