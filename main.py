import pygame
import random
import time

WIDTH = 1100
HEIGH = 700
SIZE = (WIDTH, HEIGH)  
FPS = 60

lives = 3
window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
background = pygame.transform.scale(pygame.image.load("la.png"),SIZE)
pygame.font.init()
small_font = pygame.font.Font(None, 30)
big_font = pygame.font.Font(None, 60)
start_time = time.time()
current_time = start_time
enemies = pygame.sprite.Group()
stones = pygame.sprite.Group()
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, filename, size, coords):
        super().__init__()
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
        if self.rect.top >= HEIGH:
            self.rect.y = -300
            self.rect.x = random.randint(100, WIDTH-100)
class Enemy_human(GameSprite):
    def __init__(self, filename, size, coords):
        super().__init__(filename, size, coords)
        self.speed_x = random.randint(2,6)
        self.speed_y = random.randint(2,6)
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.bottom >= HEIGH or self.rect.top <= 0:
            self.speed_y = -self.speed_y
        if self.rect.right >= WIDTH or self.rect.left <= 0:
            self.speed_x = -self.speed_x
            self.image = pygame.transform.flip(self.image, True, False)
        


class Enemy_stone(GameSprite):
    def update(self):
        self.rect.y += 4
        if self.rect.top >= HEIGH:
            self.rect.y = -300
            self.rect.x = random.randint(100, WIDTH-100)

player = Player("mustang.png", (50,100), (550,635))
enemies.add(Enemy_car("enemy_car.png", (50,100), (450,400)))
enemies.add(Enemy_car("enemy_car.png", (50,100), (300,500)))
finish = False

human = Enemy_human("people.walk.png", (30,80), (100,100))
random_number = random.randint(10,100)
timer = 0

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    if not finish:     
        window.blit(background,(0,0))
        player.reset()
        player.update()

        enemies.update()
        enemies.draw(window)

        human.update()
        human.reset()

        stones.update()
        stones.draw(window)

        lives_text = small_font.render("lives: "+ str(lives), True, (255, 255, 255))
        window.blit(lives_text, (0,0))

        if pygame.sprite.spritecollide(player, enemies, True):
            lives -= 2
            enemies.add(Enemy_car("enemy_car.png", (50,100), (random.randint(100,WIDTH-100),0)))

        if pygame.sprite.spritecollide(player, stones, True):
            lives -= 1
            
        if pygame.sprite.collide_rect(player, human):
            finish = True
            text = f"""YOU ARE MURDERER. Your time: {round(new_time-start_time)} seconds"""
            lose_text = big_font.render(text, True, (255,0,0))
            window.blit(lose_text, (WIDTH//4, HEIGH//2))


        if timer == random_number:
            stones.add(Enemy_stone("stone.png", (50, 60), (random.randint(100,WIDTH-100),0)))
            timer = 0
            random_number = random.randint(50,200)
        timer += 1

        new_time = time.time()
        if round(new_time-current_time) >= 1:
            time_text = small_font.render("time: "+ str(round(new_time-start_time)), True, (255, 255, 255))
            window.blit(time_text, (WIDTH-100, 0))


        if lives < 0:
            finish = True
            text = f"""YOU LOSE. Your time: {round(new_time-start_time)} seconds"""
            lose_text = big_font.render(text, True, (0,0,255))
            window.blit(lose_text, (WIDTH//4, HEIGH//2))

        collisions = pygame.sprite.groupcollide(enemies, stones, True, True)

        if collisions:
            for _ in collisions:
                enemies.add(Enemy_car("enemy_car.png", (50,100), (random.randint(100,WIDTH-100),0)))

        if pygame.sprite.spritecollide(human, enemies, False) or \
            pygame.sprite.spritecollide(human, stones, False)  :
            human.kill()
            human = Enemy_human("people.walk.png", (30,80), (100,100))
            


        pygame.display.update()
        clock.tick(FPS)
    

