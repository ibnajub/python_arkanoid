import pygame
from random import randrange

RES = 1024
SIZE = 50

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
# запрет движения самого на себя
keys_prohibition = {'W': True, 'A': True, 'S': True, 'D': True, }

lenght = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 5
score = 0

pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
img = pygame.image.load('wallpaper_snake.jpg').convert()

while True:
    sc.blit(img, (0, 0))
    # sc.fill(pygame.Color('black'))
    # drawing snake, apple
    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, SIZE - 2, SIZE - 2))) for i, j in snake]
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))
    
    # show score
    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    sc.blit(render_score, (5, 5))
    
    # snake movement
    x += dx * SIZE
    y += dy * SIZE
    
    snake.append((x, y))
    snake = snake[-lenght:]
    # eating apple
    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        lenght += 1
        fps += 1
        score += 1
    
    # game over
    if (x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE  # over display
            or len(snake) != len(set(snake))):  # eating yoself
        # break
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
            sc.blit(render_end, (RES // 2 - 200, RES // 3))
            pygame.display.flip()
            # exit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
    
    # reload surfase
    pygame.display.flip()
    clock.tick(fps)
    
    # exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    # control
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and keys_prohibition['W']:
        dx, dy = 0, -1
        keys_prohibition = {'W': True, 'A': True, 'S': False, 'D': True, }
    if key[pygame.K_DOWN] and keys_prohibition['S']:
        dx, dy = 0, 1
        keys_prohibition = {'W': False, 'A': True, 'S': True, 'D': True, }
    if key[pygame.K_LEFT] and keys_prohibition['A']:
        dx, dy = -1, 0
        keys_prohibition = {'W': True, 'A': True, 'S': True, 'D': False, }
    if key[pygame.K_RIGHT] and keys_prohibition['D']:
        dx, dy = 1, 0
        keys_prohibition = {'W': True, 'A': False, 'S': True, 'D': True, }
