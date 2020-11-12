from Algorithm import Algorithm
import sys
import math


class DijkstraAlgorithm(Algorithm):

    def __init__(self, grid, ui_drawer):
        super().__init__(grid, ui_drawer)
        self.grid = grid
        self.distances = []
        self.spt = []
        self.grid_size = len(grid)
        self.source = self.grid[0][0]
        self.end = self.grid[self.grid_size - 1][self.grid_size - 1]
        self.init_algorithm()

    def reset(self):
        self.end_reached = False
        self.source = self.grid[0][0]
        self.source.distance = 0
        self.end = self.grid[self.grid_size - 1][self.grid_size - 1]
        self.source.set_color("green", "source")
        self.end.set_color("black", "end")
        self.init_algorithm()

    def init_algorithm(self):
        self.spt.clear()
        self.distances.clear()
        self.path.clear()
        self.init_distances()

    def run(self, visualize=False):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.grid[i][j].distance == 0:
                    print(self.grid[i][j])
        self.compute_distances(visualize)
        self.clear_grid_after_computing()
        self.show_shortest_path()

    def compute_distances(self, visualize):
        while len(self.distances) != 0:

            min_dist_node = min(self.distances)
            if min_dist_node.distance == sys.maxsize:
                break
            self.distances.remove(min_dist_node)

            if min_dist_node not in self.spt:
                neighbours = min_dist_node.get_neighbours(self.grid)

                self.spt.append(min_dist_node)
                if min_dist_node is self.end:
                    self.end_reached = True
                    break

                for n in neighbours:
                    if n.distance > min_dist_node.distance + n.weight:
                        n.distance = min_dist_node.distance + n.weight
                        if visualize:
                            n.set_color("red", "compute")

    def clear_grid_after_computing(self):
        self.ui.clear_by_tag("compute")
        self.end.set_color("black", "end")
        self.source.set_color("green", "source")

    def show_shortest_path(self):
        self.ui.clear_by_tag("path")
        self.path.clear()

        got_source = False

        neighbours = self.end.get_neighbours(self.grid)

        while not got_source:
            min_neighbour = min(neighbours)
            self.path.append(min_neighbour)

            if min_neighbour.distance == 0:
                break
            neighbours = min_neighbour.get_neighbours(self.grid)

        for i in self.path:
            if i is not self.source:
                i.set_color("yellow", "path")

    def init_distances(self):
        self.distances = []
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                node = self.grid[i][j]
                node.distance = sys.maxsize
                self.distances.append(node)
        self.source.distance = 0

    def set_source_node(self, x, y):
        i = int(math.floor(x / self.ui.rect_size))
        j = int(math.floor(y / self.ui.rect_size))
        if (self.source.i, self.source.j) != (i, j):
            self.ui.clear_by_tag("source")
            self.source.distance = sys.maxsize
        self.source = self.grid[i][j]
        self.source.set_color("green", "source")
        self.source.distance = 0
        self.init_algorithm()

    def set_end_point(self, x, y):
        i = int(math.floor(x / self.ui.rect_size))
        j = int(math.floor(y / self.ui.rect_size))

        self.ui.clear_by_tag("end")
        self.end = self.grid[i][j]
        self.end.set_color("black", "end")
        if self.end_reached:
            self.show_shortest_path()

