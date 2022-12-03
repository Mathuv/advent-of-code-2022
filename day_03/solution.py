import string
import pathlib
import sys
from typing import List

# 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ASCII_LETTERS: str = string.ascii_letters


def parse_input(puzzle_input: str) -> List[str]:
    """Parse input data."""

    # Split the input into lines
    lines: List[str] = puzzle_input.splitlines()

    # Further process the lines
    data: List[str] = lines

    return data


def solve_part_1(puzzle_input: str) -> int:
    """
    Solve part 1:
    Find the item type that appears in both compartments of each rucksack.
    What is the sum of the priorities of those item types?
    """

    data: List[str] = parse_input(puzzle_input)
    total_score: int = 0
    # Calculate the total score
    for line in data:
        # find common letters between both halves of the line
        common_letters = "".join(
            set(line[: len(line) // 2]) & set(line[len(line) // 2 :])
        )
        # add the score for the common letters
        total_score += sum([ASCII_LETTERS.index(i) + 1 for i in common_letters])

    return total_score


def solve_part_2(puzzle_input: str) -> int:
    """
    Solve part 2:
    """

    data: List[str] = parse_input(puzzle_input)
    total_score: int = 0
    # Calculate the total score
    for i in range(len(data) // 3):
        # chunk the data into 3 lines at a time
        chunk = data[i * 3 : i * 3 + 3]
        # find the common letters between the 3 in a group
        common_letters = "".join(set.intersection(*[set(i) for i in chunk]))
        # add the score for the common letters
        total_score += sum([ASCII_LETTERS.index(i) + 1 for i in common_letters])

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
