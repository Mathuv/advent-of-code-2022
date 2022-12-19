import sys
from pathlib import Path
from typing import List, Tuple

import numpy as np
from icecream import ic
from scipy.spatial.distance import cdist, cityblock


def parse_input(puzzle_input_file_path: Path) -> List[List[Tuple[int, int]]]:
    """Parse input data."""

    text: str = puzzle_input_file_path.read_text().strip()
    # Remove unwanted strings form text
    text: str = (
        text.replace("Sensor at x=", "")
        .replace("y=", "")
        .replace(" closest beacon is at x=", "")
    )
    positions = [
        [(eval(pos)[1], eval(pos)[0]) for pos in line.split(":")]
        for line in text.splitlines()
    ]

    return positions


def draw_sensors_and_beacons(grid: np.ndarray, positions: List[List[Tuple[int, int]]]):
    """
    Draw sensors and beacons on the grid
    """
    for position in positions:
        # Draw the sensor
        grid[position[0][0], position[0][1]] = "S"
        # Draw the beacon
        grid[position[1][0], position[1][1]] = "B"

    ic(grid.shape)
    ic("\n", grid)

    return grid


def draw_positons_without_beacons(
    grid: np.ndarray, positions: List[List[Tuple[int, int]]]
):
    """
    Draw positions without beacons on the grid with '#' by calculating manhattan distance between a sensor and closest beacon
    All the positons within the manhattan distance of a senson wouldn't have another beacon.
    """
    for position in positions:
        # Manhattan distance
        sensor = position[0]
        beacon = position[1]
        distance = cityblock(sensor, beacon)
        # create a meshgrid of grid
        idx_grid = np.meshgrid(np.arange(grid.shape[1]), np.arange(grid.shape[0]))
        # ic(idx_grid)
        sensor_pt = np.array(sensor).reshape(-1, 1, 1)
        ic(sensor_pt)
        # create a matrix of manhattan(cityblock)
        # distance of points in the grid from sensor
        # md_matrix = np.abs(idx_grid - np.array([sensor])).sum()
        md_matrix = np.abs(idx_grid - sensor_pt).sum(axis=0)
        ic(md_matrix.shape)
        ic(sensor_pt.shape)
        md_diamond = np.where(md_matrix <= distance)
        cords_B = np.where(grid == "B")
        cords_S = np.where(grid == "S")
        # grid[
        #     np.logical_and(md_diamond, np.where(grid == "B"), np.where(grid == "S"))
        # ] = "#"
        grid[md_diamond] = "#"
        grid[cords_B] = "B"
        grid[cords_S] = "S"

        ic("\n", grid)

    # ic(grid.shape)
    # ic("\n", grid)

    return grid


def create_grid(positions: List[List[Tuple[int, int]]]) -> np.ndarray:
    """
    Create just enough size of the numpy array to accomodate cordinates in the positions
    """

    # find min_row, max_row and min_col and max_col from scans for numpy array
    min_row = 0
    max_row = max(max(c[0] for c in position) for position in positions)
    min_col = min(min(c[1] for c in position) for position in positions)
    max_col = max(max(c[1] for c in position) for position in positions)

    rows = (max_row - min_row) + 1
    cols = (max_col - min_col) + 1

    # Draw the grid of air
    grid: np.ndarray = np.full((rows, cols), ".")
    ic(grid.shape)
    ic("\n", grid)

    # Draw sensors and beacons
    grid = draw_sensors_and_beacons(grid, positions)

    # Draw positions without additional beacons
    grid = draw_positons_without_beacons(grid, positions)

    # # Draw the sensors and beacons again
    # grid = draw_sensors_and_beacons(grid, positions)

    return grid


def find_positions_cannot_contain_beacons(
    positions: List[List[Tuple[int, int]]], row: int
) -> int:
    """
    Find the positions that cannot contain a beacon.
    """

    grid: np.ndarray = create_grid(positions)

    return np.count_nonzero(grid[row, :] == "#")


def solve_part_1(puzzle_input_file_path: Path, row: int = 2000000) -> int:
    """
    Solve part 1:
    Consult the report from the sensors you just deployed.
    In the row where y=2000000, how many positions cannot contain a beacon?
    """

    positions: List[List[Tuple[int, int]]] = parse_input(puzzle_input_file_path)

    return find_positions_cannot_contain_beacons(positions, row)


def solve_part_2(puzzle_input_file_path: Path) -> int:
    """
    Solve part 2:
    """

    data: List[str] = parse_input(puzzle_input_file_path)

    return 0


def solve_puzzle(puzzle_input_file_path: Path):
    """
    Solve the Advent of Code puzzle of the day.
    --- Day 15: Beacon Exclusion Zone ---
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
