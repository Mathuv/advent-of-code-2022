import pathlib

import pytest
import solution as sol

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example_data():
    """Example data."""
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text()

    return puzzle_input


def test_parse_example(example_data):
    """Test parsing example."""
    parsed_date = sol.parse_input(example_data)
    assert parsed_date == [
        "     D     \n N   C     \n Z   M   P \n 1   2   3 ",
        " 1  2  1\n 3  1  3\n 2  2  1\n 1  1  2",
    ]


def test_part_1_example(example_data):
    """Test part 1 of the puzzle using the data example."""
    assert sol.solve_part_1(example_data) == "CMZ"


@pytest.mark.skip(reason="Not implemented yet")
def test_part_2_example(example_data):
    """Test part 2 of the puzzle using the data example."""
    assert sol.solve_part_2(example_data) == ...
