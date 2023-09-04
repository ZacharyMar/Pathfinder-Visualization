import pygame as pg
import Grid
import RCPos
import Draw
import Calculations

# Create screen
WIDTH = 800
WIN = pg.display.set_mode((WIDTH, WIDTH))
pg.display.set_caption("A* Path Finding Algorithm")


def main(win, width, rows):
    grid = Grid.make_grid(rows, width)

    start = None
    end = None

    run = True
    started = False

    while run:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and not started:
                    started = True

                    for row in grid:
                        for node in row:
                            node.update_neighbours(grid)

                    if not Calculations.algorithm(lambda: Draw.draw(win, grid, rows, width), grid, start, end):
                        print("No path found")

                # Reset
                if event.key == pg.K_c:
                    start = None
                    end = None
                    grid = Grid.make_grid(rows, width)
                    started = False

        # Prevents user from inputing anything once algorithm has started
        if not started:

            # Left click
            if pg.mouse.get_pressed()[0]:
                pos = pg.mouse.get_pos()
                row, col = RCPos.get_clicked_pos(pos, rows, width)
                node = grid[row][col]
                if node != end and not start:
                    start = node
                    start.make_start()

                elif node != start and not end:
                    end = node
                    end.make_end()

                elif node != end and node != start:
                    node.make_barrier()

            # Right click
            elif pg.mouse.get_pressed()[2]:
                pos = pg.mouse.get_pos()
                row, col = RCPos.get_clicked_pos(pos, rows, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None

        Draw.draw(win, grid, rows, width)

    pg.quit()


main(WIN, WIDTH, 50)
