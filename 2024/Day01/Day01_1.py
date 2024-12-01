def main():
    file = open("input.txt")

    list1 = []
    list2 = []

    for line in file:
        if len(line.strip()) > 2: # at least 3 characters
            ids = [x for x in line.strip().split(' ') if x.isdigit()]
            list1.append(int(ids[0]))
            list2.append(int(ids[1]))
        
    list1 = sorted(list1)
    list2 = sorted(list2)

    total_distance = 0
    for location_index in range(len(list1)):
        total_distance += abs(list1[location_index] - list2[location_index])
    
    print(f"Total distance: {total_distance}") # answer: 2367773

    file.close()

if __name__ == '__main__':
    main()