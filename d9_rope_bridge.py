from AoCGui import AoCGui
import math

EXAMPLE_DATA = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

MOVEMENTS = {
    "R": (1, 0),
    "U": (0, 1),
    "L": (-1, 0),
    "D": (0, -1)
}


class RopeBridge(AoCGui):
    def __init__(self):
        super().__init__()
        self.visited_positions = set()
        self.number_of_knots = 1
        self.knot_positions = []
        self.prepare_gui("Day 9: Rope Bridge", "Calculate positions", EXAMPLE_DATA)

    def button_pressed(self):
        self.load_text_box_data()
        self.data_lines.pop()
        if self.part.get() == 1:
            self.part_one()
        else:
            self.part_two()

    def part_one(self):
        self.execute_moves()
        self.write_result(f"Number of unique positions: {len(self.visited_positions)}")

    def part_two(self):
        self.number_of_knots = 9
        self.execute_moves()
        self.write_result(f"Number of unique positions: {len(self.visited_positions)}")

    def execute_moves(self):
        self.visited_positions.clear()
        self.visited_positions.add((0, 0))
        for _ in range(self.number_of_knots + 1):
            self.knot_positions.append((0, 0))
        for move in self.data_lines:
            direction, steps = move.split(" ")
            self.move_knots(direction, int(steps))

    def move_knots(self, direction: str, steps: int):
        step_value = MOVEMENTS[direction]
        for _ in range(steps):
            self.knot_positions[0] = (self.knot_positions[0][0] + step_value[0], self.knot_positions[0][1] + step_value[1])
            for i in range(1, self.number_of_knots + 1):
                self.update_knot_positions(i)
                # print(f"Tail: {self.tail_position}, Head: {self.head_distance}")
            self.visited_positions.add(self.knot_positions[self.number_of_knots])

    def update_knot_positions(self, knot_number):
        distance = (
            self.knot_positions[knot_number - 1][0] - self.knot_positions[knot_number][0],
            self.knot_positions[knot_number - 1][1] - self.knot_positions[knot_number][1],
        )
        if abs(distance[0]) > 1 or abs(distance[1]) > 1:
            necessary_move = (divide_by_2(distance[0]), divide_by_2(distance[1]))
            # print(f"Due to distance {distance} making move: {necessary_move}")
            self.knot_positions[knot_number] = (self.knot_positions[knot_number][0] + necessary_move[0],
                                                self.knot_positions[knot_number][1] + necessary_move[1])


def divide_by_2(value: int) -> int:
    if value > 0:
        return math.ceil(value / 2)
    else:
        return math.floor(value / 2)


if __name__ == "__main__":
    rope_bridge = RopeBridge()
