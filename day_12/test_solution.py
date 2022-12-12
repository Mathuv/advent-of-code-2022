import pathlib

import numpy as np
import pytest
import solution as sol

# from pprint import pprint


PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example_data() -> pathlib.Path:
    """Example data."""
    return PUZZLE_DIR / "example.txt"


def test_parse_example(example_data):
    """Test parsing example."""
    grid: np.ndarray = np.array(
        [
            ["S", "a", "b", "q", "p", "o", "n", "m"],
            ["a", "b", "c", "r", "y", "x", "x", "l"],
            ["a", "c", "c", "s", "z", "E", "x", "k"],
            ["a", "c", "c", "t", "u", "v", "w", "j"],
            ["a", "b", "d", "e", "f", "g", "h", "i"],
        ]
    )
    parsed_data = sol.parse_input(example_data)
    # pprint(parsed_data)
    assert np.array_equal(parsed_data, grid)


def test_part_1_example(example_data):
    """Test part 1 of the puzzle using the data example."""
    assert sol.solve_part_1(example_data) == 31


@pytest.mark.skip("Not implemented yet")
def test_part_2_example(example_data):
    """Test part 2 of the puzzle using the data example."""
    assert sol.solve_part_2(example_data) == ...
