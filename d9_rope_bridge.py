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
        self.positions = set()
        self.tail_position = (0, 0)
        self.head_distance = (0, 0)
        self.prepare_gui("Day 9: Rope Bridge", "Calculate positions", EXAMPLE_DATA)

    def button_pressed(self):
        self.load_text_box_data()
        self.data_lines.pop()
        if self.part.get() == 1:
            self.part_one()
        else:
            self.part_two()

    def part_one(self):
        self.positions.add(self.tail_position)
        for move in self.data_lines:
            direction, steps = move.split(" ")
            self.move_head(direction, int(steps))
        self.write_result(f"Number of unique positions: {len(self.positions)}")

    def part_two(self):
        pass

    def move_head(self, direction: str, steps: int):
        step_value = MOVEMENTS[direction]
        for _ in range(steps):
            self.head_distance = (self.head_distance[0] + step_value[0], self.head_distance[1] + step_value[1])
            self.move_tail()
            print(f"Tail: {self.tail_position}, Head: {self.head_distance}")

    def move_tail(self):
        if abs(self.head_distance[0]) > 1 or abs(self.head_distance[1]) > 1:
            necessary_move = (divide_by_2(self.head_distance[0]), divide_by_2(self.head_distance[1]))
            # print(f"Due to distance {self.head_distance} making move: {necessary_move}")
            self.tail_position = (self.tail_position[0] + necessary_move[0], self.tail_position[1] + necessary_move[1])
            self.head_distance = (self.head_distance[0] - necessary_move[0], self.head_distance[1] - necessary_move[1])
            self.positions.add(self.tail_position)


def divide_by_2(value: int) -> int:
    if value > 0:
        return math.ceil(value / 2)
    else:
        return math.floor(value / 2)


if __name__ == "__main__":
    rope_bridge = RopeBridge()
