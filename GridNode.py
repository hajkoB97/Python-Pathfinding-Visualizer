import sys

GRID_SIZE = 20


class GridNode:
    size = 40

    def __init__(self, i, j, canvas, is_blocked=False):
        self.i = i
        self.j = j
        self.is_blocked = is_blocked
        self.canvas = canvas
        self.distance = sys.maxsize

    def get_neighbours(self, arr):
        horizontal_offsets = [-1, 0, 1]
        vertical_offsets = [-1, 0, 1]

        offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        neighbours = []

        for k, l in offsets:
            h_offset = self.i + k
            v_offset = self.j + l
            if GRID_SIZE > (self.i + k) >= 0 and 0 <= (self.j + l) < GRID_SIZE:
                if k != 0 or l != 0:
                    nb = arr[h_offset][v_offset]
                    if not nb.is_blocked:
                        self.canvas.update()
                        neighbours.append(nb)

        return neighbours

    def set_color(self, color):
        x = self.i * GridNode.size
        y = self.j * GridNode.size
        self.canvas.create_rectangle(x, y, x + GridNode.size, y + GridNode.size, fill=color)

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
