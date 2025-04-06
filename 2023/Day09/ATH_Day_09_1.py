# https://adventofcode.com/2023/day/9

def main():
    file = open(r'input.txt')
    line = file.readline()

    total: int = 0
    while line != '':
        try:
            numbers: list[int] = [int(x) for x in line.strip().split(' ')]
            total += predict_value(numbers)
        except ValueError as ve:
            print(ve)

        line = file.readline()

    print(f'Total: {total}')

def predict_value(seq: list[int]) -> int:
    diffs: list[list[int]] = [[]]
    diffs[0] = seq.copy()

    length: int = len(seq)
    if length < 2:
        raise ValueError('Error: not enough numbers provided')

    if length == 2: # if it's just an array of 2 numbers
        return diffs[0][1] + diffs[0][1] - diffs[0][0]

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

    # add an extra 0 at the end of the last "level"
    diffs[level].append(0)

    for i in range(level - 1, -1, -1):
        diffs[i].append(diffs[i + 1][length - i - 1] + diffs[i][length - i - 1])

    return diffs[0][-1]


    #####################
    # pop() method
    # print(f'\ndiffs: {diffs}')

    # sum_diffs: int = 0
    # for i in range(level - 1, -1, -1):
    #     sum_diffs = sum_diffs + diffs[i].pop()

    # print(sum_diffs)
    # return sum_diffs
    #####################


# def test():
#     a = [[1, 5, 9], [-1, -2, -3, -4], [1, 2], [9, -8, 92, 1], [-2, -1, 0, 1, 2]]
#     for nums in a:
#         print(f'Input: {nums}')
#         print(f'Output: {predict_value(nums)}')

if __name__ == '__main__':
    main()

    # try:
    #     test()
    # except ValueError as ve:
    #     print(ve)
    # except Exception as e:
    #     print(e)
    #     print('blah')
