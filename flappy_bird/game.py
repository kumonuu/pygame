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
game_over = False
pipe_gap = 40

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
        self.click = False
    def update(self):
        global count
        count += 1
        # gravity
        if tapped:
            self.velocity += 0.01
            if self.rect.y < 680:
                self.rect.y += self.velocity

        if game_over == False:
            # add delay for flapping
            if tapped:
                if count > 20: 
                    count = 0
                    self.img_index += 1
                    if self.img_index > 2:
                        self.img_index = 0
                self.image = self.images[self.img_index]
                self.image = pygame.transform.rotate(self.image, -self.velocity*20)
            # jumping
            if pygame.mouse.get_pressed()[0] == True and self.click == False:
                self.velocity = -1.5
                self.click = True
            elif pygame.mouse.get_pressed()[0] == False:
                self.click = False
class PipeSprite(pygame.sprite.Sprite):
    def __init__(self,x,y,direction):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load("flappy_bird/pipe.png")
        self.rect = self.image.get_rect()
        if direction == True:
            self.rect.topleft = (x,y+50)
        else:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft = (x,y-50)
    def update(self):
        pass
    
bird_sprite = BirdSprite(200,HEIGHT/2)


group_bird = pygame.sprite.Group()
group_bird.add(bird_sprite)

group_pipe = pygame.sprite.Group()
group_pipe.add(pipe_sprite)
group_pipe.add(pipe_sprite2)

x = 0
bg = pygame.image.load("flappy_bird/bg.png")
ground = pygame.image.load("flappy_bird/ground.png")

while True:
    screen.blit(bg, (0,0))
    group_pipe.draw(screen)
    group_pipe.update()
    screen.blit(ground, (x,700))

    pipe_height = 50 # replace with random
    pipe_sprite = PipeSprite(400,200,True)
    pipe_sprite2 = PipeSprite(400,200,False)
    
    x -= 1
    if x <= -38:
        x = 0
    group_bird.draw(screen)
    group_bird.update()
    if bird_sprite.rect.y > 680 or bird_sprite.rect.y <= 0:
        game_over = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            tapped = True
    pygame.display.update()