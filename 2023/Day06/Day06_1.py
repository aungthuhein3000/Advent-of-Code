def main():
    file = open('input.txt')
    lines: list[str] = file.readlines()
    file.close()

    times: list[int] = []
    distances: list[int] = []

    input_nums: list[str] = lines[0].split(':')[1].strip().split(' ')
    for i in range(len(input_nums)):
        if input_nums[i].isdigit():
            times.append(int(input_nums[i]))

    input_nums = lines[1].split(':')[1].strip().split(' ')
    for i in range(len(input_nums)):
        if input_nums[i].isdigit():
            distances.append(int(input_nums[i]))

    print(times)
    print(distances)

    total: int = 1
    for i in range(len(times)):
        record_times = 0
        for h in range(1, times[i]):
            if (times[i] - h) * h > distances[i]:
                record_times += 1
        total *= record_times
    
    print(total) # answer: 840336

if __name__ == '__main__':
    main()
