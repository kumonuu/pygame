import pygame
import sys
import random

WIDTH = 1000
HEIGHT = 600

pygame.init()

# make screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#make title
pygame.display.set_caption("Match")

names = ["candycrush", "subwaysurfers", "templerun", "ludo"]
font = pygame.font.SysFont("Calibri", 30)
y = 20

for name in names:
    logo = pygame.image.load("match/" + name + ".png")
    screen.blit(logo, (30,y))
    y += 150
y = 20
random.shuffle(names)
for name in names:
    text = font.render(name, True, "white")
    screen.blit(text, (550,y))
    y += 150

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            rect = pygame.rect.Rect(
                pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1],
                5,5
            )
            pygame.draw.rect(screen, "blue", rect)
            print(pygame.mouse.get_pos())
    pygame.display.update()