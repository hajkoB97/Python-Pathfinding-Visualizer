import tkinter
import math
import PathFindingGrid

GRID_SIZE = 20


def click_event(event):
    y = int(math.floor(event.y / 40)) * 40
    x = int(math.floor(event.x / 40)) * 40
    if int(x / 40) < GRID_SIZE and int(y / 40) < GRID_SIZE:
        node = grid.grid[int(x / 40)][int(y / 40)]
        if not node.is_blocked:
            grid.blocked_counter += 1
            node.is_blocked = True
            node.set_color("blue")
        else:
            grid.blocked_counter -= 1
            node.is_blocked = False
            node.set_color("white")


def right_click_event(event):
    y = int(math.floor(event.y / 40)) * 40
    x = int(math.floor(event.x / 40)) * 40
    if int(x / 40) < GRID_SIZE and int(y / 40) < GRID_SIZE:
        grid.set_source(int(x / 40), int(y / 40))


def do(event):
    if event.char == 'd':
        grid.draw_array()

    if event.char == 'c':
        grid.construct_adj_list()

    if event.char == 's':
        grid.run()

    if event.char == 'n':
        y = int(math.floor(event.y / 40)) * 40
        x = int(math.floor(event.x / 40)) * 40
        if int(x / 40) < GRID_SIZE and int(y / 40) < GRID_SIZE:
            grid.showneighbours(int(x / 40), int(y / 40))

    if event.char == 'e':
        y = int(math.floor(event.y / 40)) * 40
        x = int(math.floor(event.x / 40)) * 40
        if int(x / 40) < GRID_SIZE and int(y / 40) < GRID_SIZE:
            grid.set_end_point(int(x / 40), int(y / 40))


main = tkinter.Tk()
main.title("Pathfinder Visualizer")
main.geometry("800x800")

canvas = tkinter.Canvas(main, width=800, height=800)
canvas.configure(bg="white")
canvas.pack()

grid = PathFindingGrid.PathFinderGrid(canvas)
grid.draw_grid()

main.bind("<Button-2>", click_event)
main.bind("<Return>", grid.reset)
main.bind("<Button-3>", right_click_event)
main.bind("<Key>", do)
main.mainloop()
