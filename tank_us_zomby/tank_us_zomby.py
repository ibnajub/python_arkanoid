import random
import pgzrun
# import random

from pgzero.actor import Actor
from pgzero.clock import clock
# from pgzero.game import screen
from pgzero.keyboard import keyboard
from pgzero.loaders import sounds

TITLE = "Zombies vs Tanks"
WIDTH = 800
HEIGHT = 640

UP = 180
DOWN = 0
LEFT = 270
RIGHT = 90
BULLET_SPEED = 10
ZOMBIE_SPEED = 1
SCORE = 0
blue_tank = Actor('tank_blue.png')
blue_tank.x = WIDTH / 2
blue_tank.y = WIDTH / 2

GAME_OVER = False
bullet = Actor("bulletblue.png")
bullet_fired = False
bullet_start_angle = None

zomby_list = []


def shoot_bullet():
    global bullet_fired, bullet_start_angle
    if bullet_fired:
        if bullet_start_angle == None:
            bullet_start_angle = blue_tank.angle
        
        if bullet_start_angle == LEFT:
            bullet.x -= BULLET_SPEED
        elif bullet_start_angle == RIGHT:
            bullet.x += BULLET_SPEED
        elif bullet_start_angle == DOWN:
            bullet.y += BULLET_SPEED
        elif bullet_start_angle == UP:
            bullet.y -= BULLET_SPEED
        if bullet.x >= WIDTH or bullet.x <= 0 or bullet.y >= HEIGHT or bullet.y <= 0:
            bullet_fired = False
            bullet_start_angle = None


def create_zombies():
    if len(zomby_list) < 5:
        loc_rand = random.randint(0, 3)
        z = Actor("zombie_stand.png")
        if loc_rand == 0:
            z.x = 1
            z.y = random.randint(40, HEIGHT - 40)
        elif loc_rand == 1:
            z.x = WIDTH - 1
            z.y = random.randint(40, HEIGHT - 40)
        elif loc_rand == 2:
            z.x = 1
            z.y = random.randint(40, WIDTH - 40)
        elif loc_rand == 3:
            z.x = HEIGHT - 1
            z.y = random.randint(40, WIDTH - 40)
        zomby_list.append(z)


def move_zombies():
    global SCORE, GAME_OVER
    for zomb in zomby_list:
        if zomb.x < blue_tank.x:
            zomb.x += ZOMBIE_SPEED
        elif zomb.x > blue_tank.x:
            zomb.x -= ZOMBIE_SPEED
        elif zomb.y < blue_tank.y:
            zomb.y += ZOMBIE_SPEED
        elif zomb.y > blue_tank.y:
            zomb.y -= ZOMBIE_SPEED
        zomb.draw()
        if zomb.colliderect(bullet):
            zomby_list.remove(zomb)
            SCORE += 1
        elif zomb.colliderect(blue_tank):
            # SCORE = 0
            GAME_OVER = True


def draw():
    if not GAME_OVER:
        screen.blit("tank.png", (0, 0))
        blue_tank.draw()
        if bullet_fired:
            bullet.draw()
        clock.schedule(shoot_bullet, 5)
        clock.schedule(create_zombies, 2)
        move_zombies()
        screen.draw.text(f'score:{SCORE}', (350, 150))
    else:
        screen.fill("blue")
        screen.draw.text(f'GAME OVER, score:{SCORE}', (350, 150))


def start_game():
    global GAME_OVER, zomby_list, SCORE
    GAME_OVER = False
    zomby_list = []
    SCORE = 0


def update():
    global bullet_fired
    if keyboard.left:
        blue_tank.x -= 5
        blue_tank.angle = LEFT
    elif keyboard.right:
        blue_tank.x += 5
        blue_tank.angle = RIGHT
    if keyboard.up:
        blue_tank.y -= 5
        blue_tank.angle = UP
    elif keyboard.down:
        blue_tank.y += 5
        blue_tank.angle = DOWN
    if keyboard.space:
        if not bullet_fired:
            bullet_fired = True
            # sounds.sounds_laserretro_004.play()
            if blue_tank.angle == LEFT:
                bullet.x = blue_tank.x - 30
                bullet.y = blue_tank.y
            elif blue_tank.angle == RIGHT:
                bullet.x = blue_tank.x + 30
                bullet.y = blue_tank.y
            elif blue_tank.angle == UP:
                bullet.x = blue_tank.x
                bullet.y = blue_tank.y - 30
            elif blue_tank.angle == DOWN:
                bullet.x = blue_tank.x
                bullet.y = blue_tank.y + 30
    elif keyboard.s:
        start_game()


pgzrun.go()
