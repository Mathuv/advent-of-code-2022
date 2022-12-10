import sys
from pathlib import Path
from typing import List, Dict


def parse_input(puzzle_input_file_path: Path) -> List[str]:
    """Parse input data."""

    return puzzle_input_file_path.read_text().strip().splitlines()


def calculate_sum_of_signal_strengths(program_instructions: List[str]) -> int:

    instr_cycle_map: Dict[str, int] = {
        "noop": 1,
        "addx": 2,
    }

    cycle_intervals: List[int] = list(
        range(20, 221, 40)
    )  # [20, 60, 100, 140, 180, 220]

    x = 1  # register value
    cycle_count = 0
    sum_signal_strengths: int = 0

    for instr in program_instructions:
        op = instr.split()[0]
        inst_cycles = instr_cycle_map[op]
        for i in range(inst_cycles):
            cycle_count += 1

            if cycle_count in cycle_intervals:
                sum_signal_strengths += cycle_count * x
            # i = 1 -> add the value only at the end of second cycle
            if op == "addx" and i == 1:
                val = int(instr.split()[1])
                x += val

    return sum_signal_strengths


def solve_part_1(puzzle_input_file_path: Path) -> int:
    """
    Solve part 1:
    Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.
    What is the sum of these six signal strengths?
    """

    program_instructions: List[str] = parse_input(puzzle_input_file_path)
    return calculate_sum_of_signal_strengths(program_instructions)


def solve_part_2(puzzle_input_file_path: Path) -> int:
    """
    Solve part 2:
    """

    program_instructions: List[str] = parse_input(puzzle_input_file_path)

    return 0


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
