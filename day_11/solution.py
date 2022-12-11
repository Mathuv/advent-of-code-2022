import sys
from pathlib import Path
from typing import List, Dict, Any

import yaml


def parse_input(puzzle_input_file_path: Path) -> Dict[str, Any]:
    """Parse input data."""

    text: str = puzzle_input_file_path.read_text().strip().lower()

    # replace 4 spaces with 2 spaces to may in YAML compliant
    text = text.replace("    ", "  ")
    # replace "divisible by " and "throw to monkey " with "" to make it easy to process
    text = text.replace("divisible by ", "").replace("throw to monkey ", "")
    return yaml.safe_load(text)


def solve_part_1(puzzle_input_file_path: Path) -> int:
    """
    Solve part 1:
    Figure out which monkeys to chase by counting how many
    items they inspect over 20 rounds. What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?
    """

    document: Dict[str, Any] = parse_input(puzzle_input_file_path)

    return 0


def solve_part_2(puzzle_input_file_path: Path) -> int:
    """
    Solve part 2:
    """

    document: str = parse_input(puzzle_input_file_path)

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
