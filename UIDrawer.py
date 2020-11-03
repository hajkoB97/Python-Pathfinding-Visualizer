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
        self.current_rect_position = -1, -1
        print(self.rect_size, self.canvas_height, canvas['height'])

    def draw_rect(self, i, j, color="blue"):
        x = i * self.rect_size
        y = j * self.rect_size
        self.canvas.create_rectangle(x, y, x + self.rect_size, y + self.rect_size, fill=color)

    def draw_grid(self):
        for i in numpy.arange(0, self.canvas_height + self.rect_size, self.rect_size):
            self.draw_line(0, i, self.canvas_height, i)

        for i in numpy.arange(0, self.canvas_width + self.rect_size, self.rect_size):
            self.draw_line(i, 0, i, self.canvas_width)

    def reset(self):
        self.canvas.delete("all")
        self.draw_grid()
        self.update()

    def draw_line(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2)

    def update(self):
        self.canvas.update()

    def draw_rect_on_hover(self, x, y, color):
        i, j = self.get_indexes_from_coords(x, y)
        if self.current_rect_position != (i, j):
            k, l = self.current_rect_position
            self.draw_rect(k, l, "white")
            self.current_rect_position = i, j
            self.draw_rect(i, j, color)

    def change_gridsize(self, new_col_num, new_row_num):
        self.col_num = new_col_num
        self.row_num = new_row_num
        self.rect_size = self.canvas_height / self.row_num
        self.canvas.delete("all")
        self.draw_grid()
        self.update()

    def get_indexes_from_coords(self, x, y):
        i = int(math.floor(x / self.rect_size))
        j = int(math.floor(y / self.rect_size))
        return i, j
