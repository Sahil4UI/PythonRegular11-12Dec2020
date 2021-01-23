#access modes - read(r),write(w),append(a) , readbytes(rb) ,writebytes(wb), appendbytes(ab)

data = ''' 
import pygame
#pygame initialization
pygame.init()
H = 600
W = 800
gameScreen = pygame.display.set_mode((W,H))
red = (255,0,0)#rgb color coding
gameScreen.fill(red)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
'''

file = open("mydata.txt",'w')
file.write(data)
file.close()
