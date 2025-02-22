import pygame
import sys

# make screen
screen = pygame.display.set_mode((500, 500))

#make title
pygame.display.set_caption("Title")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()