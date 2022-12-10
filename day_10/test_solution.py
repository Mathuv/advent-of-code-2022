import pathlib

import pytest
import solution as sol

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example_data_1() -> pathlib.Path:
    """Example data 1."""
    return PUZZLE_DIR / "example1.txt"


@pytest.fixture
def example_data_2() -> pathlib.Path:
    """Example data 2."""
    return PUZZLE_DIR / "example2.txt"


def test_parse_example(example_data_2):
    """Test parsing example2.txt."""
    parsed_data = sol.parse_input(example_data_2)
    assert parsed_data == [
        "noop",
        "addx 3",
        "addx -5",
    ]


def test_part_1_example(example_data_1):
    """Test part 1 of the puzzle using the data example."""
    assert sol.solve_part_1(example_data_1) == 13140


@pytest.mark.skip("Not implemented yet")
def test_part_2_example(example_data_1):
    """Test part 2 of the puzzle using the data example."""
    assert sol.solve_part_2(example_data_1) == ...
