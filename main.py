import pygame


WIDTH = 1100
HEIGH = 700
SIZE = (WIDTH, HEIGH)  
FPS = 60

lives = 3
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

        if keys[pygame.K_a]:
            self.rect.x -= 7

        if keys[pygame.K_d]:
            self.rect.x += 7



class Enemy_car(GameSprite):
    def update(self):
        self.rect.y += 4
       
class Enemy_human(GameSprite):
    def update(self):
        ...


class Enemy_stone(GameSprite):
    def update(self):
        ...

player = Player("mustang.png", (50,100), (550,635))
enemy = Enemy_car("enemy_car.png", (50,100), (450,400))

finish = False

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
if not finish:     
    window.blit(background,(0,0))
    player.reset()
    player.update()
    enemy.reset()
    enemy.update()



    if player.rect.colliderect(enemy.rect):
        lives -= 1
    if lives == 0:
        game_over = True

    pygame.display.update()
    clock.tick(FPS)
    

