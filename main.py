import pygame
import random
import time

# Dimensiunile ferestrei
WIDTH = 800
HEIGHT = 600
sc = 0

# Dimensiunile și viteza inițială a șarpelui
SNAKE_SIZE = 20
SNAKE_HEAD_SIZE = 30  # Size of the snake head (slightly larger than body)

# Inițializare Pygame
pygame.init()

# Inițializare ecran
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
# Inițializare font
fonts = pygame.font.Font('font/pixelated.ttf', 30)
# Inițializare culoare text



clock = pygame.time.Clock()

# Încărcarea imaginii fructului
apple_image = pygame.image.load('images/fruit.png')
apple_image = pygame.transform.scale(apple_image, (SNAKE_SIZE * 2, SNAKE_SIZE * 2))
banana_image = pygame.image.load('images/banana.png')
banana_image = pygame.transform.scale(banana_image, (SNAKE_SIZE * 2, SNAKE_SIZE * 2))
orange_image = pygame.image.load('images/orange.png')
orange_image = pygame.transform.scale(orange_image, (SNAKE_SIZE * 2, SNAKE_SIZE * 2))
pear_image = pygame.image.load('images/pear.png')
pear_image = pygame.transform.scale(pear_image, (SNAKE_SIZE * 2, SNAKE_SIZE * 2))
melon_image = pygame.image.load('images/melon.png')
melon_image = pygame.transform.scale(melon_image, (SNAKE_SIZE * 2, SNAKE_SIZE * 2))
peach_image = pygame.image.load('images/peach.png')
peach_image = pygame.transform.scale(peach_image, (SNAKE_SIZE * 2, SNAKE_SIZE * 2))
cherry_image = pygame.image.load('images/cherry.png')
cherry_image = pygame.transform.scale(cherry_image, (SNAKE_SIZE * 2, SNAKE_SIZE * 2))
plum_image = pygame.image.load('images/plum.png')
plum_image = pygame.transform.scale(plum_image, (SNAKE_SIZE * 2, SNAKE_SIZE * 2))
snake_body_image = pygame.image.load('images/snake-body.png')
snake_body_image = pygame.transform.scale(snake_body_image, (SNAKE_SIZE, SNAKE_SIZE))
snake_head_image = pygame.image.load('images/head.png')
snake_head_image = pygame.transform.scale(snake_head_image, (SNAKE_HEAD_SIZE, SNAKE_HEAD_SIZE))

# Încărcarea imaginii de fundal
background = pygame.image.load('images/background.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))


# Rularea jocului
def start_menu():

    SNAKE_S = 0
    background = pygame.image.load('images/start.png')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    screen.blit(background, (0, 0))

    font = pygame.font.Font('font/pixelated.ttf', 40)
    text = font.render("SLOW          MEDIUM          FAST", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT - 100))

    text2 = font.render("Press S     Press M     Press F" , True, (255, 255, 255))
    text_rect2 = text.get_rect(center=(WIDTH - 430, HEIGHT - 160))
    screen.blit(text, text_rect)
    screen.blit(text2, text_rect2)



    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    SNAKE_S = 3
                if event.key == pygame.K_f:
                    SNAKE_S = 9
                if event.key == pygame.K_m:
                    SNAKE_S = 5

        if SNAKE_S == 3:
            game(SNAKE_S)
        if SNAKE_S == 9:
            game(SNAKE_S)
        if SNAKE_S == 5:
            game(SNAKE_S)

        clock.tick(60)


# Funcția principală a jocului
def game(SNAKE_SPEED):

    global sc
    # Poziția inițială a șarpelui
    snake_x = WIDTH // 2
    snake_y = HEIGHT // 2

    # Direcția inițială a șarpelui
    direction_x = 0
    direction_y = 0

    # Coordonatele fructului
    apple_x = random.randint(20, WIDTH -  2 * SNAKE_SIZE)
    apple_y = random.randint(20, HEIGHT - 2 * SNAKE_SIZE)
    banana_x = random.randint(20, WIDTH -  2 * SNAKE_SIZE)
    banana_y = random.randint(20, HEIGHT - 2 * SNAKE_SIZE)
    orange_x = random.randint(20, WIDTH -  2 * SNAKE_SIZE)
    orange_y = random.randint(20, HEIGHT - 2 * SNAKE_SIZE)
    pear_x = random.randint(20, WIDTH -  2 * SNAKE_SIZE)
    pear_y = random.randint(20, HEIGHT - 2 * SNAKE_SIZE)
    melon_x = random.randint(20, WIDTH -  2 * SNAKE_SIZE)
    melon_y = random.randint(20, HEIGHT - 2 * SNAKE_SIZE)
    peach_x = random.randint(20, WIDTH -  2 * SNAKE_SIZE)
    peach_y = random.randint(20, HEIGHT - 2 * SNAKE_SIZE)
    cherry_x = random.randint(20, WIDTH -  2 * SNAKE_SIZE)
    cherry_y = random.randint(20, HEIGHT - 2 * SNAKE_SIZE)
    plum_x = random.randint(20, WIDTH -  2 * SNAKE_SIZE)
    plum_y = random.randint(20, HEIGHT - 2 * SNAKE_SIZE)

    # Coordonatele segmentelor corpului șarpelui
    snake_body = []
    snake_length = 1

    # Variabilă pentru controlul jocului
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction_x != SNAKE_SPEED:  # Evită schimbarea în direcția opusă pe axa X
                    direction_x = -SNAKE_SPEED
                    direction_y = 0
                elif event.key == pygame.K_RIGHT and direction_x != -SNAKE_SPEED:  # Evită schimbarea în direcția opusă pe axa X
                    direction_x = SNAKE_SPEED
                    direction_y = 0
                elif event.key == pygame.K_UP and direction_y != SNAKE_SPEED:  # Evită schimbarea în direcția opusă pe axa Y
                    direction_x = 0
                    direction_y = -SNAKE_SPEED
                elif event.key == pygame.K_DOWN and direction_y != -SNAKE_SPEED:  # Evită schimbarea în direcția opusă pe axa Y
                    direction_x = 0
                    direction_y = SNAKE_SPEED

        # Mișcarea șarpelui
        snake_x += direction_x
        snake_y += direction_y

        # Verificarea coliziunii cu fructul
        if (snake_x >= apple_x and snake_x < apple_x + SNAKE_SIZE) and (snake_y >= apple_y and snake_y < apple_y + SNAKE_SIZE):
            # Noul fruct apare în altă poziție
            apple_x = random.randint(0, WIDTH - 2 * SNAKE_SIZE)
            apple_y = random.randint(0, HEIGHT - 2 * SNAKE_SIZE)
            # Actualizare scor
            sc = sc + 1
            score = fonts.render("Score " + str(sc), True, (255, 255, 255))
            screen.blit(score, (70, 650))
            pygame.display.update()
            snake_length += 1

        if (snake_x >= banana_x and snake_x < banana_x + SNAKE_SIZE) and (snake_y >= banana_y and snake_y < banana_y + SNAKE_SIZE):
            # Noul fruct apare în altă poziție
            banana_x = random.randint(0, WIDTH - 2 * SNAKE_SIZE)
            banana_y = random.randint(0, HEIGHT - 2 * SNAKE_SIZE)
            # Actualizare scor
            sc = sc + 1
            score = fonts.render("Score " + str(sc), True, (255, 255, 255))
            screen.blit(score, (70, 650))
            pygame.display.update()
            snake_length += 1

        if (snake_x >= orange_x and snake_x < orange_x + SNAKE_SIZE) and (snake_y >= orange_y and snake_y < orange_y + SNAKE_SIZE):
            # Noul fruct apare în altă poziție
            orange_x = random.randint(0, WIDTH - 2 * SNAKE_SIZE)
            orange_y = random.randint(0, HEIGHT - 2 * SNAKE_SIZE)
            # Actualizare scor
            sc = sc + 1
            score = fonts.render("Score " + str(sc), True, (255, 255, 255))
            screen.blit(score, (70, 650))
            pygame.display.update()
            snake_length += 1

        if (snake_x >= pear_x and snake_x < pear_x + SNAKE_SIZE) and (snake_y >= pear_y and snake_y < pear_y + SNAKE_SIZE):
            # Noul fruct apare în altă poziție
            pear_x = random.randint(0, WIDTH - 2 * SNAKE_SIZE)
            pear_y = random.randint(0, HEIGHT - 2 * SNAKE_SIZE)
            # Actualizare scor
            sc = sc + 1
            score = fonts.render("Score " + str(sc), True, (255, 255, 255))
            screen.blit(score, (70, 650))
            pygame.display.update()
            snake_length += 1


        if (snake_x >= melon_x and snake_x < melon_x + SNAKE_SIZE) and (snake_y >= melon_y and snake_y < melon_y + SNAKE_SIZE):
            # Noul fruct apare în altă poziție
            melon_x = random.randint(0, WIDTH - 2 * SNAKE_SIZE)
            melon_y = random.randint(0, HEIGHT - 2 * SNAKE_SIZE)
            # Actualizare scor
            sc = sc +1
            score = fonts.render("Score " + str(sc), True, (255, 255, 255))
            screen.blit(score, (70, 650))
            pygame.display.update()
            snake_length += 1


        if (snake_x >= peach_x and snake_x < peach_x + SNAKE_SIZE) and (snake_y >= peach_y and snake_y < peach_y + SNAKE_SIZE):
            # Noul fruct apare în altă poziție
            peach_x = random.randint(0, WIDTH - 2 * SNAKE_SIZE)
            peach_y = random.randint(0, HEIGHT - 2 * SNAKE_SIZE)
            # Actualizare scor
            sc = sc + 1
            score = fonts.render("Score " + str(sc), True, (255, 255, 255))
            screen.blit(score, (70, 650))
            pygame.display.update()
            snake_length += 1

        if (snake_x >= cherry_x and snake_x < cherry_x + SNAKE_SIZE) and (snake_y >= cherry_y and snake_y < cherry_y + SNAKE_SIZE):
            # Noul fruct apare în altă poziție
            cherry_x = random.randint(0, WIDTH - 2 * SNAKE_SIZE)
            cherry_y = random.randint(0, HEIGHT - 2 * SNAKE_SIZE)
            # Actualizare scor
            sc = sc + 1
            score = fonts.render("Score " + str(sc), True, (255, 255, 255))
            screen.blit(score, (70, 650))
            pygame.display.update()
            snake_length += 1


        if (snake_x >= plum_x and snake_x < plum_x + SNAKE_SIZE) and (snake_y >= plum_y and snake_y < plum_y + SNAKE_SIZE):
            # Noul fruct apare în altă poziție
            plum_x = random.randint(0, WIDTH - 2 * SNAKE_SIZE)
            plum_y = random.randint(0, HEIGHT - 2 * SNAKE_SIZE)
            sc = sc + 1
            score = fonts.render("Score " + str(sc), True, (255, 255, 255))
            screen.blit(score, (70, 650))
            pygame.display.update()
            snake_length += 1


        # Actualizarea segmentelor corpului șarpelui
        snake_head = [snake_x, snake_y]
        snake_body.append(snake_head)

        if len(snake_body) > snake_length:
            del snake_body[0]

        # Verificarea coliziunii cu marginea ecranului
        if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
            game_over = True

        # Verificarea coliziunii cu propria coadă
        for segment in snake_body[:-1]:
            if segment == snake_head:
                game_over = True

        # Desenarea imaginilor
        screen.blit(background, (0, 0))

        screen.blit(apple_image, (apple_x, apple_y))
        screen.blit(banana_image, (banana_x, banana_y))
        screen.blit(orange_image, (orange_x, orange_y))
        screen.blit(pear_image, (pear_x, pear_y))
        screen.blit(melon_image, (melon_x, melon_y))
        screen.blit(peach_image, (peach_x, peach_y))
        screen.blit(cherry_image, (cherry_x, cherry_y))
        screen.blit(plum_image, (plum_x, plum_y))

        for segment in snake_body:
            screen.blit(snake_body_image, (segment[0], segment[1]))

        # Desenarea capului șarpelui
        screen.blit(snake_head_image, (snake_x, snake_y))

        # Actualizarea ecranului

        clock.tick(30)

        score = fonts.render("Score: " + str(sc), True, (255, 255, 255))
        screen.blit(score, (70, 550))
        pygame.display.update()

    # Desenarea imaginii de fundal
    screen.blit(background, (0, 0))
    font = pygame.font.Font('font/pixelated.ttf', 70)
    text = font.render("FINAL SCORE IS: " + str(sc), True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)

    pygame.display.update()
    time.sleep(5)

    pygame.quit()


start_menu()
