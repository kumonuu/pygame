import pygame
import sys

WIDTH = 306
HEIGHT = 388

# make screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#make title
pygame.display.set_caption("Bulb")

bulb_off = pygame.image.load("bulb/bulb_off.jpg")
bulb_on = pygame.image.load("bulb/bulb_on.jpg")

while True:
    for event in pygame.event.get():
        screen.blit(bulb_off, (0,0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.blit(bulb_on, (0,0))
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()