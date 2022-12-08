import sys
from pathlib import Path
from typing import Tuple

import numpy as np


def parse_input(puzzle_input_file_path: Path) -> np.ndarray:
    """Parse input data."""

    matrix: np.ndarray = np.empty(0, dtype=str)
    with puzzle_input_file_path.open() as f:
        # read line by line
        for line in f:
            # numpy array for the line
            array_line: np.ndarray = np.array([list(line.strip())])
            # concatinae each line's numpy array into matrix.
            matrix = (
                np.concatenate((matrix, array_line), axis=0)
                if matrix.size > 0
                else array_line
            )

    return matrix.astype(int)


def solve_part_1(puzzle_input_file_path: Path) -> int:
    """
    Solve part 1:
    """

    matrix: np.ndarray = parse_input(puzzle_input_file_path)
    trees_on_the_edge, trees_visible_inside_edge = find_trees_visible(matrix)

    return trees_on_the_edge + trees_visible_inside_edge


def find_trees_visible(matrix: np.ndarray) -> Tuple[int, int]:

    nrows: int = matrix.shape[0]
    ncols: int = matrix.shape[1]

    trees_on_the_edge = 2 * (nrows - 1) + 2 * (ncols - 1)

    trees_visible_inside_edge = 0
    # loop through trees inside the edge
    for x in range(1, nrows - 1):
        for y in range(1, ncols - 1):
            tree_height = matrix[x, y]
            # get the threes in the top, down, left, right directions
            top: np.ndarray = matrix[0:x, y]
            bottom: np.ndarray = matrix[x + 1 : nrows, y]
            left: np.ndarray = matrix[x, 0:y]
            right: np.ndarray = matrix[x, y + 1 : ncols]

            # check if it's visible in any direction
            # - all the trees in one direction are shorter than the current tree
            for direction in [top, bottom, left, right]:
                if all(i < tree_height for i in direction):
                    trees_visible_inside_edge += 1
                    break

    return trees_on_the_edge, trees_visible_inside_edge


def solve_part_2(puzzle_input_file_path: Path) -> int:
    """
    Solve part 2:
    Consider each tree on your map. What is the highest scenic score possible for any tree?
    """

    matrix: np.ndarray = parse_input(puzzle_input_file_path)
    highest_sceninc_score: int = calc_highest_scenic_score(matrix)

    return highest_sceninc_score


def calc_highest_scenic_score(matrix: np.ndarray) -> int:

    nrows: int = matrix.shape[0]
    ncols: int = matrix.shape[1]

    highest_scenic_score: int = 0

    # loop through trees inside the edge
    for x in range(1, nrows - 1):
        for y in range(1, ncols - 1):
            tree_height = matrix[x, y]
            # get the threes in the top, down, left, right directions
            top: np.ndarray = np.flip(matrix[0:x, y])
            bottom: np.ndarray = matrix[x + 1 : nrows, y]
            left: np.ndarray = np.flip(matrix[x, 0:y])
            right: np.ndarray = matrix[x, y + 1 : ncols]

            # check if it's visible in any direction
            # - all the trees in one direction are shorter than the current tree
            scenic_score = 1
            for direction in [top, bottom, left, right]:
                viewing_distance = 0
                for i in direction:
                    viewing_distance += 1
                    if i >= tree_height:
                        break
                scenic_score = scenic_score * viewing_distance

            highest_scenic_score = (
                scenic_score
                if scenic_score > highest_scenic_score
                else highest_scenic_score
            )

    return highest_scenic_score


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
