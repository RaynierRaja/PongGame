import pygame
from time import sleep

# VARIABLES
WIDTH = 640
HEIGHT = 480
BORDER = 20
FgColour = pygame.Color("Red")
BgColour = pygame.Color("Black")
XVELOCITY = -1
YVELOCITY = -1

# PADDLE CONTROL
class Paddle():
    WIDTH = 10
    HEIGHT = 100
    
    def __init__(self,y):
        self.y = y
    
    def show(self,Colour):
        global BORDER,HEIGHT,WIDTH,Surface
        pygame.draw.rect(Surface,Colour,pygame.Rect(WIDTH-self.WIDTH,self.y-self.HEIGHT//2,self.WIDTH,self.HEIGHT))
    
    def Update(self):
        global BgColour,FgColour
        self.show(BgColour)
        self.y = pygame.mouse.get_pos()[1]
        self.show(FgColour)
        

# BALL CONTROL
class Ball(Paddle):
    RADIUS = 10
    def __init__(self,x,y,vx,vy,paddle):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def show(self,Colour):
        global Surface
        pygame.draw.circle(Surface,Colour,(self.x,self.y),self.RADIUS)
        
    def Update(self):
        global BgColour,FgColour,BORDER,HEIGHT,WIDTH
        self.show(BgColour)
        if self.y == BORDER + self.RADIUS or self.y == HEIGHT-self.RADIUS-BORDER:
            self.vy = -self.vy
        if self.x == BORDER+self.RADIUS:
            self.vx = -self.vx
        if self.x == WIDTH-paddle.WIDTH-self.RADIUS and abs(self.y-paddle.y)<paddle.HEIGHT//2:
            self.vx = -self.vx
            self.vy = -self.vy

        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(FgColour)


# SCREEN
pygame.init()
Surface = pygame.display.set_mode(size=(WIDTH,HEIGHT))
pygame.draw.rect(Surface,FgColour,pygame.Rect(0,0,WIDTH-Paddle.WIDTH,BORDER))
pygame.draw.rect(Surface,FgColour,pygame.Rect(0,0,BORDER,WIDTH))
pygame.draw.rect(Surface,FgColour,pygame.Rect(0,HEIGHT-BORDER,WIDTH-Paddle.WIDTH,BORDER))


paddle = Paddle(HEIGHT//2)
paddle.show(FgColour)

ballplay = Ball(WIDTH//2,HEIGHT//2,XVELOCITY,YVELOCITY,paddle)
ballplay.show(FgColour)


# QUIT
while True:
    e = pygame.event.poll()
    paddle.Update()
    ballplay.Update()
    if e.type == pygame.QUIT:
        break
    pygame.display.flip()
    sleep(0.009)
    

pygame.quit()

