from typing import List, Tuple
import pathlib
import sys


def parse_input(puzzle_input: str) -> str:
    """Parse input data."""

    # strip the input
    puzzle_input = puzzle_input.strip()

    return puzzle_input


def solve_part_1(puzzle_input: str) -> int:
    """
    Solve part 1:
    How many characters need to be processed before the
    first start-of-packet marker is detected?
    """

    data: str = parse_input(puzzle_input)
    char_pos: int = 0

    # find char_pos after first occurence of 4 unique chars occurs.
    for i in range(len(data)):
        if len(set(data[i : i + 4])) == 4:
            char_pos = i + 4
            break

    return char_pos


def solve_part_2(puzzle_input: str) -> int:
    """
    Solve part 2:
    How many characters need to be processed
    before the first start-of-message marker is detected?
    """

    data: str = parse_input(puzzle_input)
    char_pos: int = 0

    # find char_pos after first occurence of 14 unique chars occurs.
    for i in range(len(data)):
        if len(set(data[i : i + 14])) == 14:
            char_pos = i + 14
            break

    return char_pos


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
