def main():
    file_input  = open(r'input.txt')
    lines: list[str] = file_input.readlines()
    total: int = 0

    for line in lines:
        total += calibration_value(line)

    print(f"Total: {total}")

    file_input.close()

def calibration_value(line: str) -> int:
    
    value: str = '0' # not an int. The '0' is for when there's no numbers in the line

    if line.strip() == '':
        return 0

    index: int = 0
    while index < len(line) and not line[index].isdigit():
        index += 1
    if index < len(line):
        value += line[index] # concat as a string

    index = len(line) - 1 # reusing a variable
    while index >= 0 and not line[index].isdigit():
        index -= 1
    if index >= 0:
        value += line[index]

    return int(value)

if __name__ == '__main__':
    main()
