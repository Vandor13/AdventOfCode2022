from AoCGui import AoCGui

EXAMPLE_DATA = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


class CampCleanup(AoCGui):
    def __init__(self):
        super().__init__()
        self.prepare_gui("Day 4: Camp Cleanup", "Calculate Sectors", EXAMPLE_DATA)

    def button_pressed(self):
        self.load_text_box_data()
        self.data_lines.pop()

        if self.part.get() == 1:
            self.part_one()
        else:
            self.part_two()

    def part_one(self):
        number_of_full_contains = 0
        for elf_pair in self.data_lines:
            elf1, elf2 = elf_pair.split(",")
            elf1start, elf1end = elf1.split("-")
            elf2start, elf2end = elf2.split("-")
            if range_fully_contained(int(elf1start), int(elf1end), int(elf2start), int(elf2end)):
                number_of_full_contains += 1
                print(f"{elf_pair} are fully containing each other")
        self.write_result(f"Number of full contains: {number_of_full_contains}")

    def part_two(self):
        number_of_overlaps = 0
        for elf_pair in self.data_lines:
            elf1, elf2 = elf_pair.split(",")
            elf1start, elf1end = elf1.split("-")
            elf2start, elf2end = elf2.split("-")
            if range_fully_contained(int(elf1start), int(elf1end), int(elf2start), int(elf2end)) or \
                    (ranges_partly_overlap(int(elf1start), int(elf1end), int(elf2start), int(elf2end))):
                number_of_overlaps += 1
                print(f"{elf_pair} are overlaping")
        self.write_result(f"Number of overlaping areas: {number_of_overlaps}")


def range_fully_contained(x1, x2, y1, y2) -> bool:
    if (x1 <= y1 and x2 >= y2) or (y1 <= x1 and y2 >= x2):
        return True
    else:
        return False
    
    
def ranges_partly_overlap(x1, x2, y1, y2) -> bool:
    if (x1 <= y1 <= x2) or (x1 <= y2 <= x2):
        return True
    else:
        return False


if __name__ == "__main__":
    cleanup = CampCleanup()
