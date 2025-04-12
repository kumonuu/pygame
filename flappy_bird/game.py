import pygame
import sys

WIDTH = 864
HEIGHT = 768

# make screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))

#make title
pygame.display.set_caption("Flappy Bird")

class BirdSprite (pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("flappy_bird/bird1.png")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x,y)

bird_sprite = BirdSprite(50,HEIGHT/2)
group = pygame.sprite.Group()
group.add(bird_sprite)

x = 0
bg = pygame.image.load("flappy_bird/bg.png")
ground = pygame.image.load("flappy_bird/ground.png")

while True:
    screen.blit(bg, (0,0))
    screen.blit(ground, (x,700))
    x -= 1
    if x <= -38:
        x = 0
    group.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()