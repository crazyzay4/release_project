import pygame


WIDTH = 1000
HEIGH = 600
SIZE = (WIDTH, HEIGH)  
FPS = 60

window = pygame.display.set_mode()
clock = pygame.time.Clock()
background = pygame.transform.scale(pygame.image.load("test_let.png"),SIZE)
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, filename, size, coords):
        self.image = pygame.transform.scale(pygame.image.load(filename),size)
        #self.rect = pygame.Rect(coords, size)
        self.rect = self.image.get_rect()
        self.rect.center = coords

    def reset(self):
        window.blit(self.image, self.rect)

test_object = GameSprite("test_im.png", (100,100), (100,100))



game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    window.blit(background,(0,0))
    test_object.reset()

 

    pygame.display.update()
    clock.tick(FPS)
    

