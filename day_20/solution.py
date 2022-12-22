import sys
from pathlib import Path
from typing import List, Tuple
from collections import deque


def parse_input(puzzle_input_file_path: Path) -> List[int]:
    """Parse input data."""

    text = puzzle_input_file_path.read_text().strip()

    return [int(line) for line in text.splitlines()]


def get_sum_of_three_numbers(
    coordinates: List[int], decryption_key=1, no_of_mix=1
) -> int:

    # Create a list of tuples (indexed coordinates)
    i_cordinates: List[Tuple[int, int]] = list(enumerate(coordinates))
    i_cordinates = list(map(lambda x: (x[0], x[1] * decryption_key), i_cordinates))

    # create a deque
    i_cordinates_deque: deque = deque(i_cordinates)

    for i in range(no_of_mix):
        # loop through the coordinates and move the numbers around
        for coord in i_cordinates:
            fr_index = i_cordinates_deque.index(coord)
            # remove the item
            i_cordinates_deque.remove(coord)
            # calculate to index
            to_index = (fr_index + coord[1]) % (len(i_cordinates) - 1)
            # insert at to_index
            i_cordinates_deque.insert(to_index, coord)

    idx_zero = i_cordinates_deque.index((coordinates.index(0), 0))

    return (
        i_cordinates_deque[(idx_zero + 1000) % len(i_cordinates)][1]
        + i_cordinates_deque[(idx_zero + 2000) % len(i_cordinates)][1]
        + i_cordinates_deque[(idx_zero + 3000) % len(i_cordinates)][1]
    )


def solve_part_1(puzzle_input_file_path: Path) -> int:
    """
    Solve part 1:
    Mix your encrypted file exactly once. **What is the sum of
    the three numbers that form the grove coordinates?**
    """

    coordinates: List[int] = parse_input(puzzle_input_file_path)

    return get_sum_of_three_numbers(coordinates)


def solve_part_2(puzzle_input_file_path: Path) -> int:
    """
    Solve part 2:
    Apply the decryption key and mix your encrypted file ten times. What is the sum of the three numbers that form the grove coordinates?
    """

    coordinates: List[int] = parse_input(puzzle_input_file_path)

    return get_sum_of_three_numbers(coordinates, 811589153, 10)


def solve_puzzle(puzzle_input_file_path: Path):
    """
    Solve the Advent of Code puzzle of the day.
    --- Day 20: Grove Positioning System ---
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
