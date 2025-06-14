from itertools import combinations
from io import StringIO # dabble in some in-memory streams
from typing import NamedTuple


class Index(NamedTuple): # for readibility
    row: int
    col: int


def read_file(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return file.read().splitlines()


def insert_columns(img: list[str], indexes: list[int]) -> None:
    ss: StringIO = StringIO()
    for r in range(len(img)):
        line: str = img[r]
        prev_index: int = 0
        for index in indexes:
            ss.write(line[prev_index:index])
            prev_index = index
            ss.write('.')
        ss.write(line[prev_index:])

        img[r] = ss.getvalue()
        ss.seek(0)
        ss.truncate()
    ss.close()


def expand_image(img: list[str]) -> list[str]:
    empty_cols: list[int] = []
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
            empty_cols.append(c)

    # insert columns
    if len(empty_cols) > 0:
        insert_columns(img, empty_cols)
        width = len(img[0])

    # insert rows
    empty_line: str = '.' * width
    for r in range(height - 1, -1, -1):
        if img[r] == empty_line:
            img.insert(r, empty_line)


def main() -> None:
    image: list[str] = read_file('input.txt')
    expand_image(image)

    WIDTH: int = len(image[0])
    HEIGHT: int = len(image)
    galaxy_coords: list[Index] = []

    for r in range(HEIGHT):
        for c in range(WIDTH):
            if image[r][c] == '#':
                galaxy_coords.append(Index(r, c))

    pairs: combinations[str] = combinations(galaxy_coords, 2)
    total_distances: int = 0
    for pair in pairs: # tuple of two Index objects
        total_distances += abs(pair[0].row - pair[1].row) + abs(pair[0].col - pair[1].col)

    print(f"Total distances: {total_distances}")


if __name__ == '__main__':
    main()

