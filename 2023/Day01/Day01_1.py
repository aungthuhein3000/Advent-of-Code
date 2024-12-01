def main():
    file_input = open('input.txt')
    lines = file_input.readlines()
    total = 0

    for line in lines:
        total += calibration_value(line)

    print(f"Total: {total}")

    file_input.close()

def calibration_value(line) -> int:
    
    value: str = '0'

    if line.strip() == '':
        return 0

    index = 0
    while index < len(line) and not line[index].isdigit():
        index += 1
    if index < len(line):
        value += line[index]

    index = len(line) - 1
    while index >= 0 and not line[index].isdigit():
        index -= 1
    if index >= 0:
        value += line[index]

    return int(value)

if __name__ == '__main__':
    main()
