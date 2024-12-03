def main():
    file = open("input.txt")

    list1 = []
    list2 = []

    for line in file:
        if len(line.strip()) > 2: # at least 3 characters
            ids = [x for x in line.strip().split(' ') if x.isdigit()]
            list1.append(int(ids[0]))
            list2.append(int(ids[1]))
    
    score = 0 # similarity score
    for left_loc_id in list1:
        found = 0
        for right_loc_id in list2:
            if left_loc_id == right_loc_id:
                found += 1
        score += left_loc_id * found
    
    print(f"Similarity score: {score}") # answer: 21271939

    file.close()

if __name__ == '__main__':
    main()
