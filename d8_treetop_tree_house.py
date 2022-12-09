from AoCGui import AoCGui

EXAMPLE_DATA = """30373
25512
65332
33549
35390"""


class TreetopTreeHouse(AoCGui):
    def __init__(self):
        super().__init__()
        self.forest = []
        self.seen_trees = set()
        self.prepare_gui("Day 8: Treetop Tree House", "Count Trees", EXAMPLE_DATA)

    def button_pressed(self):
        self.load_text_box_data()
        self.data_lines.pop()
        self.load_forest()
        if self.part.get() == 1:
            self.part_one()
        else:
            self.part_two()

    def part_one(self):
        self.seen_trees.clear()
        self.find_trees_left_and_right()
        self.find_trees_up_and_down()
        # print(sorted(self.seen_trees))
        # print(len(self.seen_trees))
        self.write_result(f"Number of seen trees: {len(self.seen_trees)}")


    def find_trees_left_and_right(self):
        for row_index in range(len(self.forest)):
            # Find trees from left to right
            highest_tree = -1
            column_index = 0
            length_of_row = len(self.forest[row_index])
            while column_index < length_of_row:
                if self.forest[row_index][column_index] > highest_tree:
                    highest_tree = self.forest[row_index][column_index]
                    self.seen_trees.add((row_index, column_index))
                column_index += 1
            # print(self.seen_trees)
            # Find trees from right to left
            highest_tree = -1
            length_of_row = len(self.forest[row_index])
            column_index = length_of_row - 1
            while column_index >= 0:
                if self.forest[row_index][column_index] > highest_tree:
                    highest_tree = self.forest[row_index][column_index]
                    self.seen_trees.add((row_index, column_index))
                column_index -= 1
            # print(self.seen_trees)

    def find_trees_up_and_down(self):
        for column_index in range(len(self.forest[0])):
            # Find trees from up to down
            highest_tree = -1
            row_index = 0
            length_of_column = len(self.forest)
            while row_index < length_of_column:
                if self.forest[row_index][column_index] > highest_tree:
                    highest_tree = self.forest[row_index][column_index]
                    self.seen_trees.add((row_index, column_index))
                # print((row_index, column_index))
                row_index += 1
            # print(self.seen_trees)
            # Find trees from down to up
            highest_tree = -1
            row_index = length_of_column - 1
            while row_index >= 0:
                if self.forest[row_index][column_index] > highest_tree:
                    highest_tree = self.forest[row_index][column_index]
                    self.seen_trees.add((row_index, column_index))
                # print((row_index, column_index))
                row_index -= 1
            # print(self.seen_trees)

    def part_two(self):
        best_scenic_score = -1
        best_tree = None
        for row in range(1, len(self.forest)-1):
            for column in range(1, len(self.forest[0])-1):
                scenic_score = self.calculate_scenic_score(row, column)
                if scenic_score > best_scenic_score:
                    best_scenic_score = scenic_score
                    best_tree = (row, column)
        self.write_result(f"Best scenic score: {best_scenic_score} for tree {best_tree}")

    def calculate_scenic_score(self, row, column):
        treehouse_height = self.forest[row][column]
        # search right
        right_view = 0
        for column_index in range(column + 1, len(self.forest[0])):
            right_view += 1
            if self.forest[row][column_index] >= treehouse_height:
                break
        # search down
        down_view = 0
        for row_index in range(row + 1, len(self.forest)):
            down_view += 1
            if self.forest[row_index][column] >= treehouse_height:
                break
        # search left
        left_view = 0
        for column_index in range(column - 1, -1, -1):
            left_view += 1
            if self.forest[row][column_index] >= treehouse_height:
                break
        # search up
        up_view = 0
        for row_index in range(row - 1, -1, -1):
            up_view += 1
            if self.forest[row_index][column] >= treehouse_height:
                break
        # print(f"Tree at {(row, column)} has view of left {left_view}, right {right_view}, up {up_view}, down {down_view}")
        return left_view * right_view * up_view * down_view

    def load_forest(self):
        for line in self.data_lines:
            tree_row = []
            for tree in line:
                tree_row.append(int(tree))
            self.forest.append(tree_row)


if __name__ == "__main__":
    treehouse = TreetopTreeHouse()
