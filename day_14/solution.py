import sys
from pathlib import Path
from pprint import pprint
from typing import List, Tuple

import numpy as np
from icecream import ic

# np.set_printoptions(threshold=sys.maxsize)

ROCK: str = "#"
AIR: str = "."
SAND_SOURCE: str = "+"
SAND_AT_REST: str = "o"


def parse_input(puzzle_input_file_path: Path) -> List[List[Tuple[int, int]]]:
    """Parse input data."""

    text: str = puzzle_input_file_path.read_text().strip()

    # Split/convert text into list of lists of tuples of integers.
    scans: List[List[Tuple[int, int]]] = [
        # [eval(c) for c in line.split(" -> ")] for line in text.splitlines()
        # Swap the cordinated to represet in a numpy array rows and columns.
        [(eval(c)[1], eval(c)[0]) for c in line.split(" -> ")]
        for line in text.splitlines()
    ]

    return scans

# TODO: refactor the function
def create_grid(
    scans: List[List[Tuple[int, int]]], floor_at_bottom: bool = False
) -> np.ndarray:
    """
    Crate just enough size of the numpy array to accomodate cordinates in the scans
    """

    # FIXME: possibly grid size can be dynamically adjusted using np.roll
    # instead of trying to determine the size based on the input.
    # in that way it could lead to  more redable code

    # find min_row, max_row and min_col and max_col from scans for numpy array
    min_row = 0
    max_row = max(max(c[0] for c in scan) for scan in scans)
    min_col = min(min(c[1] for c in scan) for scan in scans)
    max_col = max(max(c[1] for c in scan) for scan in scans)

    if floor_at_bottom:
        max_row += 2  # Infinite floor is 2 tiles down the lowest rock path
        max_floor_length: int = 2 * (max_row + 2) - 1  # n'th odd number = 2n - 1
        min_col = (
            min_col
            if (500 - min_col) >= max_floor_length // 2
            else (500 - max_floor_length // 2)
        )
        max_col = (
            max_col
            if (max_col - 500) >= max_floor_length // 2
            else (500 + max_floor_length // 2)
        )

    rows = (max_row - min_row) + 1
    cols = (max_col - min_col) + 1


    # Draw the grid of air
    grid: np.ndarray = np.full((rows, cols), AIR)
    ic(grid.shape)
    # ic('\n', grid)
    pprint(grid)

    # Draw rock lines
    row_idx = np.array([], dtype=int)
    col_idx = np.array([], dtype=int)
    prev_point_r = 0
    prev_point_c = 0

    # Add floor at the bottom(rock line) to scans
    if floor_at_bottom:
        scans.append([(rows - 1, min_col), (rows - 1, max_col)])
        # scans.append([(grid.shape[0] - 1, 0), (grid.shape[0] - 1, grid.shape[1] - 1)])

    for rock_line in scans:
        for i, point in enumerate(rock_line):
            ic(point)
            ic(min_row)
            ic(min_col)
            current_point_r = point[0] - min_row
            current_point_c = point[1] - min_col

            # add the points in between the current point and the previous point
            if i > 0:
                if current_point_r == prev_point_r:
                    # Add horizontal points in between
                    for c in range(
                        min(prev_point_c, current_point_c) + 1,
                        max(prev_point_c, current_point_c),
                    ):
                        row_idx = np.append(row_idx, current_point_r)
                        col_idx = np.append(col_idx, c)

                elif current_point_c == prev_point_c:
                    # Add vertical point in between
                    for r in range(
                        min(prev_point_r, current_point_r) + 1,
                        max(prev_point_r, current_point_r),
                    ):
                        row_idx = np.append(row_idx, r)
                        col_idx = np.append(col_idx, current_point_c)

            # Add current point to the indexes
            row_idx = np.append(row_idx, current_point_r)
            col_idx = np.append(col_idx, current_point_c)

            prev_point_r = current_point_r
            prev_point_c = current_point_c

        ic(rock_line)
        ic(row_idx)
        ic(col_idx)

    grid[row_idx, col_idx] = ROCK  # #

    # Draw the source of sand
    grid[0, 500 - min_col] = SAND_SOURCE  # +
    ic(grid)

    return grid


def simulate_sand_fall(grid) -> bool:
    """Simulate sand falling among the rocks"""

    if SAND_SOURCE not in grid:
        ic("Souce is occupied")
        return False

    # Find the source of sand
    sand_source_pos = np.where(grid == SAND_SOURCE)
    sand_pos = sand_source_pos

    # let the sand fall down vertically
    while True:
        # if the point below is AIR, move the sand down
        if grid[sand_pos[0] + 1, sand_pos[1]] == AIR:
            sand_pos = (sand_pos[0] + 1, sand_pos[1])
        # else rest or move it sideways
        else:
            if sand_pos[1] in [0, grid.shape[1] - 1]:
                # if the sand has reached the edges of the
                # grid they fall off into the void
                ic("Free fall started")
                return False
            elif grid[sand_pos[0] + 1, sand_pos[1] - 1] == AIR:
                # else if space available move down left
                sand_pos = (sand_pos[0] + 1, sand_pos[1] - 1)
            elif grid[sand_pos[0] + 1, sand_pos[1] + 1] == AIR:
                #  else if space available move down right
                sand_pos = (sand_pos[0] + 1, sand_pos[1] + 1)
            else:
                # else stay on top
                # It has come to rest
                grid[sand_pos] = SAND_AT_REST
                return True


def find_no_of_sands(
    scans: List[List[Tuple[int, int]]], floor_at_the_bottom: bool = False
) -> int:

    # Initialize the grid
    grid: np.ndarray = create_grid(scans, floor_at_the_bottom)

    no_of_sands = 0

    while True:
        at_rest: bool = simulate_sand_fall(grid)
        # break when first sand freefalls into the void
        # or sand source is occcupied by a resting sand
        if not at_rest:
            break
        no_of_sands += 1

    return no_of_sands


def solve_part_1(puzzle_input_file_path: Path) -> int:
    """
    Solve part 1:
    Using your scan, simulate the falling sand.
    How many units of sand come to rest before sand starts flowing into the abyss below?
    """

    scans: List[List[Tuple[int, int]]] = parse_input(puzzle_input_file_path)

    return find_no_of_sands(scans)


def solve_part_2(puzzle_input_file_path: Path) -> int:
    """
    Solve part 2:
    """

    scans: List[List[Tuple[int, int]]] = parse_input(puzzle_input_file_path)

    return find_no_of_sands(scans=scans, floor_at_the_bottom=True)


def solve_puzzle(puzzle_input_file_path: Path):
    """
    Solve the Advent of Code puzzle of the day.
    Day 14: Regolith Reservoir
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
