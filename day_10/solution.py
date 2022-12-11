import sys
from pathlib import Path
from typing import Dict, List

import numpy as np
import pandas as pd


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


def draw_CRT(grid: np.ndarray, sprite_pixels: List[int]) -> np.ndarray:
    """
    Draws CRT pixel based on the value of the
    register X and the position of the Sprite.
    """

    # cordinates of the current pixel to be drawn
    row, col = np.where(grid == "C")
    row = row[0]
    col = col[0]


    grid[row, col] = "#" if col in sprite_pixels else "."
    df = pd.DataFrame(grid)
    print(df)

    # Mark the next pixel as current pixel
    # Move to the row below if it has reched the right most pixel
    # and not in the last row
    if col + 1 == grid.shape[1] and row + 1 < grid.shape[0]:
        row = row + 1
    # otherwise remain in the same row
    else:
        row = row

    # Move to column 0 if it has reched the right most pixel
    # otherwise to the next column (col + 1) in right.
    col = 0 if col + 1 == grid.shape[1] else col + 1
    # print(f"r,c after: {row},{col}")
    grid[row, col] = "C"

    return grid


def render_image(program_instructions: List[str]) -> np.ndarray:

    crt_grid = np.full((6, 40), ".")
    crt_grid[
        0, 0
    ] = "C"  # Mark the current pixel position. 0,0 is the starting position

    instr_cycle_map: Dict[str, int] = {
        "noop": 1,
        "addx": 2,
    }

    x = 1  # register value
    cycle_count = 0
    # sum_signal_strengths: int = 0

    for instr in program_instructions:
        op = instr.split()[0]
        inst_cycles = instr_cycle_map[op]
        for i in range(inst_cycles):
            # -> Cycle start
            sprite_pixels: List[int] = [x - 1, x, x + 1]
            cycle_count += 1

            # Draw CRT
            crt_grid = draw_CRT(crt_grid, sprite_pixels)

            # -> Cycle end
            if op == "addx" and i == 1:
                val = int(instr.split()[1])
                x += val

    # At the end: replace "C" with "#" on CRT
    crt_grid[crt_grid == "C"] = "#"

    return crt_grid


def solve_part_1(puzzle_input_file_path: Path) -> int:
    """
    Solve part 1:
    Find the signal strength during the 20th, 60th, 100th, 140th, 180th,
    and 220th cycles.
    What is the sum of these six signal strengths?
    """

    program_instructions: List[str] = parse_input(puzzle_input_file_path)
    return calculate_sum_of_signal_strengths(program_instructions)


def solve_part_2(puzzle_input_file_path: Path) -> np.ndarray:
    """
    Solve part 2:
    Render the image given by your program.
    What eight capital letters appear on your CRT?
    """

    program_instructions: List[str] = parse_input(puzzle_input_file_path)
    return render_image(program_instructions)


def solve_puzzle(puzzle_input_file_path: Path):
    """Solve the Advent of Code puzzle of the day."""

    solution_1: int = solve_part_1(puzzle_input_file_path)
    solution_2: np.ndarray = solve_part_2(puzzle_input_file_path)

    return solution_1, solution_2


if __name__ == "__main__":
    # Read input data
    puzzle_input_file_path: Path = Path(sys.argv[1])

    # Solve the puzzle
    solution_1, solution_2 = solve_puzzle(puzzle_input_file_path)

    # Print the solutions
    print(f"Solution 1: {solution_1}")
    # Convert the numpy array to pandas data_frame for better printing.
    print(f"Solution 2: \n{pd.DataFrame(solution_2)}")
