def find_numbers(line: str) -> list[tuple[int, int, int]]:
    LENGTH: int = len(line)
    numbers_list: list[tuple[int, int, int]] = [] # list of [start index, end index, actual number]

    i: int = 0 # top-level iterator
    while i < LENGTH:
        num: int = 0
        j: int = i # to look for digits
        while j < LENGTH and line[j].isdigit():
            num = (num * 10) + int(line[j])
            j += 1

        if num > 0:
            numbers_list.append((i, j, num))
            i = j # continue after the number
        i += 1

    return numbers_list

def main():
    file = open(r'input.txt')

    lines: list[str] = []
    for _ in range(2):
        lines.append('.' + file.readline().strip() + '.')
    LINE_LENGTH: int = len(lines[0]) # including the border dots
    BLANK_LINE: str = '.' * LINE_LENGTH # immutable
    lines.insert(0, BLANK_LINE) # necessary to prevent out of bounds when doing the masking thing

    BLANK_LINE_FOR_SPECIAL: list[bool] = [False for _ in range(LINE_LENGTH)] # mutable
    specials: list[list[bool]] = [BLANK_LINE_FOR_SPECIAL.copy() for _ in range(3)] # start with 3 blank lines

    sum: int = 0
    while True:
        # find special characters in current line and new line
        for row in range(1, 3):
            for i in range(1, LINE_LENGTH - 1):
                if lines[row][i] != '.' and not lines[row][i].isdigit():
                    specials[1][i - 1] = specials[1][i] = specials[1][i + 1] = True # current line: [1]
                    specials[2][i - 1] = specials[2][i] = specials[2][i + 1] = True # next line: [2]
        
        # add adjacent numbers
        numbers: list[tuple[int, int, int]] = find_numbers(lines[1])
        for number in numbers:
            for i in range(number[0], number[1]):
                if specials[1][i]:
                    sum += number[2]
                    break # break out of the inner for loop

        # read next line
        lines.pop(0)
        lines.insert(2, '.' + file.readline().strip() + '.')
        if lines[2] == '..': # just to prevent index out of range when you reach the last line of the file
            lines[2] = BLANK_LINE

        # exit condition
        if lines[1] == BLANK_LINE:
            break

        # prepare for masking new line
        specials.pop(0)
        specials.insert(2, BLANK_LINE_FOR_SPECIAL.copy())
    
    file.close()
    
    print(f'Sum: {sum:,}')
    return 0


if __name__ == '__main__':
    main()
