import sys
from pathlib import Path
from typing import Tuple, List
import itertools

import numpy as np


def parse_input(puzzle_input_file_path: Path) -> List[str]:
    """Parse input data."""

    return puzzle_input_file_path.read_text().strip().splitlines()


def solve_part_1(puzzle_input_file_path: Path) -> int:
    """
    Solve part 1:
    Simulate your complete hypothetical series of motions.
    How many positions does the tail of the rope visit at least once?
    """

    motions: List[str] = parse_input(puzzle_input_file_path)

    return 0


def solve_part_2(puzzle_input_file_path: Path) -> int:
    """
    Solve part 2:
    """

    motions: List[str] = parse_input(puzzle_input_file_path)

    return 0


def solve_puzzle(puzzle_input_file_path: Path):
    """Solve the Advent of Code puzzle of the day."""

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
