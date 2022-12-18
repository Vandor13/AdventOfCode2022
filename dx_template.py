from AoCGui import AoCGui
import itertools

EXAMPLE_DATA = """Player 1 starting position: 4
Player 2 starting position: 8
"""


class ClassName(AoCGui):
    def __init__(self):
        super().__init__()
        self.prepare_gui("Day XX: TITLE", "BUTTON NAME", EXAMPLE_DATA)

    def button_pressed(self):
        self.load_text_box_data()
        self.data_lines.pop()

        if self.part.get() == 1:
            self.part_one()
        else:
            self.part_two()

    def part_one(self):
        pass

    def part_two(self):
        pass


if __name__ == "__main__":
    short_title = ClassName()
