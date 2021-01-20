import random
import pygame
import time
from pygame.locals import *
pygame.init()
H= 600
W=800
gameScreen= pygame.display.set_mode((W,H))
color= (255,255,255)
red = (255 , 0 , 0 )
blue  = (0,0,255)
w=30
h=30

pygame.time.set_timer(USEREVENT,1000)

frog=pygame.image.load("frog.png")#raw string-path
frog = pygame.transform.scale(frog,(50,50))


audio = pygame.mixer.Sound("point.wav")
bg = pygame.image.load("bg.jpg")
bg = pygame.transform.scale(bg,(W,H))
def Score(counter):
    font=pygame.font.SysFont(None,30)
    #anti aliasing ->texture-> True
    text=font.render(f"Score : {counter}",True,blue)
    gameScreen.blit(text,(10,10))

def Snake(snakeList):
    for i in snakeList:
        pygame.draw.rect(gameScreen,red,[i[0],i[1],w,h])

def Timer(sec):
    font=pygame.font.SysFont(None,30)
    #anti aliasing ->texture-> True
    text=font.render(f"Time Left : {sec} seconds",True,blue)
    gameScreen.blit(text,(500,10))
def HomeScreen():
    gameScreen.fill(color)
    font=pygame.font.SysFont(None,50)
    #anti aliasing ->texture-> True
    text=font.render(f"PRESS SPACE TO START",True,blue)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type ==pygame.KEYDOWN:    
                if event.key == pygame.K_SPACE:
                    main()
        gameScreen.blit(bg,(0,0))
        gameScreen.blit(text,(W/2-300,H/2))
        
        pygame.display.update()
    
def gameOver():
    font=pygame.font.SysFont(None,50)
    text=font.render(f"***GAME OVER : Press space to restart***",True,blue)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type ==pygame.KEYDOWN:    
                if event.key == pygame.K_SPACE:
                    main()
        gameScreen.blit(text,(W/2-300,H/2))
        pygame.display.update()
            
def main():
    movex = 0
    movey = 0
    frogX = random.randint(0,W-50)
    frogY = random.randint(0,H-50)
    x=0
    y=0
    sec=60
    counter=0
    snakeList= []
    snakeLength=1
    while True:
        gameScreen.fill(color)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            
            elif event.type==pygame.USEREVENT:
                sec-=1
        
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movex=-2
                    movey=0
            
                elif event.key == pygame.K_RIGHT:
                    movex=2
                    movey=0
            
                elif event.key==pygame.K_UP:
                    movey=-2
                    movex=0
            
                elif event.key==pygame.K_DOWN:
                    movey=2
                    movex=0
                
        # gameScreen.blit(image,(imageX,imageY))
        snake = pygame.draw.rect(gameScreen,red,[x,y,w,h])
        
        snakeList.append([x,y])

        Snake(snakeList)
        
        frogRect = pygame.Rect([frogX,frogY,50,50])
        gameScreen.blit(frog,(frogX,frogY))

        x += movex
        y += movey
        
        if x>W-w:
            movex=-2
        elif x<0:
            movex=2
        if y>H-h:
            movey=-2
        elif y<0:
            movey=2
            
        Score(counter)
        Timer(sec)
        
        if sec ==0:
            gameOver()
            
        if snakeLength<len(snakeList):
            del snakeList[0]
            
        for i in snakeList[-2::-1]:
            if i==snakeList[-1]:
                gameOver()
            
        if snake.colliderect(frogRect):
            frogX = random.randint(0,W-50)
            frogY = random.randint(0,H-50)
            counter+=1
            audio.play()
            snakeLength+=20
            
        pygame.display.update()
        
        
HomeScreen()
