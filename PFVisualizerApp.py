import math

from AStarAlgorithm import AStarAlgorithm
from DijkstraAlgorithm import DijkstraAlgorithm
from Grid import Grid
from UIDrawer import UIDrawer


class PathFinderVisualizerApp:

    def __init__(self, canvas):
        self.grid_size = 30
        self.ui = UIDrawer(canvas, self.grid_size, self.grid_size)
        self.grid = Grid(self.grid_size, self.grid_size, self.ui)
        self._algorithm = DijkstraAlgorithm(self.grid, self.ui)
        self.visualize = True
        self.init()

    def set_algorithm(self, algorithm_name):
        if algorithm_name == "Dijkstra":
            self._algorithm = DijkstraAlgorithm(self.grid, self.ui)
        elif algorithm_name == "A*":
            self._algorithm = AStarAlgorithm(self.grid, self.ui)

    def run(self):
        self._algorithm.run(self.visualize)

    def init(self):
        self.ui.init()
        self.grid.construct()
        self._algorithm.init_algorithm()

    def set_node_state(self, x, y, weight, color):
        i = int(math.floor(x / self.ui.rect_size))
        j = int(math.floor(y / self.ui.rect_size))
        if i < self.ui.row_num and j < self.ui.col_num:
            self.grid.set_node_state(i, j, weight, color)

    def change_grid_size(self, col_num, row_num):
        self.ui.change_grid_size(col_num, row_num)
        self.grid.change_size(col_num, row_num)
        self.init()

    def set_source_node(self, x, y):
        i = int(math.floor(x / self.ui.rect_size))
        j = int(math.floor(y / self.ui.rect_size))
        if (self.grid.source_node.i, self.grid.source_node.j) != (i, j):
            self.grid.set_source_node(i, j)
            self._algorithm.init_algorithm()

    def set_end_point(self, x, y):
        i = int(math.floor(x / self.ui.rect_size))
        j = int(math.floor(y / self.ui.rect_size))
        if (self.grid.end_node.i, self.grid.end_node.j) != (i, j):
            self.grid.set_end_node(i, j)
