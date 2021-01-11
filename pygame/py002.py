import pygame
pygame.init()
H= 600
W=800
gameScreen= pygame.display.set_mode((W,H))
color= (255,255,255)
red = (255 , 0 , 0 )
x=0
y=0
w=50
h=50
movex = 0
movey = 0
while True:
    gameScreen.fill(color)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
            # 
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movex=-1
                movey=0
                
            elif event.key == pygame.K_RIGHT:
                movex=1
                movey=0
            
            elif event.key==pygame.K_UP:
                movey=-1
                movex=0
            
            elif event.key==pygame.K_DOWN:
                movey=1
                movex=0
        # pygame.draw.rect(gameScreen,red,[x,y,w,h])
    
    x += movex
    y += movey
    
    if x>W:
        x=25
    elif x<0:
        x=W
    if y>H:
        y = 25
    elif y<0:
        y = H
    
    pygame.draw.rect(gameScreen,red,[x,y,w,h])
    pygame.display.update()
    