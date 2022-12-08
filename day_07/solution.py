import pathlib
import sys
from typing import Any, Dict, Generator, List, Tuple

from dir_tree import Dir, File


class recursionlimit:
    def __init__(self, limit):
        self.limit = limit

    def __enter__(self):
        self.old_limit = sys.getrecursionlimit()
        sys.setrecursionlimit(self.limit)

    def __exit__(self, type, value, tb):
        sys.setrecursionlimit(self.old_limit)


def construct_directory_tree(data: List[str]) -> Dict[str, Dir | File]:
    """Construct a directory tree from the input data."""

    # hash table to store the directories and files
    dir_table_map: Dict[str, Dir | File] = {}

    # Create the root directory
    root_dir: Dir = Dir("/")
    dir_table_map["/"] = root_dir

    # Current directory
    current_dir = root_dir
    current_dir_name = "/"

    # Add the directories and files to the directory tree based on cd and ls commands
    for i, line in enumerate(data):
        assert current_dir is not None, f"current_dir is None at line {i}"
        words: List[str] = line.split(" ")
        # Check if the line is a command
        if words[0] == "$":
            # cd command
            if words[1] == "cd":
                if words[2] == "/":
                    continue  # root directory is already created
                # cd to parent directory
                elif words[2] == "..":
                    current_dir_name = current_dir_name.rsplit("/", 2)[0] + "/"
                    current_dir = current_dir.parent or current_dir
                # cd to child directory
                else:
                    current_dir_name += words[2] + "/"
                    current_dir = dir_table_map.get(current_dir_name, None) or Dir(
                        current_dir_name, parent=current_dir
                    )
                    dir_table_map[current_dir_name] = current_dir
            # ls command
            elif words[1] == "ls":
                continue

        # Check if the line is a directory
        elif words[0] == "dir":
            directory_name = current_dir_name + words[1] + "/"
            directory = dir_table_map.get(directory_name, None) or Dir(
                directory_name, parent=current_dir
            )
            # add the directory to the current directory
            current_dir.add_child(directory)
            dir_table_map[directory_name] = directory
        # Line is a file
        else:
            file_name = current_dir_name + words[1]
            file = dir_table_map.get(file_name, None) or File(
                file_name, int(words[0]), parent=current_dir
            )
            # add the file to the current directory
            current_dir.add_child(file)
            dir_table_map[file_name] = file

    return dir_table_map


def parse_input(puzzle_input: str) -> List[Any]:
    """Parse input data."""

    puzzle_input = puzzle_input.strip()
    # Split the input into lines
    lines: List[str] = puzzle_input.splitlines()

    return lines


def solve_part_1(puzzle_input: str) -> int:
    """
    Solve part 1:
    Find all of the directories with a total size of at most 100000.
    What is the sum of the total sizes of those directories?
    """

    data: List[str] = parse_input(puzzle_input)
    dir_file_map: Dict[str, Dir | File] = construct_directory_tree(data)

    dir_sizes: Generator[int, None, None] = (
        dir.size
        for dir in dir_file_map.values()
        if dir.type == "dir" and dir.size <= 100000
    )
    total_size: int = sum(dir_sizes)

    return total_size


def solve_part_2(puzzle_input: str) -> int:
    """
    Solve part 2:
    """

    data: List[Tuple[str, str]] = parse_input(puzzle_input)
    total_score: int = 0
    # Calculate the total score
    for i in data:
        pass

    return total_score


def solve_puzzle(puzzle_input):
    """Solve the Advent of Code puzzle of the day."""

    solution_1 = solve_part_1(puzzle_input)
    solution_2 = solve_part_2(puzzle_input)

    return solution_1, solution_2


if __name__ == "__main__":
    # Read input data
    puzzle_input = pathlib.Path(sys.argv[1]).read_text().strip()

    # Solve the puzzle
    solution_1, solution_2 = solve_puzzle(puzzle_input)

    # Print the solutions
    print(f"Solution 1: {solution_1}")
    print(f"Solution 2: {solution_2}")
