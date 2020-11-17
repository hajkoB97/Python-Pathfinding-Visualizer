from GridNode import GridNode


class Grid:
    def __init__(self, col_num, row_num, ui_drawer):
        self.grid = []
        self.ui = ui_drawer
        self.col_num = col_num
        self.row_num = row_num
        self.construct()
        self.source_node = self.grid[0][0]
        self.end_node = self.grid[self.col_num - 1][self.row_num - 1]

    def construct(self):
        self.grid.clear()

        temp_list = []
        for i in range(self.col_num):
            for j in range(self.row_num):
                temp_list.append(GridNode(i, j, self))
            self.grid.append(temp_list[:])
            temp_list.clear()

        self.set_source_node(0, 0)
        self.set_end_node(self.col_num - 1, self.row_num - 1)

    def change_size(self, col_num, row_num):
        self.ui.change_grid_size(col_num, row_num)
        self.col_num = col_num
        self.row_num = row_num
        self.construct()

    def set_source_node(self, i, j):
        self.ui.clear_by_tag("source")
        self.source_node = self.grid[i][j]
        self.source_node.set_color("green", "source")
        self.source_node.is_blocked = False

    def set_end_node(self, i, j):
        self.ui.clear_by_tag("end")
        self.end_node = self.grid[i][j]
        self.end_node.set_color("black", "end")
        self.end_node.is_blocked = False

    def set_node_state(self, i, j, weight, color):
        node = self.grid[i][j]
        if node == self.source_node or node == self.end_node:
            return
        if weight > 2:
            node.is_blocked = True
        else:
            node.weight = weight
            node.is_blocked = False

        node.set_color(color)

    def __getitem__(self, index):
        return self.grid[index]
