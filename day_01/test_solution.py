import pathlib

import pytest
import solution as sol

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example_data():
    """Example data."""
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return sol.parse_input(puzzle_input)


def test_parse_example(example_data):
    """Test parsing example."""
    assert example_data == [
        ["1000", "2000", "3000"],
        ["4000"],
        ["5000", "6000"],
        ["7000", "8000", "9000"],
        ["10000"],
    ]


def test_part_1_example(example_data):
    """Test part 1 of the puzzle using the data example."""
    assert sol.solve_part_1(example_data) == 24000


def test_part_2_example(example_data):
    """Test part 2 of the puzzle using the data example."""
    assert sol.solve_part_2(example_data) == 45000
