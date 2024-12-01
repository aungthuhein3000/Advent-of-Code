def main():
    file_input = open('/Users/aungthuhein/Documents/My Documents/Code/Advent of Code/2023/Day01/input.txt')
    lines = file_input.readlines()
    total = 0

    for line in lines:
        n1, n2 = searchDigits(line)
        total += n1 * 10 + n2

    print(total)

    file_input.close()

def searchDigits(line) -> tuple:
    length = len(line)

    if line.strip() == '' or length < 1:
        return 0, 0

    spelledDigits = {'one': 1, 'two': 2, 'three': 3, 'four': 4,
                     'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    
    first_num = 0
    first_num_pos = length # position of first number
    last_num = 0
    last_num_pos = -1 # position of last number

    # find spelled digits
    for digit in spelledDigits.keys():
        # find first spelled digit
        find_result = line.find(digit)
        if find_result != -1 and find_result < first_num_pos:
            first_num = spelledDigits[digit]
            first_num_pos = find_result
    
        # find last spelled digit
        for i in range(3, length):
            index = length - i
            find_result = line[index:length].find(digit)
            if find_result != -1 and index > last_num_pos:
                last_num = spelledDigits[digit]
                last_num_pos = index
                break

    # print(f"Line: {line.strip()}. {first_num}, {last_num}")

    # find first literal digit
    for index in range(length):
        if line[index].isdigit() and index < first_num_pos:
            first_num_pos = index
            first_num = int(line[index])
            break
    
    # find last literal digit
    for index in range(length - 1, -1, -1):
        if line[index].isdigit() and index > last_num_pos:
            last_num_pos = index
            last_num = int(line[index])
            break

    # print(f"Line: {line.strip()}. {first_num}, {last_num}")
    # input(f"Press enter to continue... ")

    return first_num, last_num


if __name__ == "__main__":
    main()
