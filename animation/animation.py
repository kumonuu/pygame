import pygame
import sys
import time

pygame.init()

# make screen
screen = pygame.display.set_mode((500, 500))

#make title
pygame.display.set_caption("Title")

image = pygame.image.load("animation\Image20250301161906.jpg")
image2 = pygame.image.load("animation\Image20250301161912.jpg")
image3 = pygame.image.load("animation\Image20250301161916.jpg")
font = pygame.font.SysFont("Times New Roman", 20, True)
text = font.render("Happy Birthday", True, "black")
text2 = font.render("You are now 16 years old", True, "black")
text3 = font.render("Enjoy your present!", True, "black")

image = pygame.transform.scale(image, (500,500))
image2 = pygame.transform.scale(image2, (500,500))
image3 = pygame.transform.scale(image3, (500,500))

while True:
    screen.blit(image, (0,0))
    screen.blit(text, (150, 100))
    pygame.display.update()
    time.sleep(2)
    screen.blit(image2, (0,0))
    screen.blit(text2, (150, 100))
    pygame.display.update()
    time.sleep(2)
    screen.blit(image3, (0,0))
    screen.blit(text3, (150, 250))
    pygame.display.update()
    time.sleep(2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()