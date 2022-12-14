import sys
import math
from pathlib import Path
from typing import Any, Dict, List

import yaml


def parse_input(puzzle_input_file_path: Path) -> Dict[str, Any]:
    """Parse input data."""

    text: str = puzzle_input_file_path.read_text().strip().lower()

    # replace 4 spaces with 2 spaces to may in YAML compliant
    text = text.replace("    ", "  ")
    # replace "divisible by " and "throw to monkey " with "" to make it easy to process
    text = (
        text.replace("divisible by ", "")
        .replace("throw to monkey ", "")
        .replace("old", "worry")
        .replace("new = ", "")
        .replace("monkey ", "")
        .replace("if ", "")
    )
    document = yaml.safe_load(text)
    for value in document.values():
        # Convert comma separated string values of 'starting items'
        # into python list of integers.
        # Eg: "1,2,3,4" -> [1,2,3,4]
        value["starting items"] = [
            int(x) for x in str(value["starting items"]).split(",")
        ]

    return document


def calc_level_of_monkey_business(
    document: Dict[str, Any], rounds: int = 20, divide_worry_level: bool = True
) -> int:
    # Initialize 'inspected=0' for all monkeys
    for value in document.values():
        value["inspected"] = 0

    for i in range(rounds):
        for monkey, v in document.items():
            starting_items: List[int] = v["starting items"]
            while len(starting_items):
                worry = starting_items.pop(0)  # not a good practice
                v["inspected"] += 1
                operation: str = v["operation"]
                worry = eval(operation)
                if divide_worry_level:
                    worry = worry // 3
                if worry % v["test"] == 0:  # Divisible
                    target_monkey = v[True]
                else:
                    target_monkey = v[False]
                target_starting_items: List[int] = document[target_monkey][
                    "starting items"
                ]
                target_starting_items.append(worry)

    inspected_items_list = [v["inspected"] for v in document.values()]
    inspected_items_list.sort(reverse=True)

    return math.prod(inspected_items_list[:2])


def solve_part_1(puzzle_input_file_path: Path) -> int:
    """
    Solve part 1:
    Figure out which monkeys to chase by counting how many
    items they inspect over 20 rounds. What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?
    """

    document: Dict[str, Any] = parse_input(puzzle_input_file_path)
    return calc_level_of_monkey_business(document)


def solve_part_2(puzzle_input_file_path: Path) -> int:
    """
    Solve part 2:
    """

    document: Dict[str, Any] = parse_input(puzzle_input_file_path)

    return calc_level_of_monkey_business(
        document=document, rounds=10000, divide_worry_level=False
    )


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
