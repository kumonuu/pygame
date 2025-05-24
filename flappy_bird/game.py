import pygame
import sys
import random
import time

WIDTH = 864
HEIGHT = 768

pygame.init()

# make screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))

#make title
pygame.display.set_caption("Flappy Bird")

font = pygame.font.SysFont("Comic Sans", 30, False, False)
bird_images = ["flappy_bird/bird1.png", "flappy_bird/bird2.png", "flappy_bird/bird3.png"]
count = 0
tapped = False
game_over = False
pipe_gap = 100
pipe_passed = False
score = 0

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
            self.rect.topleft = (x,y+pipe_gap)
        else:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft = (x,y-pipe_gap)
    def update(self):
        self.rect.x -= 1
        if self.rect.x <= -40:
            self.kill()
    
class RestartButtonSprite(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load("flappy_bird/restart.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)
    def draw(self):
        clicked_button = False
        screen.blit(self.image, (self.rect.x,self.rect.y))
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                clicked_button = True
        return clicked_button

def restart():
    global tapped, game_over, score
    tapped = False
    game_over = False
    score = 0
    bird_sprite.x = 200
    bird_sprite.y = HEIGHT/2
    group_pipe.empty()
    print("game restarted")

bird_sprite = BirdSprite(200,HEIGHT/2)
group_bird = pygame.sprite.Group()
group_bird.add(bird_sprite)

group_pipe = pygame.sprite.Group()

restart_button = RestartButtonSprite(WIDTH/2-50,HEIGHT/2-50)

x = 0
bg = pygame.image.load("flappy_bird/bg.png")
ground = pygame.image.load("flappy_bird/ground.png")

start_time = time.time()
while True:
    screen.blit(bg, (0,0))
    group_pipe.draw(screen)
    screen.blit(ground, (x,700))
    score_text = font.render(str(score), False, "black")
    screen.blit(score_text, (750,650))

    if tapped and game_over == False:
        x -= 1
        if x <= -38:
            x = 0
        current_time = time.time()
        if current_time - start_time >= 2:
            random_height = random.randint(-150,150)
            pipe_sprite = PipeSprite(WIDTH,200+random_height,True)
            pipe_sprite2 = PipeSprite(WIDTH,200+random_height,False)

            group_pipe.add(pipe_sprite)
            group_pipe.add(pipe_sprite2)
            start_time = current_time
        group_pipe.update()

    if len(group_pipe) > 0:
        if group_pipe.sprites()[0].rect.left <= group_bird.sprites()[0].rect.left and group_pipe.sprites()[0].rect.right >= group_bird.sprites()[0].rect.right and pipe_passed == False:
            pipe_passed = True
            if pipe_passed:
                score += 1
        if group_pipe.sprites()[0].rect.right < group_bird.sprites()[0].rect.left and pipe_passed == True:
            pipe_passed = False

    if pygame.sprite.groupcollide(group_bird,group_pipe,False,False) or bird_sprite.rect.y > 680 or bird_sprite.rect.y <= 0:
        game_over = True
    
    if game_over == True:
        if restart_button.draw() == True:
            print("restart button drawn")
            restart()
        
    group_bird.draw(screen)
    group_bird.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            tapped = True
    pygame.display.update()