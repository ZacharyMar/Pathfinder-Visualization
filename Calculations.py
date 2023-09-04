from queue import PriorityQueue
import pygame as pg


# Gets manhattan distance
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


# Visualization of path found
def reconstruct_path(came_from, current, draw, start):
    # Works backwards from end node to previous nodes in path
    while current in came_from:
        # Finds previous node in the path
        current = came_from[current]
        if current != start:
            current.make_path()
        draw()


# Path finding algorithm
def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    # .put adds f score, current path count and start position to open set
    open_set.put((0, count, start))

    # Dict keeps track of the path taken
    came_from = {}

    # Creates table for g scores (current shortest path to that node)
    g_score = {node: float("inf") for row in grid for node in row}
    # Start node's g score is 0 since there is no path
    g_score[start] = 0

    # Creates table for f scores (H(n) + G(n))
    f_score = {node: float("inf") for row in grid for node in row}
    # Uses heuristics to estimate distance from start to end node - initial f score since g score is 0
    f_score[start] = h(start.get_pos(), end.get_pos())

    # Used to determine current node
    open_set_hash = {start}

    # Runs while there are objects in the open set
    while not open_set.empty():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        # Gets node in open set
        current = open_set.get()[2]
        # Keep queue in sync with hash
        open_set_hash.remove(current)

        # Path found
        if current == end:
            reconstruct_path(came_from, current, draw, start)
            end.make_end()

            return True

        # Consider neighbour nodes for path
        for neighbour in current.neighbours:
            # calculate tentative g score
            temp_g_score = g_score[current] + 1

            # if the g score is lower, a better path has been found and update value
            if temp_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + h(neighbour.get_pos(), end.get_pos())
                # Add neighbour to open set
                if neighbour not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbour], count, neighbour))
                    open_set_hash.add(neighbour)
                    # New considered path
                    neighbour.make_open()

        draw()

        # Already considered
        if current != start:
            current.make_closed()

    return False
