import sys

from Algorithm import Algorithm


class DijkstraAlgorithm(Algorithm):

    def __init__(self, grid, ui_drawer):
        super().__init__(grid, ui_drawer)
        self.grid = grid
        self.distances = []
        self.spt = []
        self.grid.source_node = self.grid[0][0]
        self.grid.end_node = self.grid[self.grid.col_num - 1][self.grid.row_num - 1]
        self.init_algorithm()

    def init_algorithm(self):
        self.spt.clear()
        self.distances.clear()
        self.path.clear()
        self.end_reached = False
        self.init_distances()
        self.ui.clear_by_tag("path")

    def run(self, visualize=False):
        self.init_algorithm()

        self.start_search(visualize)
        self.clear_grid_after_search()
        if self.end_reached:
            self.show_shortest_path()

    def start_search(self, visualize):
        while len(self.distances) != 0:

            min_dist_node = self.get_min_distance_node(self.distances)
            if min_dist_node.distance == sys.maxsize:
                break
            self.distances.remove(min_dist_node)

            if min_dist_node not in self.spt:
                neighbours = min_dist_node.get_neighbours(self.grid)
                min_dist_node.set_color("gray", "search")

                self.spt.append(min_dist_node)

                if min_dist_node is self.grid.end_node:
                    self.end_reached = True
                    break

                for n in neighbours:
                    if n.distance > min_dist_node.distance + n.weight:
                        n.distance = min_dist_node.distance + n.weight
                        if visualize:
                            n.set_color("SkyBlue1", "search")

    def show_shortest_path(self):
        self.ui.clear_by_tag("path")
        self.path.clear()

        got_source = False

        neighbours = self.grid.end_node.get_neighbours(self.grid)

        while not got_source:
            min_neighbour = self.get_min_distance_node(neighbours)
            self.path.append(min_neighbour)

            if min_neighbour.distance == 0:
                break
            neighbours = min_neighbour.get_neighbours(self.grid)

        for i in self.path:
            if i is not self.grid.source_node:
                i.set_color("yellow", "path")

    def init_distances(self):
        self.distances = []
        for i in range(self.grid.col_num):
            for j in range(self.grid.row_num):
                node = self.grid[i][j]
                node.distance = sys.maxsize
                self.distances.append(node)
        self.grid.source_node.distance = 0

    def get_min_distance_node(self, nodes):
        min_node = nodes[0]
        for node in nodes:
            if node.distance < min_node.distance:
                min_node = node
        return min_node
