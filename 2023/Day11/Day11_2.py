from itertools import combinations
from io import StringIO # dabble in some in-memory streams
from typing import NamedTuple


class Index(NamedTuple): # for readability
    row: int
    col: int


def read_file(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return file.read().splitlines()


def find_empty_spaces(img: list[str], rows: list[int], cols: list[int]) -> None:
    width: int = len(img[0])
    height: int = len(img)

    # find empty columns
    for c in range(width): # go by column
        empty: bool = True
        for r in range(height):
            if img[r][c] == '#':
                empty = False
                break
        if empty:
            cols.append(c)

    # find empty rows
    empty_line: str = '.' * width
    for r in range(height):
        if img[r] == empty_line:
            rows.append(r)


# Number of empty spaces (rows/columns) between two coordinates (row, column)
def get_empty_distance(indexes: list[int], p1: int, p2: int, scale: int) -> int: # p1, p2 can be row number or col number
    if p1 > p2:
        p1, p2 = p2, p1

    """
    🐞 Initializing `start` to 0 is a bug.
    Specifically when there's no empty space between points and both points are "higher" than any empty space lines.
    Use `test()` below to debug.
    Also, slicing with invalid indices returns `[]`.
    """
    start: int = len(indexes)
    end: int = len(indexes)

    for i, index in enumerate(indexes):
        if index >= p1:
            start = i
            break

    for i, index in enumerate(indexes[start:], start = start):
        if index > p2:
            end = i
            break

    # compensate for empty spaces already counted
    return (len(indexes[start:end]) * scale) - len(indexes[start:end])


def main() -> None:
    image: list[str] = read_file('input.txt')
    SCALE: int = 1_000_000
    empty_rows: list[int] = []
    empty_cols: list[int] = []
    find_empty_spaces(image, empty_rows, empty_cols)

    WIDTH: int = len(image[0])
    HEIGHT: int = len(image)
    galaxy_coords: list[Index] = []

    for r in range(HEIGHT):
        for c in range(WIDTH):
            if image[r][c] == '#':
                galaxy_coords.append(Index(r, c))

    # check this type annotation
    pairs: combinations[Index] = combinations(galaxy_coords, 2)
    total_distances: int = 0
    for p1, p2 in pairs: # tuple of two Index objects
        total_distances += abs(p1.row - p2.row) + abs(p1.col - p2.col) # This counts empty spaces as 1. To be accounted for in function below.
        total_distances += get_empty_distance(empty_rows, p1.row, p2.row, SCALE) # empty rows
        total_distances += get_empty_distance(empty_cols, p1.col, p2.col, SCALE) # empty columns

    print(f"Total distances: {total_distances}") # 791134099634


def test() -> None:
    indexes: list[int] = [5, 9, 11]
    SCALE: int = 10

    while True:
        print(f"Scale: {SCALE}, Indexes: {indexes}")
        user_input: list[str] = input("Enter 2 numbers: ").split()

        if not user_input:
            print("Quitting...")
            break

        if len(user_input) != 2:
            print("Please enter two valid numbers.\n")
            continue

        try:
            p1: int = int(user_input[0])
            p2: int = int(user_input[1])
        except ValueError as ve:
            print(f"Error: {ve}\n")
            continue

        print(f"Distance: {get_empty_distance(indexes, p1, p2, SCALE)}\n")


if __name__ == '__main__':
    main()
    # test()

