import heapq as h
import pygame
import math

def dist(a,b):
    # return abs(a[0]-b[0]) + abs(a[1]-b[1])
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def find_path(maze, window, ROWS, COLUMNS, WIDTH, HEIGHT):
    GREEN = (0, 255, 0)
    open = []
    closed = set()
    neighbors_check = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    came_from = {}

    for i in range(ROWS):
        for j in range(COLUMNS):
            if maze[i][j] == "Start":
                start = (i,j)
            elif maze[i][j] == "End":
                end = (i,j)

    gscore = {start: 0}
    fscore = {start: dist(start, end)}

    h.heappush(open, (fscore[start], start))

    run = True

    while open and run:
        current = h.heappop(open)[1]      # Pobierz z open ten o najmniejszym koszcie dotarcia + oszacowanym do końca

        if current == end:
            data = []

            while current in came_from:
                data.append(current)

                current = came_from[current]
            data = data[1:len(data)]
            run = False
            return data

        if current != start:
            pygame.draw.rect(window, GREEN, [current[1] * (WIDTH / ROWS) + 1,
                                             (current[0] * (HEIGHT / COLUMNS)) + 1,
                                             WIDTH / ROWS - 1, HEIGHT / COLUMNS - 1])
            pygame.display.flip()
            # pygame.time.wait(50)

        closed.add(current)
        for i,j in neighbors_check:
            neighbour = current[0] + i, current[1] + j
            if maze[neighbour[0]][neighbour[1]] == "Obstacle":
                continue

            neigh_g = dist(neighbour, current) + gscore[current]   # Koszt dotarcie do sąsiada poprzez current

            if neighbour in closed:
                continue

            if neighbour not in [i[1] for i in open]:
                came_from[neighbour] = current
                gscore[neighbour] = neigh_g
                fscore[neighbour] = neigh_g + dist(neighbour, end)
                h.heappush(open, (fscore[neighbour], neighbour))


            #Jeżeli mamy krótszą drogę lub neigh nie należy do open
            elif neigh_g < gscore.get(neighbour, 0):
                came_from[neighbour] = current
                gscore[neighbour] = neigh_g
                fscore[neighbour] = neigh_g + dist(neighbour, end)
                h.heappush(open, (fscore[neighbour], neighbour))
    return False

def windowToMaze(window, ROWS, COLUMNS, WIDTH, HEIGHT):
    BLACK = (0, 0, 0)
    ORANGE = (255, 140, 0)
    PURPLE = (128, 0, 128)
    maze = [[" " for i in range(COLUMNS)] for j in range(ROWS)]
    for i in range(COLUMNS):
        for j in range(ROWS):
            color = window.get_at([i * (WIDTH // COLUMNS) + 1, j * (HEIGHT // ROWS) + 1])
            if color == ORANGE:
                maze[j][i] = "Start"
            elif color == PURPLE:
                maze[j][i] = "End"
            elif color == BLACK:
                maze[j][i] = "Obstacle"
            else:
                maze[j][i] = "Clear"
    return maze