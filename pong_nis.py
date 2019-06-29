import pygame
import random
import sys
pygame.init()
#defining colors
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
#co-ordinates
size=(700,500)
height=500
width=700
#right pad 
right=200
#left pad
left=200
bal_x=(int)(width/2)
bal_y=(int)(height/2)
clk=pygame.time.Clock()
xspeed=5
yspeed=0
padspeed=4
#creating game window
x=pygame.display.set_mode(size)

#game caption
pygame.display.set_caption('pong')
##r1=pygame.draw.rect(x,black,[0,200,10,100])
ball = pygame.draw.circle(x,red,[bal_x,bal_y],20)
pad1=pygame.draw.rect(x,white,[10,left,10,100])
pad2=pygame.draw.rect(x,white,[680,right,10,100])

score_r=0
score_l=0
game=True
right_paddle_up=0
right_paddle_down=0
left_paddle_up=0
left_paddle_down=0
clock=pygame.time.Clock()
def printscore(msg,m,n): 
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(str(msg), True, white, black) 
    textRect = text.get_rect()   
    textRect.center = (m,n)
    x.blit(text, textRect) 
  


win=""

##pygame.display.update()
while game:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
        #looking for the key that is pressed
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                right_paddle_up=1
            if event.key==pygame.K_DOWN:
                right_paddle_down=1
            if event.key==pygame.K_w:
                left_paddle_up=1
            if event.key==pygame.K_s:
                left_paddle_down=1
        #checking if key pressed is removed
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                right_paddle_up=0
            if event.key==pygame.K_DOWN:
                right_paddle_down=0
            if event.key==pygame.K_w:
                left_paddle_up=0
            if event.key==pygame.K_s:
                left_paddle_down=0
            
        
    clock.tick(60)   
        
    #moving the ball along the x-axis
    bal_x+=xspeed
    if(bal_x>=pad2.x-10 and pad2.y<bal_y<(pad2.y+100)):
        xspeed=-5
        yspeed=random.randint(-3,3)
        
    if(bal_x<=pad1.x+20 and pad1.y<bal_y<(pad1.y+100) ):
        xspeed=5
        yspeed=random.randint(-3,3)
    if bal_x>700:
        bal_x=350
        bal_y=250
        score_l+=1
        xspeed=-5
    if bal_x<0:
        bal_x=350
        bal_y=250
        score_r+=1
        xspeed=5
        print(score_r)
        
    if(score_r>9):
        win=1
        break
    if(score_l>9):
        win=0
        break
        
    #moving the ball along y axis
    bal_y+=yspeed
    if bal_y<10 or bal_y>height-10:
        yspeed=-yspeed
    
    #controlling movement of paddles:
        #if flag is set to 1 and the position of paddle is within screen
    if right_paddle_up==1 and right>0:
        right-=padspeed

    if right_paddle_down==1 and right<(height-100):
        right+=padspeed
        
    if left_paddle_up==1 and left>0:
        left-=padspeed
    if left_paddle_down==1 and left<(height-100):
        left+=padspeed

    x.fill(black)
    printscore(score_r,525,50)
    printscore(score_l,175,50)
    #to draw a line
    pygame.draw.line(x,white,(350,0),(350,500),5)
    #drawing circle
    ball = pygame.draw.circle(x,red,[bal_x,bal_y],10)
    #drawing rectangles
    pad1=pygame.draw.rect(x,white,[10,left,10,100])
    pad2=pygame.draw.rect(x,white,[680,right,10,100])
    pygame.display.update()
    
x.fill(black)
if(win==1):
    printscore("player 1 wins",350,250)
else:
    printscore("player 2 wins",350,250)
pygame.display.update()   
                
            
             
        
            
           
    
