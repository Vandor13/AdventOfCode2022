from AoCGui import AoCGui

EXAMPLE_DATA = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""


class CRTube(AoCGui):
    def __init__(self):
        super().__init__()
        self.cycle_number = 0
        self.register = 1
        self.checkpoints = [20, 60, 100, 140, 180, 220]
        self.result_sum = 0
        self.picture = ""
        self.prepare_gui("Day 10: Cathode-Ray Tube", "Calculate Signal Strength", EXAMPLE_DATA)

    def button_pressed(self):
        self.load_text_box_data()
        self.data_lines.pop()

        if self.part.get() == 1:
            self.part_one()
        else:
            self.part_two()

    def part_one(self):
        while len(self.data_lines) > 0 and len(self.checkpoints) > 0:
            self.process_command(self.data_lines.pop(0))
        self.write_result(f"End sum: {self.result_sum}")

    def part_two(self):
        while len(self.data_lines) > 0:
            self.process_command_2(self.data_lines.pop(0))
        self.write_result(self.picture)

    def process_command(self, command: str):
        if command == "noop":
            self.tick_cycle()
        else:
            summand = int(command.split(" ")[1])
            self.tick_cycle()
            self.tick_cycle()
            self.register += summand

    def tick_cycle(self):
        self.cycle_number += 1
        # print(f"Cycle: {self.cycle_number}, Register: {self.register}")
        if self.cycle_number in self.checkpoints:
            signal_strength = self.cycle_number * self.register
            self.result_sum += signal_strength
            self.checkpoints.remove(self.cycle_number)
            print(f"Cycle Number: {self.cycle_number}. Register: {self.register}. Current Signal strength: {signal_strength}. New sum: {self.result_sum}")

    def process_command_2(self, command: str):
        if command == "noop":
            self.tick_cycle_2()
        else:
            summand = int(command.split(" ")[1])
            self.tick_cycle_2()
            self.tick_cycle_2()
            self.register += summand

    def tick_cycle_2(self):
        self.cycle_number += 1
        pixel_position = (self.cycle_number - 1) % 40
        if self.register - 1 <= pixel_position <= self.register + 1:
            self.picture = self.picture + "#"
        else:
            self.picture = self.picture + "."
        if pixel_position == 39:
            self.picture = self.picture + "\n"


if __name__ == "__main__":
    syntax_scorer = CRTube()
