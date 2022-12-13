import sys
from pathlib import Path
from typing import List, Any


def parse_input(puzzle_input_file_path: Path) -> List[List[Any]]:
    """Parse input data."""

    text: str = puzzle_input_file_path.read_text().strip()
    # replace '\n\n' with '|' and '\n' with ','
    text = text.replace("\n\n", "|").replace("\n", ",")
    pairs = text.split("|")
    return [list(eval(x)) for x in pairs]


def solve_part_1(puzzle_input_file_path: Path) -> int:
    """
    Solve part 1:
    """

    data: List[str] = parse_input(puzzle_input_file_path)

    return 0


def solve_part_2(puzzle_input_file_path: Path) -> int:
    """
    Solve part 2:
    """

    data: List[str] = parse_input(puzzle_input_file_path)

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
