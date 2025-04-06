def main():
    file_input = open(r'input.txt')
    lines: list[str] = file_input.readlines()
    total: int = 0

    for line in lines:
        n1, n2 = searchDigits(line)
        total += n1 * 10 + n2

    print(total) # answer: 55413

    file_input.close()

def searchDigits(line: str) -> tuple[int, int]:
    length: int = len(line)

    if line.strip() == '' or length < 1:
        return 0, 0

    spelledDigits: dict[str, int] = {'one': 1, 'two': 2, 'three': 3, 'four': 4,
                     'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    
    first_num: int = 0
    first_num_pos: int = length # position of first number
    last_num: int = 0
    last_num_pos: int = -1 # position of last number

    # find spelled digits
    for digit in spelledDigits.keys():
        # find first spelled digit
        find_result: int = line.find(digit)
        if find_result != -1 and find_result < first_num_pos:
            first_num = spelledDigits[digit]
            first_num_pos = find_result
    
        # find last spelled digit
        for i in range(3, length):
            index: int = length - i
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
