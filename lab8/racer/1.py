import pygame 
import sys
import random
from pygame.locals import *
pygame.init()

fps = 60
FramePerSec = pygame.time.Clock    

#some colors
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)

#screen information
screen_w = 400
screen_h = 600
displaysurf = pygame.display.set_mode((400,600))
displaysurf.fill(white)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        
    def move(self):
        self.rect.move_ip(0,10)
        if(self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30,370),0)
    
    def draw (self,surface):
        surface.blit(self.image,self.rect)
        
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)
        
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
            
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right < screen_w:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5,0)       
    def draw(self,surface):
        surface.blit(self.image, self.rect)  
        
P1  = Player()
E1 = Enemy()  
        

while True:
 for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        P1.update()
        E1.move()
        DISPLAYSURF.fill(WHITE)
         P1.draw(DISPLAYSURF)
         E1.draw(DISPLAYSURF)
         
         pygame.display.update()
         FramePerSec.tick(FPS)