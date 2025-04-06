def main():
    file = open(r'/Users/aungthuhein/Documents/My documents/Code/Advent of Code/2023/Day03/test_input.txt')

    lines = [] # Process 3 lines at a time: 0 = last line, 1 = current line, 2 = next line
    lines.insert(0, '.' + file.readline().strip() + '.') # read first line
    lines.insert(0, '.' * (len(lines[0]))) # set first line as a border of dots
    lines.insert(2, '.' + file.readline().strip() + '.') # read next line

    line_length = len(lines[0])

    # array of Booleans to keep track of places adjacent to special characters
    specials = [[False for _ in range(line_length)] for __ in range(3)]

    while lines[1] != '..' and lines[2] != '..':

        # update "adjacent" zone
        for i in range(1, 3):
            for j in range(1, line_length - 1):
                if lines[i][j] != '.' and not lines[i][j].isdigit():
                    specials[i][j] = True # mark the special character itself
                    specials[i][j - 1] = specials[i][j + 1] = True # left and right
                    specials[i - 1][j - 1] = specials[i - 1][j] = specials[i - 1][j + 1] = True # above 3

        numbers = find_numbers(lines[1])

        print('\n\n' + ('#' * 30) + f"\nLines: ")
        custom_print(lines)
        print(f"\nNumbers: {numbers}")
        print(f"\nSpecials: ")
        custom_print(specials)
        input('Press enter to continue... ')
        # for number in numbers:
        #     take_number = False
        #     for index in range(number[0], number[1]):
        #         if specials[1][index]:
        #             take_number = True
        #             break

        lines.pop(0) # remove last line
        lines.insert(2, '.' + file.readline().strip() + '.') # read next line

        specials.pop(0) # remove last line
        specials.insert(2, [0 for _ in range(line_length)])
            
    file.close()

def custom_print(list2d):
    # print('[', end = "")
    for row in list2d:
        print('[', end = "")
        for index in range(len(row)):
            print(f"{row[index]:>2}", end = "")
        print("]")


    # print(']')
        

def find_numbers(line):
    length = len(line)
    numbers_list = []

    i = 0 # top-level iterator
    while i < length:
        num = 0
        j = i # to look for digits
        while j < length and line[j].isdigit():
            num = (num * 10) + int(line[j])
            j += 1
        
        if num > 0:
            numbers_list.append([i, j, num])
            i = j
        i += 1

    return numbers_list

if __name__ == '__main__':
    main()
