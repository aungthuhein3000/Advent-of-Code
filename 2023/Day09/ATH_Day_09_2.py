# https://adventofcode.com/2023/day/9#part2

def main():
    file = open(r'input.txt')
    line = file.readline()

    total: int = 0
    while line != '':
        try:
            numbers: list[int] = [int(x) for x in line.strip().split(' ')]
            total += extrapolate_backward(numbers)
        except ValueError as ve:
            print(ve)

        line = file.readline()

    print(f'Total: {total}')

def extrapolate_backward(seq: list[int]) -> int:
    diffs: list[list[int]] = [[]]
    diffs[0] = seq.copy()

    length: int = len(seq)
    if length < 2:
        raise ValueError('Error: not enough numbers provided')

    if length == 2: # if it's just an array of 2 numbers
        return diffs[0][0] - (diffs[0][1] - diffs[0][0])

    # generate all diffs
    level: int = 1
    while True:
        diff_len: int = length - level # length of each set of diffs depending on `level`

        if diff_len < 1: # if there's no discernable pattern
            raise ValueError('Error: invalid sequence')

        diffs.append([]) # append an empty array for the next row of diffs
        for i in range(diff_len):
            diffs[level].append(diffs[level - 1][i + 1] - diffs[level - 1][i])

        if sum(diffs[level]) == 0:
            break

        level += 1
    
    historic_value: int = 0
    for i in range(level - 1, -1, -1):
        historic_value = diffs[i][0] - historic_value

    return historic_value

if __name__ == '__main__':
    main()
