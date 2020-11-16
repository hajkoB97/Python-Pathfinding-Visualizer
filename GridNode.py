import sys


class GridNode:

    def __init__(self, i, j, grid, is_blocked=False):
        self.i = i
        self.j = j
        self.is_blocked = is_blocked
        self.grid = grid
        self.distance = sys.maxsize
        self.weight = 1

    def get_neighbours(self, arr, ignore_corners=True):
        neighbours = []

        if ignore_corners:
            offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        else:
            offsets = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

        for k, l in offsets:
            h_offset = self.i + k
            v_offset = self.j + l
            if self.grid.ui.col_num > (self.i + k) >= 0 and 0 <= (self.j + l) < self.grid.ui.row_num:
                if k != 0 or l != 0:
                    nb = arr[h_offset][v_offset]
                    if not nb.is_blocked:
                        neighbours.append(nb)
                        self.grid.ui.update()

        return neighbours

    def set_color(self, color, tag=None):
        self.grid.ui.draw_rect(self.i, self.j, color, tag)

    def __str__(self):
        return f"GRID_NODE[I: {self.i}, J: {self.j} IS_BLOCKED: {self.is_blocked}, DIST: {self.distance}]"

    def __repr__(self):
        return f"GRID_NODE[I: {self.i}, J: {self.j} IS_BLOCKED: {self.is_blocked}, DIST: {self.distance}]"
