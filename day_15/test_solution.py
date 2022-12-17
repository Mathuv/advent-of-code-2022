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
        [(2, 18), (-2, 15)],
        [(9, 16), (10, 16)],
        [(13, 2), (15, 3)],
        [(12, 14), (10, 16)],
        [(10, 20), (10, 16)],
        [(14, 17), (10, 16)],
        [(8, 7), (2, 10)],
        [(2, 0), (2, 10)],
        [(0, 11), (2, 10)],
        [(20, 14), (25, 17)],
        [(17, 20), (21, 22)],
        [(16, 7), (15, 3)],
        [(14, 3), (15, 3)],
        [(20, 1), (15, 3)],
    ]


@pytest.mark.skip("Not implemented yet")
def test_part_1_example(example_data):
    """Test part 1 of the puzzle using the data example."""
    assert sol.solve_part_1(example_data) == 26


@pytest.mark.skip("Not implemented yet")
def test_part_2_example(example_data):
    """Test part 2 of the puzzle using the data example."""
    assert sol.solve_part_2(example_data) == ...
