from GridNode import GridNode
import math
from tkinter import messagebox
from UIDrawer import UIDrawer
from DijkstraAlgorithm import DijkstraAlgorithm


class PathFinderGrid:

    def __init__(self, canvas):
        self.grid_size = 20
        self.grid = []
        self.ui = UIDrawer(canvas, self.grid_size, self.grid_size)
        self.consturct_grid_node_array()
        self._algorithm = DijkstraAlgorithm(self.grid, self.ui)
        self.init()
        self.ui.draw_grid()

    def set_algorithm(self, algorithm_name):
        if algorithm_name == "Dijkstra":
            self._algorithm = DijkstraAlgorithm(self.grid, self.ui)

    def consturct_grid_node_array(self):
        temp_list = []
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                temp_list.append(GridNode(i, j, self.ui))
            self.grid.append(temp_list)
            temp_list = []

    def run(self):
        if len(self._algorithm.spt) > 0:
            self._algorithm.reset()
        self._algorithm.run(True)

    def clear_grid_after_computing(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                node = self.grid[i][j]
                if not node.is_blocked:
                    node.set_color("white")
        self.get_end_node().set_color("black")
        self.get_source_node().set_color("green")

    def get_end_node(self):
        return self._algorithm.end

    def get_source_node(self):
        return self._algorithm.source

    def set_source(self, x, y):
        self._algorithm.set_source_node(x, y)

    def set_end_point(self, x, y):
        self._algorithm.set_end_point(x, y)

    def init(self):
        self.grid.clear()
        self.consturct_grid_node_array()
        self.ui.init()
        self._algorithm.reset()

    def set_blocked_state(self, x, y, block=True):
        i = int(math.floor(x / self.ui.rect_size))
        j = int(math.floor(y / self.ui.rect_size))
        if i < self.ui.row_num and j < self.ui.col_num:

            node = self.grid[i][j]
            if node == self._algorithm.source or node == self._algorithm.source:
                return
            if not node.is_blocked:
                if block:
                    node.is_blocked = True
                    node.set_color("blue", "blocked")
            else:
                if not block:
                    node.is_blocked = False
                    node.set_color("white")

    def change_grid_size(self, col_num, row_num):
        self.ui.change_grid_size(col_num, row_num)
        self.grid_size = col_num
        self._algorithm.grid_size = col_num
        self.init()

    def alert(self, title, message, kind='info', hidemain=True):
        if kind not in ('error', 'warning', 'info'):
            raise ValueError('Unsupported alert kind.')

        show_method = getattr(messagebox, 'show{}'.format(kind))
        show_method(title, message)
