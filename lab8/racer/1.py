import pygame 
import sys
import random, time

from pygame.locals import *
pygame.init()

fps = 60
FramePerSec = pygame.time.Clock()    

#some colors
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)


#screen information
screen_w = 400
screen_h = 600
SPEED = 7
score = 0
#setting up fonts
font = pygame.font.SysFont("Verdana",60)
font_small = pygame.font.SysFont("Verdana",20)
game_over = font.render("Game Over", True, black)
background = pygame.image.load("street.png")
pygame.mixer.init()
pygame.mixer.music.set_volume(0.45) 
pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(loops = 10**9)

pygame.display.set_caption('GAME')


displaysurf = pygame.display.set_mode((400,600))
displaysurf.fill(white)
pygame.display.set_caption("Game")

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.set_random_position() 
    
    def move(self):
        self.rect.move_ip(0,3)
        if self.rect.top > screen_h:
            self.set_random_position()
            

    def draw(self,surface):
        surface.blit(self.image, self.rect)     
    
    def set_random_position(self):
        self.rect.center = (random.randint(65,screen_w - 65),0)
        self.rect.bottom = 0  
        

        

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,screen_h - 40),0)
        
    def move(self):
        self.rect.move_ip(0,10)
        if(self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30,370),0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)  # displaying the player
    

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)  #defines a starting position for the Rect
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
            
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.left > 0:  #ensure that the player isn’t able to move off screen.
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5,0)       
    def draw(self, surface):
        surface.blit(self.image, self.rect)  # displaying the player
        
P1 = Player()
E1 = Enemy()
C1 = Coin()
#Creating sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

coins = pygame.sprite.Group()
coins.add(C1)


#adding a new user event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED,1000)

def generated_new_coin():
    global coin
    coin = Coin()
    coins.add(coin)
    all_sprites.add(coin)
    
captured_coins = 0
while True:     
    for event in pygame.event.get():    
        if event.type == INC_SPEED:
            SPEED += 1         
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    displaysurf.blit(background,(0,0))
    
    
    displaysurf.blit(
        font_small.render(f'Score: {score}', True, blue), (293, 10)
    )  # displaying total score

    displaysurf.blit(
        font_small.render(f'Coins: {captured_coins}', True, blue), (293, 30)
        
    )  # displaying number of touched coins


    
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        displaysurf.blit(entity.image,entity.rect)
        entity.move()
        
    for sprite in all_sprites:
        sprite.move()  # moving and displaying all sprites
        sprite.draw(displaysurf)

    if pygame.sprite.spritecollideany(P1, coins):  # if player get coin
        Coin.kill()  # coin disappear
        captured_coins += 1  # variable of number of touched coins
        score += 1  # for touching a coin player get one point
        generated_new_coin()  # new coin will appear

    

        displaysurf.fill((69, 172, 116))  # unique green color on a backgroung
        displaysurf.blit(game_over, (12, 190))  # displaying message that game over
        displaysurf.blit(font_small.render(f'Your score: {score}', True, white), (15, 270))  # display score
        displaysurf.blit(font_small.render(f'Captured coins: {captured_coins}', True, white),
                    (15, 290))  # display number of touched coins

        pygame.display.update()  # updating the screen for showing game over page
    #to be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
        displaysurf.fill(red)
        displaysurf.blit(game_over,(30,250))
        pygame.display.update()
        
        for entity in all_sprites:
            entity.kill()
        time.sleep(3)
        pygame.quit()
        sys.exit()
    pygame.display.update()
    FramePerSec.tick(fps)