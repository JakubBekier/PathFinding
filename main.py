import finding as f
import gui as g
import pygame

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 140, 0)
PURPLE = (128, 0, 128)
GREEN = (0, 255, 0)
ROWS = 26
COLUMNS = 26
WIDTH = 780
HEIGHT = 780
drawing = False
deleting = False
drawing_number = 0
start = []

pygame.init()
window = pygame.display.set_mode((WIDTH,HEIGHT))

g.drawGrid(window, ROWS, COLUMNS, WIDTH, HEIGHT)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
            elif event.button == 3:
                deleting = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
            elif event.button == 3:
                deleting = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                g.drawGrid(window, ROWS, COLUMNS, WIDTH, HEIGHT)
                drawing_number = 0
            elif event.key == pygame.K_SPACE:
                maze = f.windowToMaze(window, ROWS, COLUMNS, WIDTH, HEIGHT)
                ans = f.find_path(maze, window, ROWS, COLUMNS, WIDTH, HEIGHT)

                if ans:
                    g.delPath(window, ROWS, COLUMNS, WIDTH, HEIGHT)
                    for ele in ans:
                        pygame.draw.rect(window, RED, [ ele[1] * (WIDTH / ROWS) + 1,
                                                         (ele[0] * (HEIGHT / COLUMNS)) + 1,
                                                         WIDTH / ROWS - 1, HEIGHT / COLUMNS - 1])
                    pygame.display.flip()


    if drawing:
        mouse_position = pygame.mouse.get_pos()
        left = mouse_position[0]
        top = mouse_position[1]
        if drawing_number == 0:
            pygame.draw.rect(window, ORANGE, [(left//(WIDTH/ROWS)) * (WIDTH/ROWS) + 1, (top//(HEIGHT/COLUMNS)) * (HEIGHT/COLUMNS) + 1,
                                         WIDTH / ROWS - 1, HEIGHT / COLUMNS - 1])
            drawing = False
            drawing_number += 1
        elif drawing_number == 1:
            pygame.draw.rect(window, PURPLE, [(left // (WIDTH / ROWS)) * (WIDTH / ROWS) + 1,
                                              (top // (HEIGHT / COLUMNS)) * (HEIGHT / COLUMNS) + 1,
                                              WIDTH / ROWS - 1, HEIGHT / COLUMNS - 1])
            drawing = False
            drawing_number += 1
        else:
            pygame.draw.rect(window, BLACK, [(left//(WIDTH/ROWS)) * (WIDTH/ROWS) + 1, ((top//(HEIGHT/COLUMNS)) * (HEIGHT/COLUMNS)) + 1,
                                             WIDTH / ROWS - 1, HEIGHT / COLUMNS - 1])
    if deleting:
        mouse_position = pygame.mouse.get_pos()
        left = mouse_position[0]
        top = mouse_position[1]

        pygame.draw.rect(window, WHITE, [(left//(WIDTH/ROWS)) * (WIDTH/ROWS) + 1, ((top//(HEIGHT/COLUMNS)) * (HEIGHT/COLUMNS)) + 1,
                                             WIDTH / ROWS - 1, HEIGHT / COLUMNS - 1])
    pygame.display.flip()

pygame.quit()
