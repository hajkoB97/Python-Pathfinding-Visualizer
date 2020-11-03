from GridNode import GridNode
import sys
import math
from tkinter import messagebox
from UIDrawer import UIDrawer


class PathFinderGrid:

    def __init__(self, canvas):
        self.grid_size = 20
        self.ui = UIDrawer(canvas, self.grid_size, self.grid_size)
        self.reset(None)
        self.ui.draw_grid()

    def consturct_grid_node_array(self):
        temp_list = []
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                temp_list.append(GridNode(i, j, self.ui))
            self.grid.append(temp_list)
            temp_list = []

    def run(self):
        self.init_distances()
        self.compute_distances()
        self.clear_grid_after_computing()

        if self.end_reached:
            self.draw_shortest_path()

    def clear_grid_after_computing(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                node = self.grid[i][j]
                if not node.is_blocked:
                    node.set_color("white")
        self.get_end_node().set_color("black")
        self.get_source_node().set_color("green")

    def get_end_node(self):
        return self.grid[self.end[0]][self.end[1]]

    def get_source_node(self):
        return self.grid[self.source[0]][self.source[1]]

    def draw_shortest_path(self):
        if len(self.sp) > 0:
            for n in self.sp:
                n.set_color("white")
            self.sp = []

        got_source = False

        neighbours = self.grid[self.end[0]][self.end[1]].get_neighbours(self.grid)
        while not got_source:
            min_neighbour = min(neighbours)
            self.sp.append(min_neighbour)
            if min_neighbour.distance == 0:
                break

            neighbours = min_neighbour.get_neighbours(self.grid)

        for i in self.sp:
            if i is not self.get_source_node():
                i.set_color("yellow")

        self.alert("Number of steps", len(self.sp) - 1)

    def init_distances(self):
        self.distances = []
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.distances.append(self.grid[i][j])

    def compute_distances(self):
        while len(self.spt) != self.grid_size ** 2 - self.blocked_counter:
            if len(self.distances) != 0:
                min_dist_node = min(self.distances)
                if min_dist_node.distance == sys.maxsize:
                    break
                self.distances.remove(min_dist_node)

                if min_dist_node not in self.spt:
                    neighbours = min_dist_node.get_neighbours(self.grid)

                    self.spt.append(min_dist_node)
                    if min_dist_node.i == self.end[0] and min_dist_node.j == self.end[1]:
                        self.end_reached = True

                    for n in neighbours:
                        n.set_color("red")
                        if n.distance > min_dist_node.distance + 1:
                            n.distance = min_dist_node.distance + 1
                            n.set_color("purple")

    def reset(self, event):
        self.blocked_counter = 0
        self.grid = []
        self.end = (self.grid_size - 1, self.grid_size - 1)
        self.end_reached = False
        self.source = 0, 0
        self.spt = []
        self.distances = []
        self.sp = []
        self.consturct_grid_node_array()

        self.ui.reset()
        self.set_source(0, 0)
        self.set_end_point(self.end[0] * self.ui.rect_size, self.end[1] * self.ui.rect_size)

    def get_node_by_index(self, position):
        i, j = position
        return self.grid[i][j]

    def set_source(self, x, y):
        i = int(math.floor(x / self.ui.rect_size))
        j = int(math.floor(y / self.ui.rect_size))
        if self.source != (i, j):
            self.get_node_by_index(self.source).set_color("white")
            self.get_node_by_index(self.source).distance = sys.maxsize
        self.source = (i, j)
        self.grid[i][j].set_color("green")
        self.grid[i][j].distance = 0

    def set_end_point(self, x, y):
        i = int(math.floor(x / self.ui.rect_size))
        j = int(math.floor(y / self.ui.rect_size))

        if self.end != (-1, -1):
            self.get_node_by_index(self.end).set_color("white")

        self.end = (i, j)
        self.grid[i][j].set_color("black")
        if self.end_reached:
            self.draw_shortest_path()

    def set_blocked_state(self, x, y, block=True):
        i = int(math.floor(x / self.ui.rect_size))
        j = int(math.floor(y / self.ui.rect_size))

        if (i, j) == self.source or (i, j) == self.end:
            return

        if i < self.ui.row_num and j < self.ui.col_num:
            node = self.grid[i][j]
            if not node.is_blocked:
                if block:
                    self.blocked_counter += 1
                    node.is_blocked = True
                    node.set_color("blue")
            else:
                if not block:
                    self.blocked_counter -= 1
                    node.is_blocked = False
                    node.set_color("white")

    def change_gridsize(self, col_num, row_num):
        self.ui.change_gridsize(col_num, row_num)
        self.grid_size = col_num
        self.reset(None)

    def alert(self, title, message, kind='info', hidemain=True):
        if kind not in ('error', 'warning', 'info'):
            raise ValueError('Unsupported alert kind.')

        show_method = getattr(messagebox, 'show{}'.format(kind))
        show_method(title, message)
