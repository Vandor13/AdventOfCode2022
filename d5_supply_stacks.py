from AoCGui import AoCGui
import itertools

EXAMPLE_DATA = """    [D]    
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
        self.number_of_stacks = 0
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
        for command in self.data_lines:
            print(command)
            command = str(command)
            command = command.strip("move ")
            command = command.replace("from ", "")
            command = command.replace("to ", "")
            command = command.strip()
            number_of_containers, origin, target = command.split(" ")
            self.make_crate_move(int(origin) - 1, int(target) - 1, int(number_of_containers))
            # print(f"Origin: {origin}, target: {target}, number of containers: {number_of_containers}")
        self.calculate_message()

    def part_two(self):
        self.load_stacks()
        for command in self.data_lines:
            print(command)
            command = str(command)
            command = command.strip("move ")
            command = command.replace("from ", "")
            command = command.replace("to ", "")
            command = command.strip()
            number_of_containers, origin, target = command.split(" ")
            self.make_crate_move_9001(int(origin) - 1, int(target) - 1, int(number_of_containers))
            # print(f"Origin: {origin}, target: {target}, number of containers: {number_of_containers}")
        self.calculate_message()

    def load_stacks(self):
        row = str(self.data_lines.pop(0))
        self.number_of_stacks = (len(row) + 1) // 4
        for number in range(self.number_of_stacks):
            self.stacks.append([])
        while not row.startswith(" 1"):
            print(f"Processing row {row}")
            for stack_number in range(self.number_of_stacks):
                print(f"Adding string field {1 + 4 * stack_number}")
                container = row[1 + 4 * stack_number]
                if container != " ":
                    self.stacks[stack_number].insert(0, container)
                    # print(f"Appended container {container} to stack {stack_number}")
            row = str(self.data_lines.pop(0))
        print(self.stacks)
        self.data_lines.pop(0)

    def make_crate_move(self, origin: int, target: int, number_of_containers: int):
        for i in range(number_of_containers):
            container = self.stacks[origin].pop()
            self.stacks[target].append(container)
        print(self.stacks)

    def make_crate_move_9001(self, origin: int, target: int, number_of_containers: int):
        move_stack = []
        for i in range(number_of_containers):
            container = self.stacks[origin].pop()
            move_stack.append(container)
        for j in range(number_of_containers):
            self.stacks[target].append(move_stack.pop())
        print(self.stacks)

    def calculate_message(self):
        message = ""
        for i in range(self.number_of_stacks):
            message += self.stacks[i].pop()
        self.write_result(message)


if __name__ == "__main__":
    suplly_stacks = SupplyStacks()
