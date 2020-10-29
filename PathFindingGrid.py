from GridNode import GridNode
import sys

GRID_SIZE = 20


class PathFinderGrid:

    def __init__(self, canvas):
        self.blocked_counter = 0
        self.grid = []
        self.canvas = canvas

        self.end = (-1, -1)
        self.end_reached = False

        self.spt = []
        self.source = -1, -1
        self.adj_lists = dict()
        self.consturct_grid_node_array()
        self.distances = []
        self.sp = []

    def consturct_grid_node_array(self):
        temp_list = []
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                temp_list.append(GridNode(i, j, self.canvas))
            self.grid.append(temp_list)
            temp_list = []

    def construct_adj_list(self):
        for i in range(20):
            for j in range(20):
                node = self.grid[i][j]
                if node.is_blocked:
                    continue
                else:
                    self.adj_lists[node] = node.get_neighbours(self.grid)

    def run(self):
        self.init_distances()
        self.compute_distances()

        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                node = self.grid[i][j]
                if not node.is_blocked:
                    node.set_color("white")
        self.get_end_node().set_color("black")
        self.get_source_node().set_color("green")

        if self.end_reached:
            self.draw_shortest_path()

    def get_end_node(self):
        return self.grid[self.end[0]][self.end[1]]

    def get_source_node(self):
        return self.grid[self.source[0]][self.source[1]]

    def draw_shortest_path(self):
        if len(self.sp) > 0:
            for n in self.sp:
                n.set_color("white")
            self.sp = []

        got_source = False

        neighbours = self.grid[self.end[0]][self.end[1]].get_neighbours(self.grid)
        while not got_source:
            min_neighbour = min(neighbours)
            self.sp.append(min_neighbour)
            if min_neighbour.distance == 0:
                break

            neighbours = min_neighbour.get_neighbours(self.grid)
        for i in self.sp:
            if i is not self.get_source_node():
                i.set_color("yellow")

    def init_distances(self):
        self.distances = []
        for i in range(20):
            for j in range(20):
                self.distances.append(self.grid[i][j])

    def compute_distances(self):
        while len(self.spt) != 400 - self.blocked_counter:
            if len(self.distances) != 0:
                min_dist_node = min(self.distances)
                if min_dist_node.distance == sys.maxsize:
                    break
                self.distances.remove(min_dist_node)

                # print(min_dist_node)
                if min_dist_node not in self.spt:
                    neighbours = min_dist_node.get_neighbours(self.grid)

                    if len(neighbours) == 0:
                        print(neighbours)

                    self.spt.append(min_dist_node)
                    if min_dist_node.i == self.end[0] and min_dist_node.j == self.end[1]:
                        self.end_reached = True

                    for n in neighbours:
                        n.set_color("red")
                        if n.distance > min_dist_node.distance + 1:
                            n.distance = min_dist_node.distance + 1
                            n.set_color("purple")

    def draw_rect(self, x, y, size, color="blue"):
        self.canvas.create_rectangle(x, y, x + size, y + size, fill=color)

    def draw_grid(self):
        for i in range(0, 840, 40):
            self.draw_line(0, i, 800, i)

        for i in range(0, 840, 40):
            self.draw_line(i, 0, i, 800)

    def draw_line(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2)

    def reset(self, event):
        self.canvas.delete("all")
        self.grid = []
        self.consturct_grid_node_array()
        self.draw_grid()

    def draw_array(self):
        for i in range(0, GRID_SIZE):
            for j in range(0, GRID_SIZE):
                if self.grid[i][j].is_blocked:
                    self.draw_rect(i * 40, j * 40, 40)

    def showneighbours(self, i, j):
        node = self.grid[i][j]
        print(node.get_neighbours(self.grid))

    def get_node_by_index(self, position):
        i, j = position
        return self.grid[i][j]

    def set_source(self, i, j):
        if self.source != (-1, -1):
            self.get_node_by_index(self.source).set_color("white")
            self.get_node_by_index(self.source).distance = sys.maxsize
        self.source = (i, j)
        self.grid[i][j].set_color("green")
        self.grid[i][j].distance = 0

    def set_end_point(self, i, j):
        if self.end != (-1, -1):
            self.get_node_by_index(self.end).set_color("white")

        self.end = (i, j)
        self.grid[i][j].set_color("black")
        if self.end_reached:
            self.draw_shortest_path()
