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
path = 'myfile.txt'
def FileWrite(data,path):
    file = open(path,'w')
    file.write(data)
    file.close()

def ReadFile(path):
    file = open(path,'r')
    data = file.read()
    return data

FileWrite(data,path)
data = ReadFile(path)
data=data.replace('a','x')
FileWrite(data,path)










