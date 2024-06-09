import pygame


WIDTH = 1100
HEIGH = 700
SIZE = (WIDTH, HEIGH)  
FPS = 60

window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
background = pygame.transform.scale(pygame.image.load("la.png"),SIZE)
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, filename, size, coords):
        self.image = pygame.transform.scale(pygame.image.load(filename),size)
        #self.rect = pygame.Rect(coords, size)
        self.rect = self.image.get_rect()
        self.rect.center = coords

    def reset(self):
        window.blit(self.image, self.rect)

class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:

            self.rect.y -= 5


class Enemy_car(GameSprite):
    def update(self):
        ...

class Enemy_human(GameSprite):
    def update(self):
        ...

class Enemy_stone(GameSprite):
    def update(self):
        ...

game_object = GameSprite("mustang.png", (60,120), (550,635))
enemy = ("enemy_car.png", (75,130), (450,400))


game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    window.blit(background,(0,0))
    game_object.reset()

 

    pygame.display.update()
    clock.tick(FPS)
    

