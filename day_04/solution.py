from typing import List
import pathlib
import sys


def parse_input(puzzle_input: str) -> List[List[str]]:
    """Parse input data."""

    # Split the input into lines
    lines = puzzle_input.splitlines()

    # TODO: improve this code block
    # Further process the lines
    for i, line in enumerate(lines):
        # convert pair range to list of ints
        pair = line.split(",")
        pair[0] = list(
            range(int(pair[0].split("-")[0]), int(pair[0].split("-")[1]) + 1)
        )  # '1-5' -> [1,2,3,4,5]
        pair[1] = list(
            range(int(pair[1].split("-")[0]), int(pair[1].split("-")[1]) + 1)
        )
        # pair[0] = list(range(int(pair[0][0]), int(pair[0][2]) + 1))  # '1-3' -> range(int('1'), int('3') + 1) -> [1, 2, 3]
        # pair[1] = list(range(int(pair[1][0]), int(pair[1][2]) + 1))
        lines[i] = pair

    data: List[List[str]] = lines

    return data


def solve_part_1(puzzle_input: str) -> int:
    """
    Solve part 1:
    In how many assignment pairs does one range fully contain the other?.
    """

    data: List[List[str]] = parse_input(puzzle_input)
    total_score: int = 0
    # Calculate the total score
    for pair in data:
        # check if pairs are subsets of each other
        if set(pair[0]).issubset(set(pair[1])) or set(pair[1]).issubset(set(pair[0])):
            total_score += 1

    return total_score


def solve_part_2(puzzle_input: str) -> int:
    """
    Solve part 2:
    In how many assignment pairs do the ranges overlap?.
    """

    data: List[List[str]] = parse_input(puzzle_input)
    total_score: int = 0
    # Calculate the total score
    for pair in data:
        # check if pairs intersect
        if set(pair[0]).intersection(set(pair[1])):
            total_score += 1

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
