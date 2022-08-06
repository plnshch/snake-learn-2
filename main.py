import pygame
import time
import random


pygame.init()

dis_w = 800
dis_h = 600

dis = pygame.display.set_mode((dis_w, dis_h))
pygame.display.update()
pygame.display.set_caption('snake game')

blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 10
score_font = pygame.font.SysFont("comicsansms", 35)
font_style = pygame.font.SysFont(None, 50)


def our_snake(snake_list):
    for c in snake_list:
        pygame.draw.rect(dis, black, [c[0], c[1], snake_block, snake_block])


def score(points):
    value = score_font.render("Your score: " + str(points), True, blue)
    dis.blit(value, [0, 0])


def message(msg, color):
    dis.fill(white)
    m = font_style.render(msg, True, color)
    dis.blit(m, [dis_w / 6, dis_h / 3])


def finish_program():
    pygame.quit()
    quit()


def game_loop():
    game_over = False
    game_close = False
    x1 = dis_w / 2
    y1 = dis_h / 2
    x1_change = 0
    y1_change = 0
    snake_list = []
    snake_len = 1
    food_x = round(random.randrange(0, dis_w - snake_block) / snake_block) * snake_block
    food_y = round(random.randrange(0, dis_h - snake_block) / snake_block) * snake_block

    while not game_over:
        while game_close:
            dis.fill(blue)
            message("You lost! Press C-play again or Q-quit", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finish_program()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        finish_program()
                    if event.key == pygame.K_c:
                        game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                if event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                if event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                if event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        if x1 >= dis_w or x1 < 0 or y1 >= dis_h or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        pygame.draw.rect(dis, green, [food_x, food_y, snake_block, snake_block])

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > snake_len:
            del snake_list[0]

        for c in snake_list[:-1]:
            if c == snake_head:
                game_close = True
        our_snake(snake_list)
        score(snake_len-1)
        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, dis_w - snake_block) / snake_block) * snake_block
            food_y = round(random.randrange(0, dis_h - snake_block) / snake_block) * snake_block
            snake_len += 1

        clock.tick(snake_speed)

    message('you lost' , red)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()


game_loop()
