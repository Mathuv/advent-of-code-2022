import pathlib
import sys
from typing import Any, List, Dict
from io import StringIO

import pandas as pd


def parse_input(puzzle_input: str) -> List[Any]:
    """Parse input data."""

    # replace the following characters
    # "[" -> " "
    # "]" -> " "
    # "move" -> ""
    # "from" -> ""
    # "to" -> ""
    puzzle_input = (
        puzzle_input.replace("[", " ")
        .replace("]", " ")
        .replace("move", "")
        .replace("from", "")
        .replace("to", "")
    )

    # Split the text into two section by empty line
    data: List[str] = [i.strip() for i in puzzle_input.split("\n\n")]
    data: List[str] = puzzle_input.split("\n\n")

    return data


def solve_part_1(puzzle_input: str) -> int:
    """
    Solve part 1:
    After the rearrangement procedure completes, what crate ends up on top of each stack?
    """

    data: List[str] = parse_input(puzzle_input)
    # Pandas dataframe from string data
    stacks_data: StringIO = StringIO(data[0])
    procedures_data: StringIO = StringIO(data[1])

    stacks_df: pd.DataFrame = pd.read_fwf(stacks_data, colspecs="infer", header=None)
    # set last row as column names
    stacks_df = stacks_df.rename(columns=stacks_df.iloc[-1]).drop(stacks_df.index[-1])
    # reverse the order of the rows
    # stacks_df = stacks_df.iloc[::-1]
    stacks_df = stacks_df[::-1]
    # create dictionary of stacks
    stacks_dict: Dict[str, List[str]] = stacks_df.to_dict(orient="list")
    # remove pandas NaN values fom the dictionary values (lists)
    for k, v in stacks_dict.items():
        stacks_dict[k] = [i for i in v if not pd.isna(i)]

    procedures_df: pd.DataFrame = pd.read_fwf(
        procedures_data, colspecs="infer", header=None, names=["move", "from", "to"]
    )

    # Loop through the rows of the procedures dataframe
    for index in procedures_df.index:
        for i in range(procedures_df.loc[index, "move"]):
            # Pop the last element from the "from" stack to append to the "to" stack
            stacks_dict[str(procedures_df.loc[index, "to"])].append(
                stacks_dict[str(procedures_df.loc[index, "from"])].pop()
            )

    # get the top element of each stack
    message: str = ""
    for col in stacks_df.columns:
        message += stacks_dict[str(col)][-1]

    return message


def solve_part_2(puzzle_input: str) -> int:
    """
    Solve part 2:
    """

    data: List[str] = parse_input(puzzle_input)
    # Pandas dataframe from string data
    stacks_data: StringIO = StringIO(data[0])
    procedures_data: StringIO = StringIO(data[1])

    stacks_df: pd.DataFrame = pd.read_fwf(stacks_data, colspecs="infer", header=None)
    # set last row as column names
    stacks_df = stacks_df.rename(columns=stacks_df.iloc[-1]).drop(stacks_df.index[-1])
    # reverse the order of the rows
    # stacks_df = stacks_df.iloc[::-1]
    stacks_df = stacks_df[::-1]
    # create dictionary of stacks
    stacks_dict: Dict[str, List[str]] = stacks_df.to_dict(orient="list")
    # remove pandas NaN values fom the dictionary values (lists)
    for k, v in stacks_dict.items():
        stacks_dict[k] = [i for i in v if not pd.isna(i)]

    procedures_df: pd.DataFrame = pd.read_fwf(
        procedures_data, colspecs="infer", header=None, names=["move", "from", "to"]
    )

    # Loop through the rows of the procedures dataframe
    for index in procedures_df.index:
        # for i in range(procedures_df.loc[index, "move"]):
        # Pop the last element from the "from" stack to append to the "to" stack
        no_of_items: int = procedures_df.loc[index, "move"]
        stack_from: str = str(procedures_df.loc[index, "from"])
        stack_to: str = str(procedures_df.loc[index, "to"])
        stacks_dict[stack_to].extend(stacks_dict[stack_from][-no_of_items:])
        # remove the items from the "from" stack
        stacks_dict[stack_from] = stacks_dict[stack_from][:-no_of_items]

    # get the top element of each stack
    message: str = ""
    for col in stacks_df.columns:
        message += stacks_dict[str(col)][-1]

    return message


def solve_puzzle(puzzle_input):
    """Solve the Advent of Code puzzle of the day."""

    solution_1 = solve_part_1(puzzle_input)
    solution_2 = solve_part_2(puzzle_input)

    return solution_1, solution_2


if __name__ == "__main__":
    # Read input data
    # puzzle_input = pathlib.Path(sys.argv[1]).read_text().strip()
    puzzle_input = pathlib.Path(sys.argv[1]).read_text()

    # Solve the puzzle
    solution_1, solution_2 = solve_puzzle(puzzle_input)

    # Print the solutions
    print(f"Solution 1: {solution_1}")
    print(f"Solution 2: {solution_2}")
