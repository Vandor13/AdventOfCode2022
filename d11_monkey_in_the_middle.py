from AoCGui import AoCGui
import itertools
import math

EXAMPLE_DATA = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


class MonkeyGame(AoCGui):
    def __init__(self):
        super().__init__()
        self.monkey_handler = MonkeyHandler()
        self.prepare_gui("Day 11: Monkey in the Middle", "Find Monkeys", EXAMPLE_DATA)

    def button_pressed(self):
        self.load_text_box_data()
        self.data_lines.pop()

        if self.part.get() == 1:
            self.part_one()
        else:
            self.part_two()

    def part_one(self):
        self.monkey_handler.adopt_monkeys_example()
        for i in range(20):
            self.monkey_handler.play_round()
        inspections = self.monkey_handler.get_all_inspection_no()
        print(inspections)
        inspections.sort(reverse=True)
        print(f"Monkey business: {inspections[0] * inspections[1]}")

    def part_two(self):
        self.monkey_handler.adopt_monkeys_input()
        self.monkey_handler.remove_worry_reduction()
        # lcm = math.lcm(23, 19, 13, 17)
        lcm = math.lcm(7, 3, 2, 11, 17, 5, 13, 19)
        self.monkey_handler.set_lcm(lcm)
        for i in range(10000):
            print(f"Round {i}")
            self.monkey_handler.play_round()
        inspections = self.monkey_handler.get_all_inspection_no()
        print(inspections)
        inspections.sort(reverse=True)
        print(inspections)
        print(f"Monkey business: {inspections[0] * inspections[1]}")


class MonkeyHandler:
    def __init__(self):
        super().__init__()
        self.monkeys = []

    def get_all_inspection_no(self) -> list[int]:
        inspections = []
        for monkey in self.monkeys:
            inspections.append(monkey.inspections)
        return inspections

    def remove_worry_reduction(self):
        for monkey in self.monkeys:
            monkey.worry_reduction = False

    def set_lcm(self, lcm):
        for monkey in self.monkeys:
            monkey.lcm = lcm

    def play_round(self):
        for monkey_no in range(len(self.monkeys)):
            # print(f"Monkey {monkey_no}")
            monkey = self.monkeys[monkey_no]
            monkey.inspect_items()

    def adopt_monkeys_example(self):
        for i in range(4):
            self.monkeys.append(Monkey())
        self.monkeys[0].set_variables(
            "Monkey 0",
            [79, 98],
            lambda x: x * 19,
            lambda x: x % 23 == 0,
            self.monkeys[2],
            self.monkeys[3]
        )
        self.monkeys[1].set_variables(
            "Monkey 1",
            [54, 65, 75, 74],
            lambda x: x + 6,
            lambda x: x % 19 == 0,
            self.monkeys[2],
            self.monkeys[0]
        )
        self.monkeys[2].set_variables(
            "Monkey 2",
            [79, 60, 97],
            lambda x: x * x,
            lambda x: x % 13 == 0,
            self.monkeys[1],
            self.monkeys[3]
        )
        self.monkeys[3].set_variables(
            "Monkey 3",
            [74],
            lambda x: x + 3,
            lambda x: x % 17 == 0,
            self.monkeys[0],
            self.monkeys[1]
        )

    def adopt_monkeys_input(self):
        for i in range(8):
            self.monkeys.append(Monkey())
        self.monkeys[0].set_variables(
            "Monkey 0",
            [91, 58, 52, 69, 95, 54],
            lambda x: x * 13,
            lambda x: x % 7 == 0,
            self.monkeys[1],
            self.monkeys[5]
        )
        self.monkeys[1].set_variables(
            "Monkey 1",
            [80, 80, 97, 84],
            lambda x: x * x,
            lambda x: x % 3 == 0,
            self.monkeys[3],
            self.monkeys[5]
        )
        self.monkeys[2].set_variables(
            "Monkey 2",
            [86, 92, 71],
            lambda x: x + 7,
            lambda x: x % 2 == 0,
            self.monkeys[0],
            self.monkeys[4]
        )
        self.monkeys[3].set_variables(
            "Monkey 3",
            [96, 90, 99, 76, 79, 85, 98, 61],
            lambda x: x + 4,
            lambda x: x % 11 == 0,
            self.monkeys[7],
            self.monkeys[6]
        )
        self.monkeys[4].set_variables(
            "Monkey 4",
            [60, 83, 68, 64, 73],
            lambda x: x * 19,
            lambda x: x % 17 == 0,
            self.monkeys[1],
            self.monkeys[0]
        )
        self.monkeys[5].set_variables(
            "Monkey 5",
            [96, 52, 52, 94, 76, 51, 57],
            lambda x: x + 3,
            lambda x: x % 5 == 0,
            self.monkeys[7],
            self.monkeys[3]
        )
        self.monkeys[6].set_variables(
            "Monkey 6",
            [75],
            lambda x: x + 5,
            lambda x: x % 13 == 0,
            self.monkeys[4],
            self.monkeys[2]
        )
        self.monkeys[7].set_variables(
            "Monkey 7",
            [83, 75],
            lambda x: x + 1,
            lambda x: x % 19 == 0,
            self.monkeys[2],
            self.monkeys[6]
        )


class Monkey:
    def __init__(self):
        self.inspections = 0
        self.worry_reduction = True
        self.lcm = 0

    def set_variables(self, name, items, operations, test, monkey1, monkey2):
        self.name = name
        self.items = items
        self.operation = operations
        self.test = test
        self.monkey1: Monkey = monkey1
        self.monkey2: Monkey = monkey2

    def inspect_items(self):
        for i in range(len(self.items)):
            worry_level = self.items.pop(0)
            self.inspections += 1
            # print(f"Monkey inspects an item with a worry level of {worry_level}")
            worry_level = self.operation(worry_level)
            if self.lcm > 1:
                worry_level = worry_level % self.lcm
            # print(f"Worry level increases to {worry_level}")
            if self.worry_reduction:
                worry_level = worry_level // 3
                # print(f"Monkey gets bored with item. Worry level is divided by 3 to {worry_level}")
            if (self.test(worry_level)):
                self.monkey1.items.append(worry_level)
                # print(f"Item given to {self.monkey1.name}")
            else:
                self.monkey2.items.append(worry_level)
                # print(f"Item given to {self.monkey2.name}")
            # print("-------------------------")



if __name__ == "__main__":
    short_title = MonkeyGame()
