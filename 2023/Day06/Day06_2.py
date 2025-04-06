def main():
    file = open('input.txt')
    lines: list[str] = file.readlines()
    file.close()

    time_str: str = ''
    distance_str: str = ''

    input_nums: list[str] = lines[0].split(':')[1].strip().split(' ')
    for i in range(len(input_nums)):
        if input_nums[i].isdigit():
            time_str += input_nums[i]

    input_nums = lines[1].split(':')[1].strip().split(' ')
    for i in range(len(input_nums)):
        if input_nums[i].isdigit():
            distance_str += input_nums[i]
    
    time: int = int(time_str)
    distance: int = int(distance_str)

    record_times: int = 0
    for h in range(1, time):
        if (time - h) * h > distance:
            record_times += 1

    print(record_times) # answer: 41382569

if __name__ == '__main__':
    main()
