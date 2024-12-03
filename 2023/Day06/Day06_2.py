def main():
    file = open('/Users/aungthuhein/Documents/My documents/Code/Advent of Code/2023/Day06/input.txt')
    lines = file.readlines()

    time_str = ''
    distance_str = ''

    input_nums = lines[0].split(':')[1].strip().split(' ')
    for i in range(len(input_nums)):
        if input_nums[i].isdigit():
            time_str += input_nums[i]

    input_nums = lines[1].split(':')[1].strip().split(' ')
    for i in range(len(input_nums)):
        if input_nums[i].isdigit():
            distance_str += input_nums[i]
    
    time = int(time_str)
    distance = int(distance_str)

    record_times = 0
    for h in range(1, time):
        if (time - h) * h > distance:
            record_times += 1

    print(record_times)

    file.close()

if __name__ == '__main__':
    main()
