import math


class UIDrawer:
    def __init__(self, canvas, col_num, row_num):
        self.canvas = canvas
        self.col_num = col_num
        self.row_num = row_num
        self.rect_size = int(canvas['height']) / row_num
        self.current_rect_position = 0, 0
        self.rect_grid = []
        self.create_rect_grid()
        self.hovering_rect = -1

    def create_rect_grid(self):
        self.rect_grid.clear()
        for i in range(self.col_num):
            temp = []
            for j in range(self.col_num):
                temp.append([self.create_rect(i, j, "white")])
            self.rect_grid.append(temp[:])
            temp.clear()
        self.update()

    def create_rect(self, i, j, color, tag=None):
        x = i * self.rect_size
        y = j * self.rect_size
        rect = self.canvas.create_rectangle(x, y, x + self.rect_size, y + self.rect_size, fill=color, tags=tag)

        return rect

    def set_rect_color(self, i, j, color=None, tag=None, foreground=False):
        self.clear_overlaps_on_node(i, j)
        if foreground:
            self.rect_grid[i][j].append(self.create_rect(i, j, color, tag))
        else:
            self.canvas.itemconfigure(self.rect_grid[i][j][0], fill=color, tags=tag)

    def clear_overlaps_on_node(self, i, j):
        if len(self.rect_grid[i][j]) > 1:
            rect_node_list = self.rect_grid[i][j]
            for rect in rect_node_list[1:]:
                self.canvas.delete(rect)
            del rect_node_list[1:]

    def init(self):
        self.clear_by_tag('all')
        self.update()

    def update(self):
        self.canvas.update()

    def draw_rect_on_hover(self, x, y, color):
        i, j = self.get_indexes_from_coords(x, y)

        if self.current_rect_position != (i, j) and 0 <= i < self.col_num and 0 <= j < self.col_num:
            if self.hovering_rect == -1:
                self.hovering_rect = self.create_rect(i, j, color)

            self.canvas.coords(self.hovering_rect, i * self.rect_size, j * self.rect_size,
                               i * self.rect_size + self.rect_size, j * self.rect_size + self.rect_size)
            self.current_rect_position = i, j

    def change_grid_size(self, new_col_num, new_row_num):
        self.col_num = new_col_num
        self.row_num = new_row_num
        self.rect_size = int(self.canvas['height']) / self.row_num
        self.canvas.delete("all")
        self.create_rect_grid()
        self.update()

    def get_indexes_from_coords(self, x, y):
        i = int(math.floor(x / self.rect_size))
        j = int(math.floor(y / self.rect_size))

        if i < 0:
            i = 0
        elif i >= self.col_num:
            i = self.col_num - 1

        if j < 0:
            j = 0
        elif j >= self.col_num:
            j = self.col_num - 1

        return i, j

    def clear_by_tag(self, tag):
        self.canvas.itemconfig(tag, fill="white")
        self.canvas.dtag(tag, tag)

    def clear_search_visualization_rects(self):
        for i in range(self.col_num):
            for j in range(self.row_num):
                self.clear_overlaps_on_node(i, j)

    def clear_hover(self):
        self.canvas.delete(self.hovering_rect)
        self.hovering_rect = -1
