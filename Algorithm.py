from abc import ABC


class Algorithm(ABC):
    def __init__(self, grid, ui_drawer):
        self.grid = grid
        self.ui = ui_drawer
        self.end_reached = False
        self.path = []


    def init_algorithm(self):
        pass

    def run(self,visualize = False):
        pass

    def show_shortest_path(self):
        pass

    def reset(self):
        pass