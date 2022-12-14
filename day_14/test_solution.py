import pathlib

import pytest
import solution as sol

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example_data() -> pathlib.Path:
    """Example data."""
    return PUZZLE_DIR / "example.txt"


def test_parse_example(example_data):
    """Test parsing example."""
    parsed_data = sol.parse_input(example_data)
    assert parsed_data == [
        [(4, 498), (6, 498), (6, 496)],
        [(4, 503), (4, 502), (9, 502), (9, 494)],
    ]


def test_part_1_example(example_data):
    """Test part 1 of the puzzle using the data example."""
    assert sol.solve_part_1(example_data) == 24


def test_part_2_example(example_data):
    """Test part 2 of the puzzle using the data example."""
    assert sol.solve_part_2(example_data) == 93
