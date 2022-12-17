import sys
from pathlib import Path
from typing import List


def parse_input(puzzle_input_file_path: Path) -> List[str]:
    """Parse input data."""

    text: str = puzzle_input_file_path.read_text().strip()
    # Remove unwanted strings form text
    text: str = (
        text.replace("Sensor at x=", "")
        .replace("y=", "")
        .replace(" closest beacon is at x=", "")
    )
    positions = [[eval(pos) for pos in line.split(":")] for line in text.splitlines()]

    return positions


def solve_part_1(puzzle_input_file_path: Path) -> int:
    """
    Solve part 1:
    Consult the report from the sensors you just deployed.
    In the row where y=2000000, how many positions cannot contain a beacon?
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
    """
    Solve the Advent of Code puzzle of the day.
    --- Day 15: Beacon Exclusion Zone ---
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
