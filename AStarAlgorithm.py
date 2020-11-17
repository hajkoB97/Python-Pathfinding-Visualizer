import sys

from Algorithm import Algorithm


class AStarAlgorithm(Algorithm):
    def __init__(self, grid, ui_drawer):
        super().__init__(grid, ui_drawer)
        self.open_list = []
        self.closed_list = []
        self.distances = []
        self.path = []
        self.init_algorithm()

    def init_algorithm(self):
        self.open_list.clear()
        self.closed_list.clear()
        self.path.clear()
        self.end_reached = False
        self.closed_list.append(self.grid.source_node)
        self.init_distances()
        self.ui.clear_by_tag("path")

    def run(self, visualize=False):
        self.init_algorithm()
        self.start_search(visualize)
        self.ui.clear_search_visualization_rects()

        if self.end_reached:
            self.show_shortest_path()

    def start_search(self, visualize):
        neighbours = self.grid.source_node.get_neighbours(self.grid)
        self.open_list.extend(neighbours)

        for n in neighbours:
            n.movement_cost_sum = self.grid.source_node.movement_cost_sum + n.weight
            n.heuristic_dist = abs(n.i - self.grid.end_node.i) + abs(n.j - self.grid.end_node.j)
            n.distance = n.movement_cost_sum + n.heuristic_dist
            if visualize:
                n.set_color("gray", "search", foreground=True)

        while not len(self.open_list) == 0:
            min_node = self.get_min_distance_node(self.open_list)
            self.open_list.remove(min_node)
            if visualize:
                min_node.set_color("gray", "search", foreground=True)
            self.closed_list.append(min_node)

            neighbours = min_node.get_neighbours(self.grid)

            for n in neighbours:
                if n is self.grid.end_node:
                    self.end_reached = True
                    n.parent = min_node
                    break

                new_movement_cost = min_node.movement_cost_sum + n.weight
                new_heuristic_dist = abs(n.i - self.grid.end_node.i) + abs(n.j - self.grid.end_node.j)
                new_distance = new_movement_cost + new_heuristic_dist

                if n not in self.closed_list:
                    if n not in self.open_list or n.distance > new_distance:
                        n.movement_cost_sum = new_movement_cost
                        n.heuristic_dist = new_heuristic_dist
                        n.distance = new_distance
                        n.parent = min_node
                        if visualize:
                            n.set_color("SkyBlue1", "search", foreground=True)
                        self.open_list.append(n)

            if self.end_reached:
                return

        if not self.end_reached:
            print("Failed to find end point")

    def init_distances(self):
        for i in range(self.grid.col_num):
            for j in range(self.grid.row_num):
                node = self.grid[i][j]
                node.distance = sys.maxsize
                node.movement_cost_sum = sys.maxsize
                node.heuristic_dist = sys.maxsize
                node.parent = None

        self.grid.source_node.heuristic = 0.0
        self.grid.source_node.movement_cost_sum = 0.0
        self.grid.source_node.distance = 0.0
        self.grid.source_node.parent = self.grid.source_node

    def show_shortest_path(self):
        parent = self.grid.end_node.parent

        while parent != self.grid.source_node:
            if parent is None:
                break
            parent.set_color("yellow", "path", foreground=True)
            self.path.append(parent)
            parent = parent.parent

    def reset(self):
        pass

    def get_min_distance_node(self, nodes):
        min_node = None
        min_dist = sys.maxsize
        for node in nodes:
            if node.distance < min_dist:
                min_node = node
                min_dist = node.distance
        return min_node
