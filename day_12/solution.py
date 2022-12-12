import sys
from pathlib import Path
from typing import List
import numpy as np


def parse_input(puzzle_input_file_path: Path) -> np.ndarray:
    """Parse input data."""

    text: str = puzzle_input_file_path.read_text().strip()

    # Convert the text into numpy array and return
    return np.array([list(line) for line in text.splitlines()])


def solve_part_1(puzzle_input_file_path: Path) -> int:
    """
    Solve part 1:
    """

    grid: np.ndarray = parse_input(puzzle_input_file_path)

    return 0


def solve_part_2(puzzle_input_file_path: Path) -> int:
    """
    Solve part 2:
    """

    grid: np.ndarray = parse_input(puzzle_input_file_path)

    return 0


def solve_puzzle(puzzle_input_file_path: Path):
    """
    Solve the Advent of Code puzzle of the day.
    Day 12: Hill Climbing Algorithm
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
