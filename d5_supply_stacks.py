from AoCGui import AoCGui
import itertools

EXAMPLE_DATA = """   [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


class SupplyStacks(AoCGui):
    def __init__(self):
        super().__init__()
        self.stacks = []
        self.prepare_gui("Day 5: Supply Stacks", "Calculate Vents", EXAMPLE_DATA)

    def button_pressed(self):
        self.load_text_box_data()
        self.data_lines.pop()

        if self.part.get() == 1:
            self.part_one()
        else:
            self.part_two()

    def part_one(self):
        self.load_stacks()

    def part_two(self):
        return

    def load_stacks(self):
        row = self.data_lines.pop(0)


if __name__ == "__main__":
    suplly_stacks = SupplyStacks()
