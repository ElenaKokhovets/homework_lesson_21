import pygame, random

pygame.init()
dis = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Змейка')

score = 0
# snake_size = 10
snake_list = []
snake_len = 1

x1 = 400  # текущие коорд змейки
y1 = 250  # текущие коорд змейки

x1_change = 0
y1_change = 0

# max координаты приложения
x_max = pygame.display.get_window_size()[0]
y_max = pygame.display.get_window_size()[1]

# координаты яблока
x_apple = random.randrange(0, x_max, 10)
y_apple = random.randrange(60, y_max, 10)

# цвета
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
black = (0, 0, 0)

# шрифт для счёта
Impact = pygame.font.SysFont('Impact', 26)

game_over = False
clock = pygame.time.Clock()


def draw_snake (snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, blue, [x[0], x[1], 10, 10])


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:  # вопрос нажата ли кнопка?
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            if event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            if event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            if event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10
    if x1 >= pygame.display.get_window_size()[0] \
            or y1 >= pygame.display.get_window_size()[1] \
            or x1 <= 0 \
            or y1 <= 60:
        game_over = True
    x1 += x1_change
    y1 += y1_change

    dis.fill(white)


    pygame.draw.rect(dis, blue, (x1, y1, 10, 10))
    pygame.draw.rect(dis, red, [x_apple, y_apple, 10, 10])
    snake_head=[]
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    if len(snake_list) > snake_len:
        del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_head:
            game_over = True
    draw_snake(snake_list)
    pygame.display.update()

    pygame.draw.rect(dis, green, (0, 0, 800, 50))
    text_score = Impact.render(f'Счёт игры :   {score}', 0, black)
    dis.blit(text_score, (10, 10)) # счёт игры
    pygame.display.update()  # обновление экрана

    if x1 == x_apple and y1 == y_apple:
        score += 1
        print('Змейка проглотила яблоко')
        print('Счёт игры :', score)
        snake_len +=1
        x_apple = random.randrange(0, x_max, 10)
        y_apple = random.randrange(60, y_max, 10)
    clock.tick(10)

pygame = quit()
quit()

# Добавить счетчик
# Сделать так, чтобы змея увеличивалась
# Если змея съест свой хвост, то игра закончится
# По желанию: добавить вступительную заставку
# По желанию: добавить музыку
