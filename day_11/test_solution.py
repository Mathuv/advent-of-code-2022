import pathlib
from pprint import pprint

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
    pprint(parsed_data)
    assert parsed_data == {
        0: {
            False: 3,
            True: 2,
            "operation": "worry * 19",
            "starting items": [79, 98],
            "test": 23,
        },
        1: {
            False: 0,
            True: 2,
            "operation": "worry + 6",
            "starting items": [54, 65, 75, 74],
            "test": 19,
        },
        2: {
            False: 3,
            True: 1,
            "operation": "worry * worry",
            "starting items": [79, 60, 97],
            "test": 13,
        },
        3: {
            False: 1,
            True: 0,
            "operation": "worry + 3",
            "starting items": [74],
            "test": 17,
        },
    }


# @pytest.mark.skip("Not implemented yet")
def test_part_1_example(example_data):
    """Test part 1 of the puzzle using the data example."""
    assert sol.solve_part_1(example_data) == 10605


@pytest.mark.skip("Not implemented yet")
def test_part_2_example(example_data):
    """Test part 2 of the puzzle using the data example."""
    assert sol.solve_part_2(example_data) == ...
