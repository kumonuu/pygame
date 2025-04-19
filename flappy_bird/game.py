import pygame
import sys

WIDTH = 864
HEIGHT = 768

# make screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))

#make title
pygame.display.set_caption("Flappy Bird")

bird_images = ["flappy_bird/bird1.png", "flappy_bird/bird2.png", "flappy_bird/bird3.png"]
count = 0
tapped = False

class BirdSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for bird_image in bird_images:
            self.images.append(pygame.image.load(bird_image))
        self.img_index = 0
        self.image = self.images[self.img_index]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x,y)
        self.velocity = 0
    def update(self):
        global count
        count += 1
        print("count: ", count) 

        # add delay for flapping
        if tapped:
            if count > 20: 
                count = 0
                self.img_index += 1
                print("index: ", self.img_index)
                if self.img_index > 2:
                    self.img_index = 0
            self.image = self.images[self.img_index]
        
        # gravity
        if tapped:
            self.velocity += 0.01
            if self.rect.y < 680:
                self.rect.y += self.velocity
        # jumping
        if pygame.mouse.get_pressed()[0]:
            self.velocity = -1.5
        
        
bird_sprite = BirdSprite(200,HEIGHT/2)
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
    group.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            tapped = True
    pygame.display.update()