import random

import pgzrun
import pgzero
# from pgzero import keyboard
# from pgzero import keyboard

from pgzero.actor import Actor

TITLE = "Arkanoid clone"
WIDTH = 800
HEIGHT = 500

paddle = Actor("paddleblue.png")
paddle.x = 220
paddle.y = 420

ball = Actor("ballblue.png")
ball.x = 30
ball.y = 300
ball_x_speed = 3
ball_y_speed = 3
barr_list = []


def draw_bar(bar_x, bar_y, quantity, pict):
    for i in range(quantity):
        bar = Actor(pict)
        bar.x = bar_x
        bar.y = bar_y
        barr_list.append(bar)
        bar_x += 70


def draw_block_list():
    barr_list.clear()
    block_x = 100
    block_y = 100
    block_len = 8
    block_list = ["element_red_rectangle_glossy.png", "element_blue_rectangle_glossy.png",
                  "element_green_rectangle_glossy.png"]
    for pic in block_list:
        draw_bar(block_x, block_y, block_len, pic)
        block_y += 50
        block_x += 70
        block_len -= 2


def update_ball():
    global ball_x_speed, ball_y_speed
    ball.x -= ball_x_speed
    ball.y -= ball_y_speed
    if (ball.x >= WIDTH) or (ball.x <= 0):
        ball_x_speed *= -1
    if (ball.y >= HEIGHT):
        # ball_y_speed *= -1
        draw_block_list()
    elif (ball.y <= 0):
        ball_y_speed *= -1


def draw():
    screen.blit("background.png", (0, 0))
    paddle.draw()
    for bar in barr_list:
        bar.draw()
    ball.draw()


def update():
    global ball_x_speed, ball_y_speed
    if keyboard.left and paddle.x > 0:
        paddle.x -= 5
    elif keyboard.right and paddle.x < WIDTH:
        paddle.x += 5
    update_ball()
    if ball.colliderect(paddle):
        ball_y_speed *= -1
        ball_x_speed *= -1 if (random.randint(0, 1)) else 1
    else:
        for bar in barr_list:
            if ball.colliderect(bar):
                barr_list.remove(bar)
                ball_y_speed *= -1
                ball_x_speed *= -1 if (random.randint(0, 1)) else 1


draw_block_list()
pgzrun.go()

# if __name__ == '__main__':
