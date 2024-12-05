def main():
    file = open('test_input.txt')
    safe_reports = 0

    while True: # loop through entire file
        line = file.readline()
        levels = [int(x) for x in line.strip().split(' ') if x.isdigit()]

        if line == '' or len(levels) < 2: # detect EOF or find at least two numbers in a line
            break
        
        ascending, descending = True, True # whether or not to keep checking for ascending and descending order
        i = 0
        for i in range(len(levels) - 1): # check all pairs of levels
            if ascending: # if is necessary to keep track of all previous checked pairs
                ascending = safe_check(levels[i], levels[i + 1])
            if descending:
                descending = safe_check(levels[i + 1], levels[i])
            
            i += 1

            if not(ascending or descending): # if the current report is not valid in either way
                break # For efficiency. Not strictly necessary.
        
        # after checking all levels
        if ascending or descending:
            safe_reports += 1
        
    print(f"Number of safe reports: {safe_reports}") # Answer: 591

    file.close()

def safe_check(a: int, b: int): # check for ascending order only
    diff = abs(a - b)
    return a < b and (diff >= 1 and diff <= 3)

if __name__ == '__main__':
    main()
