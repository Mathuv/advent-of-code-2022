import pathlib

import pytest
import solution as sol

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example_data():
    """Example data."""
    return (PUZZLE_DIR / "example.txt").read_text().strip()


@pytest.mark.skip(reason="Not implemented yet")
def test_parse_example(example_data):
    """Test parsing example."""
    parsed_date = sol.parse_input(example_data)
    assert parsed_date == ...


@pytest.mark.skip(reason="Not implemented yet")
def test_part_1_example(example_data):
    """Test part 1 of the puzzle using the data example."""
    assert sol.solve_part_1(example_data) == 95437


@pytest.mark.skip(reason="Not implemented yet")
def test_part_2_example(example_data):
    """Test part 2 of the puzzle using the data example."""
    assert sol.solve_part_2(example_data) == ...
