from AoCGui import AoCGui

EXAMPLE_DATA = """A Y
B X
C Z"""

sign_values = {
    "A": 1,  # Rock
    "B": 2,  # Paper
    "C": 3,  # Scissors
    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3  # Scissors
}

value_translation = {
    0: "C",
    1: "A",
    2: "B",
    3: "C",
    4: "A"
}

sign_translation = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}

outcome_values = {
    0: 3,  # Draw
    -1: 6,  # Won
    1: 0,  # lose
    -2: 0,  # lose
    2: 6  # win
}

sign_change = {
    "X": -1,
    "Y": 0,
    "Z": 1
}


class RockPaperScissors(AoCGui):
    def __init__(self):
        super().__init__()
        self.prepare_gui("Day 2: Rock Paper Scissors", "Calculate Score", EXAMPLE_DATA)

    def button_pressed(self):
        self.load_text_box_data()
        self.data_lines.pop()
        if self.part.get() == 1:
            self.play_rps()
        else:
            self.play_rps_targeted()

    def play_rps(self):
        score = 0
        for game in self.data_lines:
            elf_sign, my_sign = str(game).split(" ")
            game_score = game_value(elf_sign, my_sign)
            score += game_score
            print(f"{sign_translation[elf_sign]} vs {sign_translation[my_sign]}: Score: {game_score}, Total: {score}")
        self.write_result(f"The final score is: {score}")

    def play_rps_targeted(self):
        score = 0
        for game in self.data_lines:
            elf_sign, result = str(game).split(" ")
            my_sign = choose_sign(elf_sign, result)
            game_score = game_value(elf_sign, my_sign)
            score += game_score
            print(f"{sign_translation[elf_sign]} vs {sign_translation[my_sign]}: Score: {game_score}, Total: {score}")
        self.write_result(f"The final score is: {score}")


def game_value(elf_sign, my_sign):
    sign_value = sign_values[my_sign]
    outcome = sign_values[elf_sign] - sign_values[my_sign]
    outcome_value = outcome_values[outcome]
    return sign_value + outcome_value


def choose_sign(elf_sign, result):
    needed_change = sign_change[result]
    my_sign = sign_values[elf_sign] + needed_change
    return value_translation[my_sign]


if __name__ == "__main__":
    rps = RockPaperScissors()
