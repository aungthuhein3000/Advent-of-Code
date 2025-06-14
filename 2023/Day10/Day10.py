"""
Contains a ray casting solution copied from the internet. Not sure why it works.
Apart from lines indicated as copied in `part2()`, I wrote *every single line*.
"""

from typing import NamedTuple


class Index(NamedTuple): # for readibility
    row: int
    col: int


def read_file(filename: str) -> list[str]:
    pipe_map: list[str] = []
    with open(filename, 'r') as file:
        for line in file:
            pipe_map.append(line.strip())
    return pipe_map


def find_start_point(map: list[str]) -> Index:
    for row, line_str in enumerate(map):
        col: int = line_str.find('S')
        if col != -1:
            return Index(row, col)
    raise ValueError('No starting point found in the pipe map!')


"""
Assumes:
    - There's a loop containing the starting point
    - Starting point is set to False in the `visited` matrix
    - Starting point 'S' has been replaced with appropriate pipe symbol
"""
def next_pipe(map: list[str], visited: list[list[bool]], current: Index) -> Index:
    match map[current.row][current.col]:
        case '|':
            if visited[current.row - 1][current.col]:
                return Index(current.row + 1, current.col)
            else:
                return Index(current.row - 1, current.col)
        case '-':
            if visited[current.row][current.col + 1]:
                return Index(current.row, current.col - 1)
            else:
                return Index(current.row, current.col + 1)
        case 'L':
            if visited[current.row - 1][current.col]:
                return Index(current.row, current.col + 1)
            else:
                return Index(current.row - 1, current.col)
        case 'J':
            if visited[current.row - 1][current.col]:
                return Index(current.row, current.col - 1)
            else:
                return Index(current.row - 1, current.col)
        case '7':
            if visited[current.row][current.col - 1]:
                return Index(current.row + 1, current.col)
            else:
                return Index(current.row, current.col - 1)
        case 'F':
            if visited[current.row][current.col + 1]:
                return Index(current.row + 1, current.col)
            else:
                return Index(current.row, current.col + 1)
        case other:
            raise ValueError(f'Unknown pipe value found in map: {other}')


# assumes there's only 2 pipes connecting to start point
def replace_start_point(map: list[str], index: Index) -> None:
    pipe_symbol: dict[tuple[str, str], str] = { # to find symbol to replace 'S' with
        ("up", "down"): "|",
        ("left", "right"): "-",
        ("up", "right"): "L",
        ("up", "left"): "J",
        ("down", "left"): "7",
        ("down", "right"): "F"
    }

    connections: list[str] = []
    # order of checks matters
    if map[index.row - 1][index.col] in "|7F":
        connections.append("up")
    if map[index.row + 1][index.col] in "|LJ":
        connections.append("down")
    if map[index.row][index.col - 1] in "-LF":
        connections.append("left")
    if map[index.row][index.col + 1] in "-J7":
        connections.append("right")

    if len(connections) != 2:
        raise ValueError('Starting point is not connected to exactly two pipes.')

    map[index.row] = map[index.row].replace('S', pipe_symbol[tuple(connections)])


def is_connected(map: list[str], i: Index, direction: str) -> bool:
    match direction:
        case "left": # connects to the left?
            return map[i.row][i.col - 1] in "-LF" and map[i.row][i.col] in "-J7"
        case "up": # connects up?
            return map[i.row - 1][i.col] in "|7F" and map[i.row][i.col] in "|LJ"
        case _:
            raise ValueError('Wrong direction provided')


# Count number of "paths" (not pipes) to the left, right, up and down.
# This logic is wrong apparently. This function is useless for now.
def path_counts(map: list[str], i: Index) -> tuple[int, int, int, int]:
    WIDTH: int = len(map[0])
    HEIGHT: int = len(map)
    left: int = 0
    right: int = 0
    up: int = 0
    down: int = 0
    PIPES: str = "|-LJ7F" # all pipe symbols

    # left
    pointer: int = 0 # for indexing horizontally and vertically
    while pointer < i.col:
        if map[i.row][pointer] in PIPES:
            if pointer == 0: # bounds check
                left += 1
            else: # not on the border
                if not is_connected(map, Index(i.row, pointer), "left"):
                    left += 1
        pointer += 1

    # right
    pointer = i.col + 1 # for indexing horizontally and vertically
    while pointer < WIDTH:
        if map[i.row][pointer] in PIPES:
            if pointer == i.col + 1: # first path found?
                right += 1
            else: # not on the border
                if not is_connected(map, Index(i.row, pointer), "left"):
                    right += 1
        pointer += 1

    # up
    pointer = 0 # for indexing horizontally and vertically
    while pointer < i.row:
        if map[pointer][i.col] in PIPES:
            if pointer == 0: # bounds check
                up += 1
            else: # not on the border
                if not is_connected(map, Index(pointer, i.col), "up"):
                    up += 1
        pointer += 1

    # down
    pointer = i.row + 1 # for indexing horizontally and vertically
    while pointer < HEIGHT:
        if map[pointer][i.col] in PIPES:
            if pointer == i.row + 1: # first path found?
                down += 1
            else: # not on the border
                if not is_connected(map, Index(pointer, i.col), "up"):
                    down += 1
        pointer += 1

    return left, right, up, down


def part1(pipe_map: list[str], visited: list[list[bool]]) -> int:
    START: Index = find_start_point(pipe_map)
    replace_start_point(pipe_map, START) # replace 'S' with appropriate pipe

    visited[START.row][START.col] = True # set start point as visited temporarily
    loop_len: int = 1

    current: Index = Index(START.row, START.col)

    # take 1st step
    current: Index = next_pipe(pipe_map, visited, START)
    visited[current.row][current.col] = True
    loop_len += 1

    # take 2nd step
    current = next_pipe(pipe_map, visited, current)
    visited[current.row][current.col] = True
    loop_len += 1
    visited[START.row][START.col] = False # unset start point

    # finish the loop
    while (current := next_pipe(pipe_map, visited, current)) != START:
        loop_len += 1
        visited[current.row][current.col] = True


    visited[START.row][START.col] = True

    return loop_len


def part2(pipe_map: list[str], visited: list[list[bool]], region: list[list[bool]], width: int, height: int) -> int:
    inside_count: int = 0 # number of spaces inside the loop

    for r in range(height):
        for c in range(width):
            if not visited[r][c]:
                ### LINES COPIED FROM INTERNET ###
                count: int = 0
                for c2, symbol in enumerate(pipe_map[r][:c]): # look on one side only. WHY DOES THIS WORK?!
                    if visited[r][c2] and symbol in "L|J": # why only "L|J"?! Why not also "F7"?
                        count += 1

                if count % 2 == 1:
                    region[r][c] = True
                    inside_count += 1
                ### LINES COPIED FROM INTERNET ###

    return inside_count

# assumes there's a closed loop
def main() -> None:
    pipe_map: list[str] = read_file('input.txt')

    WIDTH: int = len(pipe_map[0])
    HEIGHT: int = len(pipe_map)
    visited: list[list[bool]] = [[False for _ in range(WIDTH)] for _ in range(HEIGHT)] # for the main loop

    # Part 1
    loop_len: int = part1(pipe_map, visited)
    print(f"Part 1 => Steps to farthest point: {loop_len / 2}") # Answer: 6733

    # Part 2
    region: list[list[bool]] = [[False for _ in range(WIDTH)] for _ in range(HEIGHT)] # region inside loop
    inside_count: int = part2(pipe_map, visited, region, WIDTH, HEIGHT)

    print(f"Part 2 => Tiles inside loop: {inside_count}") # Answer: 435
#    print("Inside regions:")
#    for row in region:
#        for pipe in row:
#            print(int(pipe), end = "")
#        print()


if __name__ == '__main__':
    main()

