import pygame
from math import *
pygame.init()


m = 100
n = 50

degToRad = pi/180
# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

def IK (xf, yf):
    try:
        d2 = xf*xf + yf*yf
        d = sqrt(d2)
        mycos = (d2 - m*m - n*n)/ (-2*m*n)
        alfa = 2*pi - acos(mycos)
        beta = asin(n*sin(2*pi - alfa)/d)
        theta = acos(yf/d) - beta
    except ValueError:
        theta = 0
        alfa = 0
        print('ValueError')
    return theta, alfa - pi

def circle(x, y):
    # Draw a solid blue circle in the center
    xt = x + 250
    yt = (- y + 250)
    pygame.draw.circle(screen, (0, 0, 255), (xt, yt), 5)

def line(x0, y0, x1, y1):
    xt0 = x0 + 250
    yt0 = (- y0 + 250)
    xt1 = x1 + 250
    yt1 = (- y1 + 250)
    pygame.draw.line(screen, (0, 0, 0), (xt0, yt0), (xt1, yt1), width= 5)

# Run until the user asks to quit
    
def drawFK(theta, alfa):
    x1 = m*sin(theta)
    y1 = m*cos(theta)

    xf = x1 + n*sin(theta+ alfa)
    yf = y1 + n*cos(theta+ alfa)

    line(0,0, x1, y1)
    line(x1, y1, xf, yf)
    circle(xf,yf)
    


running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))
    circle(0,0)

    xmouse, ymouse = pygame.mouse.get_pos()
    xmouse = xmouse - 250
    ymouse = (- ymouse + 250)

    circle(xmouse, ymouse)
    theta, alfa = IK(xmouse, ymouse)
    drawFK(theta, alfa)

    # Flip the display
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()