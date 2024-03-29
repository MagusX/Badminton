import pygame
from math import sin, cos, pi
from random import choice
from time import sleep

pygame.init()
game = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()

#attributes
white = ((255,255,255))

#ball obj
x_ball = 500
y_ball = 100
r_ball = 6
v_ball = 2.6
rad = pi/180
ang = choice([180,0])
angle = -ang*rad
vx_ball = cos(angle)*v_ball
vy_ball = sin(angle)*v_ball
grav = 0.042
def get_ball():
    pygame.draw.circle(game, white, (int(float(x_ball)), int(float(y_ball))), r_ball, 0)

#p1 obj
x_p1 = 150
y_p1 = 590
w_p1 = 100
h_p1 = 10
v_p1 = 3
def get_p1():
    pygame.draw.rect(game, white, ((x_p1,y_p1),(w_p1,h_p1)))

#p2 obj
x_p2 = 800
y_p2 = 590
w_p2 = 100
h_p2 = 10
v_p2 = 3
def get_p2():
    pygame.draw.rect(game, white, ((x_p2,y_p2),(w_p2,h_p2)))

#net obj
x_net = 500
y_net = 565
w_net = 10
h_net = 35
def get_net():
    pygame.draw.rect(game, white, ((x_net,y_net),(w_net,h_net)))

def text():
    pygame.font.init()
    font = pygame.font.SysFont('Lucida Console', 15)
    return font

def text2():
    font = pygame.font.SysFont('Lucida Console', 70)
    return font

p1_score = 0
p2_score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    game.fill((0,0,0))

    #text
    my_text = text().render('P1: ' + str(p1_score), False, white)
    my_text2 = text().render('P2: ' + str(p2_score), False, white)
    my_text3 = text2().render('PLAYER 1 WINS!', False, white)
    my_text4 = text2().render('PLAYER 2 WINS!', False, white)

    game.blit(my_text, (1,1))
    game.blit(my_text2, (940, 1))

    keys = pygame.key.get_pressed()
    if p1_score == 12:
        game.blit(my_text3, (200,300))
    elif p2_score == 12:
        game.blit(my_text4, (200,300))
    if keys[pygame.K_ESCAPE]:
        pygame.quit()

    #ball
    get_ball()
    vy_ball += grav
    x_ball += vx_ball
    y_ball += vy_ball

    if x_ball > x_p1 and x_ball < x_p1 + w_p1 and y_ball > y_p1:
        if x_ball > x_p1 and x_ball < x_p1+20:
            vx_ball = cos(-80*rad)*7
            vy_ball = sin(-80*rad)*7
        elif x_ball > x_p1+20 and x_ball < x_p1+40:
            vx_ball = cos(-65 * rad) * 6
            vy_ball = sin(-65 * rad) * 6
        elif x_ball > x_p1+40 and x_ball < x_p1+60:
            vx_ball = cos(-45 * rad) * 5.5
            vy_ball = sin(-45 * rad) * 5.5
        elif x_ball > x_p1+60 and x_ball < x_p1+80:
            vx_ball = cos(-30 * rad) * 5.5
            vy_ball = sin(-30 * rad) * 5.5
        elif x_ball > x_p1+80 and x_ball < x_p1+100:
            vx_ball = cos(-18 * rad) * 5.3
            vy_ball = sin(-18 * rad) * 5.3

    if x_ball > x_p2 and x_ball < x_p2 + w_p2 and y_ball > y_p2 and y_ball < y_p1 + h_p1:
        if x_ball > x_p2 and x_ball < x_p2 + 20:
            vx_ball = cos(-162 * rad) * 5.3
            vy_ball = sin(-162 * rad) * 5.3
        elif x_ball > x_p2 + 20 and x_ball < x_p2 + 40:
            vx_ball = cos(-150 * rad) * 5.5
            vy_ball = sin(-150 * rad) * 5.5
        elif x_ball > x_p2 + 40 and x_ball < x_p2 + 60:
            vx_ball = cos(-135 * rad) * 5.5
            vy_ball = sin(-135 * rad) * 5.5
        elif x_ball > x_p2 + 60 and x_ball < x_p2 + 80:
            vx_ball = cos(-115 * rad) * 6
            vy_ball = sin(-115 * rad) * 6
        elif x_ball > x_p2 + 80 and x_ball < x_p2 + 100:
            vx_ball = cos(-100 * rad) * 7
            vy_ball = sin(-100 * rad) * 7

    if x_ball > x_net and x_ball < x_net + w_net and y_ball > y_net and y_ball <= y_net + h_net:
        if x_ball > x_net and y_ball > y_net:
            p2_score += 1
        elif x_ball < x_net + w_net and y_ball > y_net:
            p1_score += 1

        sleep(0.8)
        x_ball = 500
        y_ball = 100
        angle = -ang * rad
        vx_ball = cos(angle) * v_ball
        vy_ball = sin(angle) * v_ball

    if y_ball > 600 or x_ball > 1000 or x_ball < 0:
        if (x_ball > 0 and x_ball < x_net and y_ball > 600) or (x_ball > 1000):
            p2_score += 1
        elif (x_ball > x_net + w_net and x_ball < 1000 and y_ball > 600) or (x_ball < 0):
            p1_score += 1

        sleep(0.8)
        x_ball = 500
        y_ball = 100
        angle = -ang * rad
        vx_ball = cos(angle) * v_ball
        vy_ball = sin(angle) * v_ball

    #p1
    get_p1()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x_p1 -= v_p1
        if x_p1 <= 0:
            x_p1 = 0
    elif keys[pygame.K_d]:
        x_p1 += v_p1
        if x_p1 + w_p1 >= 500:
            x_p1 = 500 - w_p1

    #p2
    get_p2()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_p2 -= v_p2
        if x_p2 <= 500 + w_net:
            x_p2 = 500 + w_net
    elif keys[pygame.K_RIGHT]:
        x_p2 += v_p2
        if x_p2 + w_p2 >= 1000:
            x_p2 = 1000 - w_p2

    #net
    get_net()

    pygame.display.flip()
    clock.tick(150)
