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
score = 0
y = 20
image_dict = {}
text_dict = {}
score_rect = pygame.rect.Rect(WIDTH/4,20,100,50)

score_text = font.render("Score: " + str(score), True, "white")
screen.blit(score_text, (WIDTH/4, 20))

for name in names:
    logo = pygame.image.load("match/" + name + ".png")
    rect = pygame.rect.Rect(30,y,90,90)
    pygame.draw.rect(screen, "black", rect)
    screen.blit(logo, (30,y))
    image_dict[name] = [rect, False]
    y += 150
y = 20
random.shuffle(names)
for name in names:
    text = font.render(name, True, "white")
    rect_text = pygame.rect.Rect(550,y,30,30)
    pygame.draw.rect(screen, "black", rect_text)
    image_dict[name].append(rect_text)
    screen.blit(text, (550,y))
    text_dict[name] = [rect_text, False]
    y += 150

print(image_dict)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            dot = pygame.rect.Rect(
                pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1],
                6,6
            )
            for k in image_dict:
                if dot.colliderect(image_dict.get(k)[0]) and image_dict.get(k)[1] == False:
                    position = pygame.mouse.get_pos()
                    pygame.draw.rect(screen, "blue", dot)
                    image_dict.get(k)[1] = True
                    image_name = k
                    print(image_dict)
            for k in text_dict:
                if dot.colliderect(text_dict.get(k)[0]) and text_dict.get(k)[1] == False:
                    position2 = pygame.mouse.get_pos()
                    pygame.draw.rect(screen, "blue", dot)
                    pygame.draw.line(screen, "blue", position, position2, 6)
                    text_dict.get(k)[1] = True
                    if k == image_name:
                        score += 1
                        pygame.draw.rect(screen, "black", score_rect)
                        score_text = font.render("Score: " + str(score), True, "white")
                        screen.blit(score_text, (WIDTH/4, 20))
                        print(score)
                    
            print(pygame.mouse.get_pos())
    pygame.display.update()