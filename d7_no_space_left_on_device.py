from AoCGui import AoCGui
import statistics

EXAMPLE_DATA = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


class NoSpace(AoCGui):
    def __init__(self):
        super().__init__()
        self.root = Directory("root", None)
        self.current_directory = self.root
        self.sum_of_small_dirs = 0
        self.prepare_gui("Day 7: No Space Left on Device", "Find Directories", EXAMPLE_DATA)

    def button_pressed(self):
        self.load_text_box_data()
        self.data_lines.pop()
        self.calculate_answer()

    def calculate_answer(self):
        command: str
        while len(self.data_lines) > 0:
            command = self.data_lines.pop(0)
            if command.startswith("$ cd"):
                if command.endswith("/"):
                    self.current_directory = self.root
                elif command.endswith(".."):
                    self.current_directory = self.current_directory.parent
                else:
                    self.current_directory = self.current_directory.dirs[command.split(" ")[2]]
            elif command == "$ ls":
                if (len(self.current_directory.dirs) == 0 and len(self.current_directory.files) == 0) or \
                        (self.current_directory.name == "root"):
                    self.add_items()
                    print(f"Filled directory {self.current_directory.name}, Parent: {self.current_directory.parent}")
                    print(f"--> Directories: {self.current_directory.dirs}, Files: {self.current_directory.files}")
                else:
                    print(f"Directory {self.current_directory.name} was already filled, Parent: "
                          f"{self.current_directory.parent}")
        list_of_sizes: list[int]
        size, sum_of_small_dirs, list_of_sizes = self.root.get_size()
        if size <= 100000:
            sum_of_small_dirs += size
            print(f"   -> Found small directory: {self.root.name} with size {size}")
            print(f"   -> New sum: {sum_of_small_dirs}")
        used_space = size
        print(f"Used space: {used_space}")
        needed_space = used_space - 40000000
        list_of_sizes.sort()
        best_file_size = 0
        print(f"We need {needed_space} of new space")
        print(list_of_sizes)
        for file_size in list_of_sizes:
            if file_size >= needed_space:
                best_file_size = file_size
                print("Found best file!")
                break
        self.write_result(f"Sum of small directories: {sum_of_small_dirs} \n"
                          f"Best File size to delete: {best_file_size}")

    def add_items(self):
        while len(self.data_lines) > 0 and not self.data_lines[0].startswith("$"):
            new_item_string: str
            new_item_string = self.data_lines.pop(0)
            if new_item_string.startswith("dir"):
                new_directory = Directory(new_item_string.split(" ")[1], self.current_directory)
                self.current_directory.add_dir(new_directory)
                # print(f"Added directory {new_directory.name}")
            else:
                file_size, file_name = new_item_string.split(" ")
                self.current_directory.add_file(file_name, file_size)

    def part_two(self):
        pass


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.dirs = {}
        self.files = {}

    def add_file(self, name, size):
        self.files[name] = int(size)

    def add_dir(self, directory):
        self.dirs[directory.name] = directory

    def get_size(self) -> [int, int, list]:
        size = sum(self.files.values())
        list_of_sizes = []
        sum_of_small_dirs = 0
        directory: Directory
        for directory in self.dirs.values():
            directory_size, sum_of_subdir_small_sizes, sublist_of_sizes = directory.get_size()
            size += directory_size
            sum_of_small_dirs += sum_of_subdir_small_sizes
            list_of_sizes.extend(sublist_of_sizes)
        print(f"Directory {self.name} with size {size}")
        list_of_sizes.append(size)
        if size <= 100000:
            sum_of_small_dirs += size
            print(f"   -> Found small directory: {self.name} with size {size}")
        return [size, sum_of_small_dirs, list_of_sizes]

    def __str__(self) -> str:
        return self.name


if __name__ == "__main__":
    device_manager = NoSpace()
