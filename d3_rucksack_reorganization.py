from AoCGui import AoCGui

EXAMPLE_DATA = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


class RucksackReorganization(AoCGui):
    def __init__(self):
        super().__init__()

        self.prepare_gui("Day 3: Rucksack Reorganization", "Calculate Item Priorities", EXAMPLE_DATA)

    def button_pressed(self):
        super().button_pressed()
        if self.part.get() == 1:
            self.calculate_1()
        else:
            self.calculate_2()

    def calculate_1(self):
        sum_of_prio = 0
        for rucksack in self.data_lines:
            rucksack = str(rucksack)
            compartment1 = rucksack[: len(rucksack) // 2]
            compartment2 = rucksack[len(rucksack) // 2:]
            wrong_item = ""
            for character in compartment1:
                if compartment2.count(character) > 0:
                    wrong_item = character
                    break
            sum_of_prio += get_priority(wrong_item)
        self.write_result(f"Sum of Priorities: {sum_of_prio}")

    def calculate_2(self):
        sum_of_prio = 0
        while len(self.data_lines) > 0:
            elf1 = self.data_lines.pop(0)
            print(f"Elf 1: {elf1}")
            elf2 = self.data_lines.pop(0)
            print(f"Elf 2: {elf2}")
            elf3 = self.data_lines.pop(0)
            print(f"Elf 3: {elf3}")
            common_item = ""
            for character in elf1:
                if (elf2.count(character) > 0) and (elf3.count(character) > 0):
                    common_item = character
                    break
            print(f"Common item found: {common_item}")
            sum_of_prio += get_priority(common_item)
            print(f"New sum: {sum_of_prio}")
        self.write_result(f"Sum of Priorities: {sum_of_prio}")



def get_priority(item: str):
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 64 + 26


if __name__ == "__main__":
    organizer = RucksackReorganization()
