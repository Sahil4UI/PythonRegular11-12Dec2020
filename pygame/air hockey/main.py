import pygame
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
    player1_x= 200
    player1_y=480
    movex1=0
    movey1=0
    player2_x= 200
    player2_y= 50
    green= (0,255,0)
    red= (255,0,0)
    color= (234,208,234)
    blue= (0,0,255)
    player_radius = 25
    ball_radius=15
    ballX=W/2
    ballY=H/2
    
    while True:
        gameScreen.fill(color)
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                quit()
            
        gameScreen.blit(bg,(0,0))
        mouse_coord=pygame.mouse.get_pos()
        
        if (mouse_coord[0] > player_radius and mouse_coord[0] <W-player_radius) and (mouse_coord[1] > H/2+player_radius and mouse_coord[1] <H-player_radius):
            player1_x = mouse_coord[0]
            player1_y = mouse_coord[1]
            
        
    
        player1 = pygame.draw.circle(gameScreen,red,[player1_x,player1_y],player_radius)
        player2 = pygame.draw.circle(gameScreen,green,[player2_x,player2_y],player_radius)
        ball = pygame.draw.circle(gameScreen,blue,[ballX,ballY],ball_radius)
        pygame.display.update()
HomeScreen()
