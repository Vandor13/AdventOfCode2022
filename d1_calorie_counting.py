from AoCGui import AoCGui

EXAMPLE_DATA = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

class SonarSweep(AoCGui):
    def __init__(self):
        super().__init__()
        self.elves = []
        self.prepare_gui("Day 1: Calorie Counting", "Find Elf", EXAMPLE_DATA)

    def button_pressed(self):
        self.load_text_box_data()
        self.data_lines.pop()
        self.load_elves()
        if self.part.get() == 1:
            self.find_elf()
        else:
            self.find_top3_elves()

    def load_elves(self):
        elf = []
        for calorie_count in self.data_lines:
            if calorie_count == "":
                self.elves.append(elf)
                elf = []
            else:
                elf.append(int(calorie_count))
        self.elves.append(elf)
        print(self.elves)

    def find_elf(self):
        highest_calorie_count = 0
        for elf in self.elves:
            calorie_count = sum(elf)
            highest_calorie_count = max(highest_calorie_count, calorie_count)
        self.write_result(highest_calorie_count)

    def find_top3_elves(self):
        highest_calorie_count = [0, 0, 0]
        for elf in self.elves:
            calorie_count = sum(elf)
            highest_calorie_count.append(calorie_count)
            highest_calorie_count = sorted(highest_calorie_count, reverse=True)[:3]
        self.write_result(sum(highest_calorie_count))


if __name__ == "__main__":
    sonar_sweep = SonarSweep()
