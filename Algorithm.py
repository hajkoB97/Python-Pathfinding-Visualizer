from abc import ABC


class Algorithm(ABC):
    def __init__(self, grid, ui_drawer):
        self.grid = grid
        self.ui = ui_drawer
        self.end_reached = False
        self.path = []

    def init_algorithm(self):
        pass

    def run(self, visualize=False):
        pass

    def show_shortest_path(self):
        pass

    def reset(self):
        pass

    def clear_grid_after_search(self):
        self.ui.clear_by_tag("search")
        self.grid.end_node.set_color("black", "end")
        self.grid.source_node.set_color("green", "source")
