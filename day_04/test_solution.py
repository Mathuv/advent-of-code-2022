import pathlib

import pytest
import solution as sol

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example_data():
    """Example data."""
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()

    return puzzle_input


def test_parse_example(example_data):
    """
    Test parsing example.
    [
        ["2-4", "6-8"],
        ["2-3", "4-5"],
        ["5-7", "7-9"],
        ["2-8", "3-7"],
        ["6-6", "4-6"],
        ["2-6", "4-8"],
    ] =>
    [
        [[2, 3, 4], [6, 7, 8]],
        [[2, 3], [4, 5]],
        [[5, 6, 7], [7, 8, 9]],
        [[2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7]],
        [[6], [4, 5, 6]],
        [[2, 3, 4, 5, 6], [4, 5, 6, 7, 8]],
    ]
    """
    parsed_date = sol.parse_input(example_data)
    assert parsed_date == [
        [[2, 3, 4], [6, 7, 8]],
        [[2, 3], [4, 5]],
        [[5, 6, 7], [7, 8, 9]],
        [[2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7]],
        [[6], [4, 5, 6]],
        [[2, 3, 4, 5, 6], [4, 5, 6, 7, 8]],
    ]


def test_part_1_example(example_data):
    """Test part 1 of the puzzle using the data example."""
    assert sol.solve_part_1(example_data) == 2


def test_part_2_example(example_data):
    """Test part 2 of the puzzle using the data example."""
    assert sol.solve_part_2(example_data) == 4
