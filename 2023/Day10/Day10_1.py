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


def set_visited(visited: list[list[bool]], index: Index) -> None:
    visited[index.row][index.col] = True


def unset_visited(visited: list[list[bool]], index: Index) -> None:
    visited[index.row][index.col] = False


"""
Assumes:
    - There's a loop containing the starting point
    - Starting point is set to False in the `visited` matrix
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
        case 'S':
            if map[current.row - 1][current.col] in "|7F":
                return Index(current.row - 1, current.col)
            if map[current.row][current.col + 1] in "-J7":
                return Index(current.row, current.col + 1)
            if map[current.row + 1][current.col] in "|LJ":
                return Index(current.row + 1, current.col)
            if map[current.row][current.col - 1] in "-LF":
                return Index(current.row, current.col - 1)
            raise ValueError('Could not move forward from starting point!')
        case other:
            raise ValueError(f'Unknown pipe value found in map: {other}')


# assumes there's a closed loop
def main() -> None:
    pipe_map: list[str] = read_file('input.txt')
    START: Index = find_start_point(pipe_map)
    WIDTH: int = len(pipe_map[0])
    HEIGHT: int = len(pipe_map)
    visited: list[list[bool]] = [[False for _ in range(WIDTH)] for _ in range(HEIGHT)]

    set_visited(visited, START)
    loop_len: int = 1

    # take 1st step
    current: Index = next_pipe(pipe_map, visited, START)
    set_visited(visited, current)
    loop_len += 1

    # take 2nd step
    current = next_pipe(pipe_map, visited, current)
    set_visited(visited, current)
    loop_len += 1
    unset_visited(visited, START) # unset starting point

    # finish the loop
    while (current := next_pipe(pipe_map, visited, current)) != START:
        loop_len += 1
        set_visited(visited, current)

    print(f"Number of steps: {loop_len / 2}") # Answer: 6733


if __name__ == '__main__':
    main()

