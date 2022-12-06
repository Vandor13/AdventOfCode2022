from AoCGui import AoCGui

EXAMPLE_DATA = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""


class Tuning_Trouble(AoCGui):
    def __init__(self):
        super().__init__()
        self.prepare_gui("Day 6: Tuning Trouble", "Fnd start", EXAMPLE_DATA)

    def button_pressed(self):
        self.load_text_box_data()
        self.data_lines.pop()
        # print(self.data_lines)
        if self.part.get() == 1:
            self.part_one()
        else:
            self.part_two()

    def part_one(self):
        answer = self.find_marker()
        if answer == 0:
            self.write_result(f"Something went wrong")
        else:
            self.write_result(f"Marker ends at: {answer}")

    def part_two(self):
        answer = self.find_start_of_message()
        if answer == 0:
            self.write_result(f"Something went wrong")
        else:
            self.write_result(f"Marker ends at: {answer}")

    def find_marker(self) -> int:
        datastream = self.data_lines.pop()
        buffer = []
        index = 0
        while index < len(datastream):
            new_character = datastream[index]
            if new_character in buffer:
                repeated_index = buffer.index(new_character)
                buffer = buffer[repeated_index + 1:]
                buffer.append(new_character)
            elif len(buffer) < 3:
                buffer.append(new_character)
            else:
                return index + 1
            index += 1
        return 0

    def find_start_of_message(self):
        datastream = self.data_lines.pop()
        buffer = []
        index = 0
        while index < len(datastream):
            new_character = datastream[index]
            if new_character in buffer:
                repeated_index = buffer.index(new_character)
                buffer = buffer[repeated_index + 1:]
                buffer.append(new_character)
            elif len(buffer) < 13:
                buffer.append(new_character)
            else:
                return index + 1
            index += 1
        return 0


if __name__ == "__main__":
    tuning_trouble = Tuning_Trouble()
