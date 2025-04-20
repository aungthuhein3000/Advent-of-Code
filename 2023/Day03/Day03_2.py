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
            numbers_list.append((i, j - 1, num))
            i = j # continue after the number
        i += 1

    return numbers_list

def main():
    with open(r'input.txt') as file:
        lines: list[str] = [] # keep track of three lines at a time
        for _ in range(2): # read the first two lines
            lines.append('.' + file.readline().strip() + '.')
        LINE_LENGTH: int = len(lines[0]) # including the border dots
        BLANK_LINE: str = '.' * LINE_LENGTH # immutable
        lines.insert(0, BLANK_LINE) # necessary to prevent out of bounds when doing the masking thing

        # store numbers found in the three lines by line number
        numbers: dict[int, list[tuple[int, int, int]]] = {} # {line number: [(start index, end index, number), (s, e, n), ... ]}

        current_line_number: int = 1
        sum: int = 0
        while True:
            for i in range(1, LINE_LENGTH - 1): # process a line
                if lines[1][i] == '*': # find stars
                    for line in range(3): # Find numbers in the three lines around the star. Necessary to loop through all 3 lines.
                        if current_line_number + line - 1 not in numbers.keys(): # To avoid looking for numbers if there is more than one star in a single line. Avoid significant duplicate work.
                            numbers[current_line_number + line - 1] = find_numbers(lines[line])
                
                    if numbers:
                        part_numbers: int = 0
                        gear_ratio: int = 1
                        for k in numbers: # for each line
                            for n in numbers[k]: # for each item in array of tuples
                                check_range: range = range(i - 1, i + 2)
                                if n[0] in check_range or n[1] in check_range: # i - 1 <= start/end index < i + 2
                                    part_numbers += 1
                                    gear_ratio *= n[2]

                    if part_numbers == 2:
                        sum += gear_ratio

            if lines[2] == BLANK_LINE: # exit condition
                break

            lines.pop(0) # delete first line
            lines.insert(2, '.' + file.readline().strip() + '.') # read a new line
            if lines[2] == '..':
                lines[2] = BLANK_LINE # to prevent out of bounds

            # delete first line
            if current_line_number - 1 in numbers.keys():
                del numbers[current_line_number - 1]

            current_line_number += 1

            # end of while
        # end of context object

    print(f'Sum: {sum:,}')
    print(f'Lines processed: {current_line_number:,}')
    return 0


if __name__ == '__main__':
    main()
