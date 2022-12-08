import pathlib

import pytest
import solution as sol

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example_data():
    """Example data."""
    return (PUZZLE_DIR / "example.txt").read_text()


def test_parse_example(example_data):
    """Test parsing example."""
    parsed_date = sol.parse_input(example_data)
    assert parsed_date == [
        "$ cd /",
        "$ ls",
        "dir a",
        "14848514 b.txt",
        "8504156 c.dat",
        "dir d",
        "$ cd a",
        "$ ls",
        "dir e",
        "29116 f",
        "2557 g",
        "62596 h.lst",
        "$ cd e",
        "$ ls",
        "584 i",
        "$ cd ..",
        "$ cd ..",
        "$ cd d",
        "$ ls",
        "4060174 j",
        "8033020 d.log",
        "5626152 d.ext",
        "7214296 k",
    ]


# @pytest.mark.skip(reason="Not implemented yet")
def test_part_1_example(example_data):
    """Test part 1 of the puzzle using the data example."""
    assert sol.solve_part_1(example_data) == 95437


@pytest.mark.skip(reason="Not implemented yet")
def test_part_2_example(example_data):
    """Test part 2 of the puzzle using the data example."""
    assert sol.solve_part_2(example_data) == ...
