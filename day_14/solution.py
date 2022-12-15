import sys
from pathlib import Path
from typing import List, Tuple
from icecream import ic

ROCK: str = "#"
AIR: str = "."
SAND_SOURCE: str = "+"
SAND_AT_REST: str = "o"


def parse_input(puzzle_input_file_path: Path) -> List[List[Tuple[int, int]]]:
    """Parse input data."""

    text: str = puzzle_input_file_path.read_text().strip()

    # Split/convert text into list of lists of tuples of integers.
    cordinates: List[List[Tuple[int, int]]] = [
        # [eval(c) for c in line.split(" -> ")] for line in text.splitlines()
        # Swap the cordinated to represet in a numpy array rows and columns.
        [(eval(c)[1], eval(c)[0]) for c in line.split(" -> ")]
        for line in text.splitlines()
    ]
    ic(cordinates)

    return cordinates


def solve_part_1(puzzle_input_file_path: Path) -> int:
    """
    Solve part 1:
    Using your scan, simulate the falling sand.
    How many units of sand come to rest before sand starts flowing into the abyss below?
    """

    cordinates: List[List[Tuple[int, int]]] = parse_input(puzzle_input_file_path)

    return 0


def solve_part_2(puzzle_input_file_path: Path) -> int:
    """
    Solve part 2:
    """

    cordinates: List[List[Tuple[int, int]]] = parse_input(puzzle_input_file_path)

    return 0


def solve_puzzle(puzzle_input_file_path: Path):
    """
    Solve the Advent of Code puzzle of the day.
    Day 14: Regolith Reservoir
    """

    solution_1 = solve_part_1(puzzle_input_file_path)
    solution_2 = solve_part_2(puzzle_input_file_path)

    return solution_1, solution_2


if __name__ == "__main__":
    # Read input data
    puzzle_input_file_path: Path = Path(sys.argv[1])

    # Solve the puzzle
    solution_1, solution_2 = solve_puzzle(puzzle_input_file_path)

    # Print the solutions
    print(f"Solution 1: {solution_1}")
    print(f"Solution 2: {solution_2}")
