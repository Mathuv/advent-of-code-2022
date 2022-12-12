import sys
import networkx as nx
from pathlib import Path
from typing import List, Tuple
import numpy as np


def parse_input(puzzle_input_file_path: Path) -> np.ndarray:
    """Parse input data."""

    text: str = puzzle_input_file_path.read_text().strip()

    # Convert the text into numpy array and return
    return np.array([list(line) for line in text.splitlines()])


def create_directed_graph(grid: np.ndarray) -> nx.DiGraph:
    G: nx.DiGraph = nx.DiGraph()

    # Add all the nodes(vertices) to the graph
    for index, x in np.ndenumerate(grid):
        G.add_node(index, value=x)

    # Add edges to the graph based on the 'ord' value of node value(alpha characters)
    # Distance betwee adjacent nodes can only be one
    # And traversal can happen only in left, right, up, down directions in the grid
    for index, x in np.ndenumerate(grid):
        # left
        if index[1] > 0:
            cordinates_left = (index[0], index[1] - 1)
            value_left = grid[cordinates_left]
            if (ord(value_left) - ord(x)) <= 1:
                G.add_edge(index, cordinates_left, weight=1)

        # right
        if index[1] < grid.shape[1] - 1:
            cordinates_right = (index[0], index[1] + 1)
            value_right = grid[cordinates_right]
            if (ord(value_right) - ord(x)) <= 1:
                G.add_edge(index, cordinates_right, weight=1)

        # up
        if index[0] > 0:
            cordinates_up = (index[0] - 1, index[1])
            value_up = grid[cordinates_up]
            if (ord(value_up) - ord(x)) <= 1:
                G.add_edge(index, cordinates_up, weight=1)

        # down
        if index[0] < grid.shape[0] - 1:
            cordinates_down = (index[0] + 1, index[1])
            value_down = grid[cordinates_down]
            if (ord(value_down) - ord(x)) <= 1:
                G.add_edge(index, cordinates_down, weight=1)

    return G


def find_shortest_path(grid: np.ndarray) -> int:
    r, c = np.where(grid == "S")
    source_node: Tuple[int, int] = (r[0], c[0])
    grid[grid == "S"] = "a"

    r, c = np.where(grid == "E")
    target_node: Tuple[int, int] = r[0], c[0]
    grid[grid == "E"] = "z"

    print(f"source_node: {source_node}")
    print(f"destination_node: {target_node}")

    G = create_directed_graph(grid)

    return nx.shortest_path_length(G, source_node, target_node)


def solve_part_1(puzzle_input_file_path: Path) -> int:
    """
    Solve part 1:
    What is the fewest steps required to move from your
    current position to the location that should get the best signal?
    """

    grid: np.ndarray = parse_input(puzzle_input_file_path)

    return find_shortest_path(grid)


def solve_part_2(puzzle_input_file_path: Path) -> int:
    """
    Solve part 2:
    """

    grid: np.ndarray = parse_input(puzzle_input_file_path)

    return 0


def solve_puzzle(puzzle_input_file_path: Path):
    """
    Solve the Advent of Code puzzle of the day.
    Day 12: Hill Climbing Algorithm
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
