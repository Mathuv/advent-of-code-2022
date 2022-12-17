import pathlib

import pytest
import solution as sol
from icecream import ic

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example_data() -> pathlib.Path:
    """Example data."""
    return PUZZLE_DIR / "example.txt"


def test_parse_example(example_data):
    """Test parsing example."""
    parsed_data = sol.parse_input(example_data)
    ic(parsed_data)
    assert parsed_data == [
        [(18, 2), (15, -2)],
        [(16, 9), (16, 10)],
        [(2, 13), (3, 15)],
        [(14, 12), (16, 10)],
        [(20, 10), (16, 10)],
        [(17, 14), (16, 10)],
        [(7, 8), (10, 2)],
        [(0, 2), (10, 2)],
        [(11, 0), (10, 2)],
        [(14, 20), (17, 25)],
        [(20, 17), (22, 21)],
        [(7, 16), (3, 15)],
        [(3, 14), (3, 15)],
        [(1, 20), (3, 15)],
    ]


def test_part_1_example(example_data):
    """Test part 1 of the puzzle using the data example."""
    assert sol.solve_part_1(example_data) == 26


@pytest.mark.skip("Not implemented yet")
def test_part_2_example(example_data):
    """Test part 2 of the puzzle using the data example."""
    assert sol.solve_part_2(example_data) == ...
