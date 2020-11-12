import sys


class GridNode:

    def __init__(self, i, j, canvas, is_blocked=False):
        self.i = i
        self.j = j
        self.is_blocked = is_blocked
        self.ui = canvas
        self.distance = sys.maxsize
        self.weight = 1

    def get_neighbours(self, arr, ignore_corners = True):
        offsets = []
        neighbours = []

        if ignore_corners:
            offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        else:
            offsets = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

        for k, l in offsets:
            h_offset = self.i + k
            v_offset = self.j + l
            if self.ui.col_num > (self.i + k) >= 0 and 0 <= (self.j + l) < self.ui.row_num:
                if k != 0 or l != 0:
                    nb = arr[h_offset][v_offset]
                    if not nb.is_blocked:
                        self.ui.update()
                        neighbours.append(nb)

        return neighbours

    def set_color(self, color, tag = None):
        self.ui.draw_rect(self.i, self.j, color, tag)

    def __str__(self):
        return f"GRID_NODE[I: {self.i}, J: {self.j} IS_BLOCKED: {self.is_blocked}, DIST: {self.distance}]"

    def __repr__(self):
        return f"GRID_NODE[I: {self.i}, J: {self.j} IS_BLOCKED: {self.is_blocked}, DIST: {self.distance}]"

    def __lt__(self, other):
        return self.distance < other.distance

    def __gt__(self, other):
        return self.distance > other.distance

    def __ge__(self, other):
        return self.distance >= other.distance

    def __le__(self, other):
        return self.distance <= other.distance
