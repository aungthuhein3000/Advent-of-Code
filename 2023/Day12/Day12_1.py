# Brute force solution. A little slow.
# Write a better one later.

from itertools import combinations
from collections.abc import Generator
import re
from io import StringIO


def count_arrangements(file_line: str) -> int:
    row, groups_str = file_line.split()
    groups: list[int] = [int(n) for n in groups_str.split(',')]

    question_mark_positions: list[int] = []
    hashes: int = row.count('#')
    for i, ch in enumerate(row):
        if ch == '?':
            question_mark_positions.append(i)

    remaining: int = sum(groups) - hashes # remaining number of hashes to fill in
    combs: combinations[int] = combinations(question_mark_positions, remaining)

    # Example regex pattern: #{1}[\.\?]+#{2}[\.\?#{3}
    regex: StringIO = StringIO()
    for group in groups:
        regex.write(fr"#{{{group}}}[\.\?]+")
    regex.truncate(regex.tell() - 7) # remove the last r"[\.\?]+"

    arrangement: StringIO = StringIO() # for possible arrangements
    possible_arrangements: int = 0
    for combination in combs:
        arrangement.write(row)

        for index in combination:
            arrangement.seek(index)
            arrangement.write('#')

        if re.search(regex.getvalue(), arrangement.getvalue()):
            possible_arrangements += 1

        arrangement.seek(0)
        arrangement.truncate()

    regex.close()
    arrangement.close()

    return possible_arrangements


def read_file(filename: str) -> Generator[str]:
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()


def main() -> None:
    filename: str = 'input.txt'
    lines: Generator[str] = read_file(filename)

    total: int = 0
    for line in lines:
        total += count_arrangements(line)

    print(f"Total arrangements: {total}") # 6958


if __name__ == '__main__':
    main()

