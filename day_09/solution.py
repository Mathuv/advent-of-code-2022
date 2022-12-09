import sys
import math
from copy import deepcopy
from pathlib import Path
from typing import Tuple, List

import numpy as np


def parse_input(puzzle_input_file_path: Path) -> List[str]:
    """Parse input data."""

    return puzzle_input_file_path.read_text().strip().splitlines()


def create_grid(motions: List[str]) -> np.ndarray:
    """
    Crate just enough size of the grid to accomodate the movement of H & T

    Returns:
     [[' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' '],
      [' ', 'S', ' ', ' '],
      [' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ']]
    """

    grid = np.full((1, 1), "H")  # grid = [["H"]]
    for i, item in enumerate(motions):
        direction, distance = tuple(item.split(" "))  # 'U 4'
        distance = int(distance)

        # current cordinates
        r, c = np.where(grid == "H")
        r = r[0]
        c = c[0]

        # Mark the starting positon
        grid[r, c] = "S" if i == 0 else "-"

        grid_h, grid_w = grid.shape

        # expand the grid in the direction by the distance
        if direction == "D":
            # move down and if required expand the grip down
            if distance > (grid_h - 1) - r:
                # expand (np.concatinate)
                n_rows_to_add = distance - ((grid_h - 1) - r)
                expansion = np.full((n_rows_to_add, grid_w), "-")
                grid = np.concatenate((grid, expansion))
            # move 'H down
            grid[r + distance, c] = "H"
        elif direction == "U":
            # move up and if required expand the grid up
            if distance > r:
                # expand (np.concatinate)
                n_rows_to_add = distance - r
                expansion = np.full((n_rows_to_add, grid_w), "-")
                grid = np.concatenate((grid, expansion))
                # np.roll to expand at the top
                grid = np.roll(grid, n_rows_to_add, axis=0)
                # update the current cordinates of "H"
                r = r + n_rows_to_add

            # move 'H' up
            grid[r - distance, c] = "H"

        elif direction == "R":
            # move left and if required expand the grid left
            if distance > (grid_w - 1) - c:
                # expand (np.concatinate)
                n_cols_to_add = distance - ((grid_w - 1) - c)
                expansion = np.full((grid_h, n_cols_to_add), "-")
                grid = np.concatenate((grid, expansion), axis=1)
            # move 'H' left
            grid[r, c + distance] = "H"
        elif direction == "L":
            # move right and if required expand the grid right
            if distance > c:
                # expand (np.concatinate)
                n_cols_to_add = distance - c
                expansion = np.full((grid_h, n_cols_to_add), "-")
                grid = np.concatenate((grid, expansion), axis=1)
                # np.roll to expand on the right
                grid = np.roll(grid, n_cols_to_add)
                # update the current cordinates of "H"
                c = c + n_cols_to_add

            # move 'H' right
            grid[r, c - distance] = "H"

            # print(item)
            # print(grid)

    # Replace 'H' with ' '
    grid[grid == "H"] = " "

    return grid


def move_H(grid_H, direction, distance):

    # direction, distance = tuple(motion.split(" "))  # 'U 4'
    # distance = int(distance)

    # current cordinates
    r, c = np.where(grid_H == "H")
    r = r[0]
    c = c[0]

    # expand the grid in the direction by the distance
    if direction == "D":
        # move 'H down
        grid_H[r + distance, c] = "H"
    elif direction == "U":
        # move 'H' up
        grid_H[r - distance, c] = "H"

    elif direction == "R":
        # move 'H' left
        grid_H[r, c + distance] = "H"
    elif direction == "L":
        # move 'H' right
        grid_H[r, c - distance] = "H"

    # Clear the starting positon of H
    grid_H[r, c] = "-"

    return grid_H, r, c


def move_T(grid_T, grid_H, grid_trail_T, r, c):

    # current cordinates of H
    rh, ch = np.where(grid_H == "H")
    rh = rh[0]
    ch = ch[0]

    # current cordinates of T
    rt, ct = np.where(grid_T == "T")
    rt = rt[0]
    ct = ct[0]

    # mark the current position T on trail
    grid_trail_T[rt, ct] = "#"

    # Calculate Euclidean distance
    distance_T_H = math.dist((rh, ch), (rt, ct))
    if distance_T_H >= 2:
        # Move T adjacent to H
        grid_T[r, c] = "T"
        # mark the new positon of T on trail
        grid_trail_T[r, c] = "#"
        grid_T[rt, ct] = "-"

    return grid_T, grid_trail_T


def solve_part_1(puzzle_input_file_path: Path) -> int:
    """
    Solve part 1:
    Simulate your complete hypothetical series of motions.
    How many positions does the tail of the rope visit at least once?
    """

    motions: List[str] = parse_input(puzzle_input_file_path)
    grid_H = create_grid(motions)
    grid_T = deepcopy(grid_H)
    grid_trail_T = deepcopy(grid_H)
    grid_H[grid_H == "S"] = "H"
    grid_T[grid_T == "S"] = "T"
    # print(f"Grid H:\n{grid_H}")
    # print(f"Grid T:\n{grid_T}")
    # print(f"Grid Trail T:\n{grid_trail_T}")

    for motion in motions:
        direction, distance = tuple(motion.split(" "))  # 'U 4'
        distance = int(distance)
        # print(motion)
        for i in range(distance):
            grid_H, r, c = move_H(grid_H, direction, 1)
            # print(grid_H)
            grid_T, grid_trail_T = move_T(grid_T, grid_H, grid_trail_T, r, c)
            # print(grid_T)
            # print(grid_trail_T)

    grid_trail_T[grid_trail_T == "S"] = "#"
    return np.count_nonzero(grid_trail_T == "#")


def solve_part_2(puzzle_input_file_path: Path) -> int:
    """
    Solve part 2:
    """

    motions: List[str] = parse_input(puzzle_input_file_path)

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
