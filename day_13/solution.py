import sys
from pathlib import Path
from typing import Any, List, Tuple


def parse_input(puzzle_input_file_path: Path) -> List[Tuple[List[Any], List[Any]]]:
    """
    Parse input data.

    Returns: Pairs of packets (list of tuples)
    """

    text: str = puzzle_input_file_path.read_text().strip()
    # replace '\n\n' with '|' and '\n' with ','
    text = text.replace("\n\n", "|").replace("\n", ",")
    pairs = text.split("|")
    return [eval(x) for x in pairs]


def find_packet_pairs_in_order(packet_pairs: List[Tuple[List[Any], List[Any]]]):
    """
    When comparing two values, the first value is called left and
    the second value is called right. Then:

    1.If both values are integers, the lower integer should come first.
      If the left integer is lower than the right integer, the inputs are in the right order.
      If the left integer is higher than the right integer, the inputs are not in the right order.
      Otherwise, the inputs are the same integer; continue checking the next part of the input.
    2.If both values are lists, compare the first value of each list, then the second value, and so on.
      If the left list runs out of items first, the inputs are in the right order.
      If the right list runs out of items first, the inputs are not in the right order.
      If the lists are the same length and no comparison makes a decision about the order,
      continue checking the next part of the input.
    3.If exactly one value is an integer, convert the integer to a list which contains that integer as its only value,
      then retry the comparison.
      For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2);
      the result is then found by instead comparing [0,0,0] and [2].


    Args:
        packet_pairs (List[Tuple[List[Any], List[Any]]]): _description_

    Returns:
        _type_: _description_
    """

    pairs_in_order = []  # indices of pairs in order

    for i, pair in enumerate(packet_pairs):
        left, right = pair
        print(f"index: {i+1}, left: {left}, right: {right}")
        if is_ordered(left, right) is True:
            index_in_packet_pairs = i + 1
            pairs_in_order.append(index_in_packet_pairs)
        print(f"pairs in order: {pairs_in_order}")
    return pairs_in_order


def is_ordered(left, right):
    # both values equal -> not in order
    if left == right:
        return None

    # 1. both values are integers
    if type(left) == int and type(right) == int:
        if left < right:
            return True
        return False

    # 3.If only either value is an integer, convert to list
    if type(left) == int:
        left = [left]

    if type(right) == int:
        right = [right]

    # 2. Both values are of type list
    if type(left) == list and type(right) == list:
        if left == right:
            return None
        else:
            if len(left) > 0 and len(right) > 0:
                # recursive
                for i, pair in enumerate(zip(left, right)):
                    print(f"(new) left: {pair[0]} , rgt: {pair[1]}")
                    remainder_left = left[i + 1 :]
                    remainder_right = right[i + 1 :]
                    ordered = is_ordered(pair[0], pair[1])
                    # Both sides are equal
                    if ordered is None:
                        # there are more items to compare -> continuw
                        if len(remainder_left) and len(remainder_right):
                            continue
                        # left side ran out of items
                        elif len(remainder_left) == 0:
                            return True
                        # right side ran out of items
                        elif len(remainder_right) == 0:
                            return False
                    return ordered
            elif len(left) == 0:
                return True
            elif len(right) == 0:
                return False


def solve_part_1(puzzle_input_file_path: Path) -> int:
    """
    Solve part 1:
    Determine which pairs of packets are already in the right order.
    What is the sum of the indices of those pairs?
    """

    packet_pairs: List[Tuple[List[Any], List[Any]]] = parse_input(
        puzzle_input_file_path
    )

    return sum(find_packet_pairs_in_order(packet_pairs))


def solve_part_2(puzzle_input_file_path: Path) -> int:
    """
    Solve part 2:
    """

    packet_pairs: List[Tuple[List[Any], List[Any]]] = parse_input(
        puzzle_input_file_path
    )

    return 0


def solve_puzzle(puzzle_input_file_path: Path):
    """
    Solve the Advent of Code puzzle of the day.
    Day 13: Distress Signal
    """

    solution_1 = solve_part_1(puzzle_input_file_path)
    solution_2 = solve_part_2(puzzle_input_file_path)

    return solution_1, solution_2


if __name__ == "__main__":
    # Read input data
    puzzle_input_file_path: Path = Path(sys.argv[1])

    # Solve the puzzle
    solution_1, solution_2 = solve_puzzle(puzzle_input_file_path)

    # Print the solutions
    print(f"Solution 1: {solution_1}")
    print(f"Solution 2: {solution_2}")
