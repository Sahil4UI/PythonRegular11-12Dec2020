import pygame
pygame.init()

H= 600
W=800
gameScreen= pygame.display.set_mode((W,H))
color= (255,255,255)
red = (255 , 0 , 0 )
x=0
y=0
movex = 1
movey = 1
while True:
    gameScreen.fill(color)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        # pygame.draw.rect(gameScreen,red,[x,y,w,h])
    x+=movex
    y+=movey
    
    if x>W-100:
        movex = -1
    elif x<0:
        movex =1
    
    if y>H-100:
        movey = -1
    elif y<0:
        movey =1
    
    
    pygame.draw.rect(gameScreen,red,[x,y,100,100])
    pygame.display.update()
    