import numpy
import math


class UIDrawer:
    def __init__(self, canvas, col_num, row_num):
        self.canvas = canvas
        self.col_num = col_num
        self.row_num = row_num
        self.canvas_width = int(canvas['width'])
        self.canvas_height = int(canvas['height'])
        self.rect_size = self.canvas_height / row_num
        self.current_rect_position = 0, 0
        self.rect_grid = []
        self.create_rect_grid()

    def create_rect_grid(self):
        self.rect_grid.clear()
        for i in range(self.col_num):
            temp = []
            for j in range(self.col_num):
                temp.append(self.create_rect(i, j, "white"))
            self.rect_grid.append(temp[:])
            temp.clear()
        self.update()

    def create_rect(self, i, j, color="blue", tag=None):
        x = i * self.rect_size
        y = j * self.rect_size
        return self.canvas.create_rectangle(x, y, x + self.rect_size, y + self.rect_size, fill=color, tags=tag)

    def draw_rect(self, i, j, color="blue", tag=None):
        self.canvas.itemconfigure(self.rect_grid[i][j], fill=color, tags=tag)

    def draw_grid(self):
        for i in numpy.arange(0, self.canvas_height + self.rect_size, self.rect_size):
            self.draw_line(0, i, self.canvas_height, i)

        for i in numpy.arange(0, self.canvas_width + self.rect_size, self.rect_size):
            self.draw_line(i, 0, i, self.canvas_width)

    def init(self):
        self.clear_by_tag('all')
        self.draw_grid()
        self.update()

    def draw_line(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2)

    def update(self):
        self.canvas.update()

    def draw_rect_on_hover(self, x, y, color):
        i, j = self.get_indexes_from_coords(x, y)

        if self.current_rect_position != (i, j) and 0 <= i < self.col_num and 0 <= j < self.col_num:
            prev_i, prev_j = self.current_rect_position
            current_rect = self.rect_grid[i][j]
            prev_rect = self.rect_grid[prev_i][prev_j]

            states = {"blocked" : "blue", "source" : "green", "end" : "black", "path" : "yellow"}
            tags = self.canvas.itemcget(prev_rect, "tags").split()

            c = None

            for t in tags:
                if t in states:
                    c = states[t]

            if c is not None:
                self.canvas.itemconfig(prev_rect, fill=c)
            else:
                self.canvas.itemconfig(prev_rect, fill="white")
                self.canvas.itemconfig(current_rect, fill=color, tags="hover")

            self.current_rect_position = i, j

    def change_grid_size(self, new_col_num, new_row_num):
        self.col_num = new_col_num
        self.row_num = new_row_num
        self.rect_size = self.canvas_height / self.row_num
        self.canvas.delete("all")
        self.draw_grid()
        self.create_rect_grid()
        self.update()

    def get_indexes_from_coords(self, x, y):
        i = int(math.floor(x / self.rect_size))
        j = int(math.floor(y / self.rect_size))
        return i, j

    def clear_by_tag(self, tag):
        self.canvas.itemconfig(tag, fill="white")
        self.canvas.dtag(tag,tag)
