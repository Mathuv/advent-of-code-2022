from typing import List, Tuple, Any
import pathlib
import sys


def parse_input(puzzle_input: str) -> List[Any]:
    """Parse input data."""

    # Split the input into lines
    lines: List[str] = puzzle_input.splitlines()

    # Further process the lines
    data: List[Any] = lines

    return data


def solve_part_1(puzzle_input: str) -> int:
    """
    Solve part 1:
    Find all of the directories with a total size of at most 100000.
    What is the sum of the total sizes of those directories?
    """

    data: List[Tuple[str, str]] = parse_input(puzzle_input)
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
