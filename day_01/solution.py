from typing import List
import pathlib
import sys


def parse_input(puzzle_input: str) -> List[List[str]]:
    """Parse input data."""

    data: List[List[str]] = []
    # Split the text into list of paragraphs
    paragraphs: List[str] = puzzle_input.split("\n\n")
    # Split each paragraph into list of lines
    for paragraph in paragraphs:
        data.append(paragraph.splitlines())

    return data


def solve_part_1(data: List[List[str]]) -> int:
    """
    Solve part 1:
    Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
    """
    total_calories_of_each_elf: List[int] = []
    total_calories_of_each_elf = list(map(lambda x: sum(int(i) for i in x), data))

    return max(total_calories_of_each_elf)


def solve_part_2(data: List[List[str]]) -> int:
    """Solve part 2."""

    return 0


def solve_puzzle(puzzle_input):
    """Solve the Advent of Code puzzle of the day."""

    data = parse_input(puzzle_input)
    solution_1 = solve_part_1(data)
    solution_2 = solve_part_2(data)

    return solution_1, solution_2


if __name__ == "__main__":
    # Read input data
    puzzle_input = pathlib.Path(sys.argv[1]).read_text().strip()

    # Solve the puzzle
    solution_1, solution_2 = solve_puzzle(puzzle_input)

    # Print the solutions
    print(f"Solution 1: {solution_1}")
    print(f"Solution 2: {solution_2}")
