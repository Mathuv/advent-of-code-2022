import pathlib
import sys
from typing import Any, List, Tuple

import pandas as pd


def parse_input(puzzle_input: str) -> List[Any]:
    """Parse input data."""

    # replace the following characters
    # "[" -> " "
    # "]" -> " "
    # "move" -> ""
    # "from" -> ""
    # "to" -> ""
    puzzle_input = (
        puzzle_input.replace("[", " ")
        .replace("]", " ")
        .replace("move", "")
        .replace("from", "")
        .replace("to", "")
    )

    # Split the text into two section by empty line
    data: List[str] = [i.strip() for i in puzzle_input.split("\n\n")]

    return data


def solve_part_1(puzzle_input: str) -> int:
    """
    Solve part 1:
    After the rearrangement procedure completes, what crate ends up on top of each stack?
    """

    data: List[str] = parse_input(puzzle_input)
    total_score: int = 0
    # Calculate the total score
    for i in data:
        pass

    return total_score


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
