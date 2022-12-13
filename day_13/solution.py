import sys
from pathlib import Path
from typing import Any, List, Tuple


def parse_input(puzzle_input_file_path: Path) -> List[Tuple[List[Any], List[Any]]]:
    """
    Parse input data.

    Returns: Pairs of packets (list of tuples)
    """

    text: str = puzzle_input_file_path.read_text().strip()
    # replace '\n\n' with '|' and '\n' with ','
    text = text.replace("\n\n", "|").replace("\n", ",")
    pairs = text.split("|")
    return [eval(x) for x in pairs]


def solve_part_1(puzzle_input_file_path: Path) -> int:
    """
    Solve part 1:
    Determine which pairs of packets are already in the right order.
    What is the sum of the indices of those pairs?
    """

    packet_pairs: List[Tuple[List[Any], List[Any]]] = parse_input(puzzle_input_file_path)

    return 0


def solve_part_2(puzzle_input_file_path: Path) -> int:
    """
    Solve part 2:
    """

    packet_pairs: List[Tuple[List[Any], List[Any]]] = parse_input(puzzle_input_file_path)

    return 0


def solve_puzzle(puzzle_input_file_path: Path):
    """
    Solve the Advent of Code puzzle of the day.
    Day 13: Distress Signal
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
