import sys
from pathlib import Path
from typing import Any, List, Tuple

import numpy as np


def parse_input(puzzle_input_file_path: Path) -> np.ndarray:
    """Parse input data."""

    matrix: np.ndarray = np.empty(0, dtype=str)
    with puzzle_input_file_path.open() as f:
        # read line by line
        for line in f:
            # numpy array for the line
            array_line: np.ndarray = np.array([list(line.strip())])
            # concatinae each line's numpy array into matrix.
            matrix = (
                np.concatenate((matrix, array_line), axis=0)
                if matrix.size > 0
                else array_line
            )

    return matrix.astype(int)


def solve_part_1(puzzle_input_file_path: Path) -> int:
    """
    Solve part 1:
    """

    data: List[Tuple[str, str]] = parse_input(puzzle_input)
    total_score: int = 0
    # Calculate the total score
    for i in data:
        pass

    return total_score


def solve_part_2(puzzle_input_file_path: Path) -> int:
    """
    Solve part 2:
    """

    data: List[Tuple[str, str]] = parse_input(puzzle_input)
    total_score: int = 0
    # Calculate the total score
    for i in data:
        pass

    return total_score


def solve_puzzle(puzzle_input_file_path: Path):
    """Solve the Advent of Code puzzle of the day."""

    solution_1 = solve_part_1(puzzle_input_file_path)
    solution_2 = solve_part_2(puzzle_input_file_path)

    return solution_1, solution_2


if __name__ == "__main__":
    # Read input data
    puzzle_input = Path(sys.argv[1]).read_text().strip()

    # Solve the puzzle
    solution_1, solution_2 = solve_puzzle(puzzle_input)

    # Print the solutions
    print(f"Solution 1: {solution_1}")
    print(f"Solution 2: {solution_2}")
