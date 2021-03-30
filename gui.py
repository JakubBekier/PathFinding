import pygame

def drawGrid(window, ROWS, COLUMNS, WIDTH, HEIGHT):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    window.fill(WHITE);
    for i in range(ROWS):
        pygame.draw.line(window, BLACK, [i * WIDTH / ROWS, 0], [i * WIDTH / ROWS, HEIGHT])
        pygame.draw.rect(window, BLACK, [1, i * WIDTH / ROWS + 1, WIDTH / ROWS - 1, HEIGHT / COLUMNS - 1])
        pygame.draw.rect(window, BLACK,
                         [WIDTH - WIDTH / COLUMNS + 1, i * WIDTH / ROWS + 1, WIDTH / ROWS - 1, HEIGHT / COLUMNS - 1])
    for j in range(COLUMNS):
        pygame.draw.line(window, BLACK, [0, j * HEIGHT / COLUMNS], [WIDTH, j * HEIGHT / COLUMNS])
        pygame.draw.rect(window, BLACK, [j * HEIGHT / COLUMNS + 1, 1, WIDTH / ROWS - 1, HEIGHT / COLUMNS - 1])
        pygame.draw.rect(window, BLACK,
                         [j * HEIGHT / COLUMNS + 1, HEIGHT - HEIGHT / ROWS + 1, WIDTH / ROWS - 1, HEIGHT / COLUMNS - 1])

def delPath(window, ROWS, COLUMNS, WIDTH, HEIGHT):
    GREEN = (0, 255, 0)
    WHITE = (255, 255, 255)
    for i in range(COLUMNS):
        for j in range(ROWS):
            color = window.get_at([i * (WIDTH // COLUMNS) + 1, j * (HEIGHT // ROWS) + 1])
            if color == GREEN:
                pygame.draw.rect(window, WHITE, [i * (WIDTH // COLUMNS) + 1,
                                                 j * (HEIGHT // COLUMNS) + 1,
                                                 WIDTH / ROWS - 1, HEIGHT / COLUMNS - 1])

