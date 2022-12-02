from typing import List, Dict, Tuple
import pathlib
import sys

SHAPE_SCORE_MAP: Dict[str, int] = {
    "A": 1,  # Rock
    "B": 2,  # Paper
    "C": 3,  # Scissors
    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3,  # Scissors
}

OUTCOME_SCORE_MAP: Dict[Tuple[str, str], int] = {
    ("A", "X"): 3,  # draw
    ("A", "Y"): 6,  # won
    ("A", "Z"): 0,  # lost
    ("B", "X"): 0,  # lost
    ("B", "Y"): 3,  # draw
    ("B", "Z"): 6,  # won
    ("C", "X"): 6,  # won
    ("C", "Y"): 0,  # lost
    ("C", "Z"): 3,  # draw
}


def parse_input(puzzle_input: str) -> List[Tuple[str, str]]:
    """Parse input data."""

    # Split the input into lines
    lines: List[str] = puzzle_input.splitlines()
    # Split each line into tuples
    data: List[Tuple[str, str]] = [tuple(line.split(" ")) for line in lines]

    return data


def solve_part_1(puzzle_input: str) -> int:
    """
    Solve part 1:
    What would your total score be
    if everything goes exactly according to your strategy guide?
    """
    data: List[Tuple[str, str]] = parse_input(puzzle_input)
    total_score: int = 0
    for round in data:
        total_score += OUTCOME_SCORE_MAP[round] + SHAPE_SCORE_MAP[round[1]]

    return total_score


def solve_part_2(puzzle_input: str) -> int:
    """
    Solve part 2:
    """

    return 0


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
