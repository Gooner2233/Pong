import pygame
import sys
import random
import winsound

def ball_movement():
    #moving the ball
    global speed_x, speed_y
    ball.x+=speed_x
    ball.y+=speed_y

    #handeling collisions
    #colliding against board/goal
    if ball.top<=0 or ball.bottom>=height:
        speed_y*=-1
    if ball.left<=0 or ball.right>=width:
        ball_restart()

    #colliding against paddles
    if ball.colliderect(player1) or ball.colliderect(enemy):
        speed_x*=-1
def player_movement():
    player1.y+=speed_player

    #making sure the pad doesn't exceed the board
    if player1.top<=0:
        player1.top = 0
    if player1.bottom>=height:
        player1.bottom=height
def enemy_AI():
    if enemy.top<ball.y:
        enemy.top+=speed_enemy
    if enemy.bottom>ball.y:
        enemy.bottom-=speed_enemy
    if enemy.top<=0:
        enemy.top = 0
    if enemy.bottom>=height:
        enemy.bottom=height
def ball_restart():
    global speed_x, speed_y
    ball.center=(width/2, height/2)
    speed_x*=random.choice((1, -1))
    speed_y*=random.choice((1, -1))
    winsound.PlaySound("shrek", winsound.SND_ASYNC)
#setup
pygame.init()
clock = pygame.time.Clock()

#creating game window
width = 1280
height = 960
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dagi Ping Pong")
#positioning rectangles and other shapes
ball = pygame.Rect(width/2-15, height/2-15, 30, 30)
player1 = pygame.Rect(width - 20, height/2-70, 10, 140)
enemy = pygame.Rect(10, height/2-70, 10, 140)
board_colour = pygame.Color((43,164,72))
colour1 = (200, 200, 200)

#positioning items in a way as to introduce an element of randomness
speed_x = 7 * random.choice((1, -1))
speed_y = 7 * random.choice((1, -1))
speed_player = 0
speed_enemy = 7
while True:
    #input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                speed_player+=7
            if event.key==pygame.K_UP:
                speed_player-=7
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                speed_player-=7
            if event.key==pygame.K_UP:
                speed_player+=7

    #calling movement functions
    ball_movement()
    player_movement()
    enemy_AI()

    #drawing the board
    screen.fill(board_colour)
    pygame.draw.rect(screen, colour1, player1)
    pygame.draw.rect(screen, colour1, enemy)
    pygame.draw.ellipse(screen, colour1, ball)
    pygame.draw.aaline(screen, colour1, (width/2, 0), (width/2, height))
    #redrawing the board
    pygame.display.flip()
    clock.tick(60)