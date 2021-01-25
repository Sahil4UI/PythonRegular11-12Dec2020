import pygame,math
pygame.init()
W= 600
H= 550
blue= (0,0,255)

gameScreen= pygame.display.set_mode((W,H))
bg2= pygame.image.load("bg0.jpg")
bg2= pygame.transform.scale(bg2,(W,H))
bg= pygame.image.load("bgPlay.jpg")
bg= pygame.transform.scale(bg,(W,H))

def HomeScreen():
    font= pygame.font.SysFont(None,60)
    text= font.render(f"Press Space to Start",True,blue)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
            gameScreen.blit(bg2,(0,0))
            gameScreen.blit(text,(W/2- 170, H-70))
            pygame.display.update()

def main():
    player_radius = 25
    player1_x= W/2
    player1_y=480
    movex1=0
    movey1=0
    player2_x= W/2
    player2_y= 70
    green= (0,255,0)
    red= (255,0,0)
    color= (234,208,234)
    blue= (0,0,255)
    ball_radius=15
    ballX=W/2
    ballY=H/2
    mouseX=0
    mouseY=0
    moveX=0
    moveY=0
    while True:
        gameScreen.fill(color)
        for event in pygame.event.get():
            # print(event)
            if event.type== pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEMOTION:
                mouseX,mouseY = pygame.mouse.get_pos()
            
        gameScreen.blit(bg,(0,0))
        
        if (mouseX > player_radius and mouseX <W-player_radius) and (mouseY > H/2 and mouseY <H-player_radius):
            player1_x =mouseX
            player1_y = mouseY
            
        #mousepos = pygame.mouse.get_pos()
        #print(mousepos)

        player1 = pygame.draw.circle(gameScreen,red,[player1_x,player1_y],player_radius)
        player2 = pygame.draw.circle(gameScreen,green,[player2_x,player2_y],player_radius)
        ball = pygame.draw.circle(gameScreen,blue,[ballX,ballY],ball_radius)
        d1 = math.dist((player1.x,player1.y),(ball.x,ball.y))
        if d1<=40:
            if ballY<player1.y and ballX<player1.x:
                moveY=-1
                moveX=-1
            elif ballY<player1.y and ballX>player1.x:
                moveY=-1
                moveX=1

            elif ballY>player1.y and ballX>player1.x:
                moveY=1
                moveX=1
                
            elif ballY>player1.y and ballX<player1.x:
                moveY=1
                moveX=-1
            elif ballY==player1.Y and ballY>player1.y:
                moveY= 1
                moveX=0


        ballX+=moveX
        ballY+=moveY

        if ballX<ball_radius:
            moveX+=1
        elif ballX>W:
            moveX-=1
        if ballY<ball_radius:
            moveY=1
        elif ballY>H:
            moveY=-1
            
        
        pygame.display.update()

HomeScreen()
