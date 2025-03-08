import pygame
import sys

WIDTH = 1000
HEIGHT = 600

# make screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#make title
pygame.display.set_caption("Title")

yellow_shooter = pygame.image.load("space_invaders/Image20250301164334.png")
red_shooter = pygame.image.load("space_invaders/Image20250301164330.png")
bg = pygame.image.load("space_invaders/Image20250301164339.png")

yellow_shooter = pygame.transform.scale(yellow_shooter, (60,60))
yellow_shooter = pygame.transform.rotate(yellow_shooter, 90)
red_shooter = pygame.transform.scale(red_shooter, (60,60))
red_shooter = pygame.transform.rotate(red_shooter, -90)
bg = pygame.transform.scale(bg, (1000,600))

def display_on_screen():
    screen.blit(bg, (0,0))
    screen.blit(yellow_shooter, (yellow_rect.x, yellow_rect.y))
    screen.blit(red_shooter, (red_rect.x, red_rect.y))
    pygame.draw.rect(screen, "black", border)
    for bullet in yellow_bullets:
        pygame.draw.rect(screen, "yellow", bullet)
        bullet.x += 2
    for bullet in red_bullets:
        pygame.draw.rect(screen, "red", bullet)
        bullet.x -= 2

def move_shooter():
    key_press = pygame.key.get_pressed()
    # yellow shooter movement
    if key_press[pygame.K_w] and yellow_rect.y > 0:
        yellow_rect.y -= 1
    elif key_press[pygame.K_s] and yellow_rect.y < HEIGHT - 60:
        yellow_rect.y += 1
    elif key_press[pygame.K_a] and yellow_rect.x > 0:
        yellow_rect.x -= 1
    elif key_press[pygame.K_d] and yellow_rect.x < WIDTH/2 - 60:
        yellow_rect.x += 1
    # red shooter movement
    if key_press[pygame.K_UP] and red_rect.y > 0:
        red_rect.y -= 1
    elif key_press[pygame.K_DOWN] and red_rect.y < HEIGHT - 60:
        red_rect.y += 1
    elif key_press[pygame.K_LEFT] and red_rect.x > WIDTH/2:
        red_rect.x -= 1
    elif key_press[pygame.K_RIGHT] and red_rect.x < WIDTH - 60:
        red_rect.x += 1

def spawn_bullet_yellow():
    global yellow_bullets
    bullet = pygame.rect.Rect(yellow_rect.x+30,yellow_rect.y+30,7,4)
    yellow_bullets.append(bullet)

def spawn_bullet_red():
    global red_bullets
    bullet = pygame.rect.Rect(red_rect.x+30,red_rect.y+30,7,4)
    red_bullets.append(bullet)

yellow_bullets = []
red_bullets = []
border = pygame.rect.Rect(WIDTH/2,0,5,600)
yellow_rect = pygame.rect.Rect(200,250,60,60)
red_rect = pygame.rect.Rect(750,250,60,60)

while True:
    display_on_screen()
    move_shooter()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                spawn_bullet_yellow()
            elif event.key == pygame.K_RSHIFT:
                spawn_bullet_red()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()