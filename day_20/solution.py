import sys
from pathlib import Path
from typing import List, Tuple
from icecream import ic


def parse_input(puzzle_input_file_path: Path) -> List[int]:
    """Parse input data."""

    text = puzzle_input_file_path.read_text().strip()

    return [int(line) for line in text.splitlines()]


def get_sum_of_three_numbers(coordinates: List[int]) -> int:

    return 0


def solve_part_1(puzzle_input_file_path: Path) -> int:
    """
    Solve part 1:
    Mix your encrypted file exactly once. **What is the sum of
    the three numbers that form the grove coordinates?**
    """

    coordinates: List[int] = parse_input(puzzle_input_file_path)

    return get_sum_of_three_numbers(coordinates)


def solve_part_2(puzzle_input_file_path: Path) -> int:
    """
    Solve part 2:
    """

    coordinates: List[int] = parse_input(puzzle_input_file_path)

    return 0


def solve_puzzle(puzzle_input_file_path: Path):
    """
    Solve the Advent of Code puzzle of the day.
    --- Day 20: Grove Positioning System ---
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
