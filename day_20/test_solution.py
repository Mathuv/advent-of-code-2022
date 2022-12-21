import time
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
    start_time = time.time()
    parsed_data = sol.parse_input(example_data)
    elapsed_time = (time.time() - start_time) * 1000
    ic(elapsed_time)
    assert parsed_data == [1, 2, -3, 3, -2, 0, 4]


def test_part_1_example(example_data):
    """Test part 1 of the puzzle using the data example."""
    start_time = time.time()
    result = sol.solve_part_1(example_data)
    elapsed_time = (time.time() - start_time) * 1000
    ic(elapsed_time)
    assert result == 3


@pytest.mark.skip("Not implemented yet")
def test_part_2_example(example_data):
    """Test part 2 of the puzzle using the data example."""
    assert sol.solve_part_2(example_data) == ...
