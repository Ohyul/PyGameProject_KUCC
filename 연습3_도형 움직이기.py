from pygame import *
from pygame.locals import *

BLACK = (0,0,0)
GRAY = (127,127,127)
WHITE = (255,255,255)

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

YELLOW = (255,255,0)
CYAN = (0,255,255)
C1_BLUE=(153,204,255)
C1_GREEN=(204,255,204)

size=width,height = 700,500
screen = display.set_mode(size)
bgColor=C1_BLUE
screen.fill(bgColor)

pos1=[0,0,100,70]
draw.rect(screen,BLUE, pos1)
display.update()

clock = time.Clock()

init()
distance =10

running=True
while running:
    clock.tick(60)
    for p_event in event.get():
        if p_event.type == QUIT:
            running=False
        if p_event.type==KEYDOWN:
            if p_event.key==K_ESCAPE:
                running=False
    event.pump()
    keys=key.get_pressed()
    
    if keys[ord('s')]:
        if pos1[1] > height - pos1[3]:
            pos1[1] = height - pos1[3]
        else:
            pos1[1] += distance
    elif keys[ord('w')]:
        if pos1[1] < 0:
            pos1[1] =0
        else:
            pos1[1] -= distance
    
    elif keys[ord('a')]:
        if pos1[0] < 0:
            pos1[0] =0
        else:
            pos1[0] -= distance
    
    elif keys[ord('d')]:
        if pos1[0] > width-pos1[2]:
            pos1[0] =width-pos1[2]
        else:
            pos1[0] += distance
            
    screen.fill(bgColor)
    draw.rect(screen, BLUE, pos1)
    display.update()
    
quit()