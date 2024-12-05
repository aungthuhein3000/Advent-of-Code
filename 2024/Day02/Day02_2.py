def main():
    file = open('/Users/aungthuhein/Documents/My documents/Code/My repos/Advent-of-Code/2024/Day02/input.txt')
    safe_reports = 0

    while True: # loop through entire file
        line = file.readline()
        levels = [int(x) for x in line.strip().split(' ') if x.isdigit()]

        if len(levels) < 2: # detect EOF or find at least two numbers in a line
            return False
        
        print("\n" + "#" * 40 + f"\n\nLevels: {levels}")

        ascending = report_asc_check(levels)
        descending = report_asc_check(levels[::-1])

        # ascending, descending = True, True # whether or not to keep checking for ascending and descending order. Keeps track of order so far.
        # ascending_unsafe_detected, descending_unsafe_detected = False, False # whether or not an unsafe level has been detected so far
        # i = 0
        # while ascending and i < nlevels - 1: # check all pairs of levels
        #     ascending = pair_asc_check(levels[i], levels[i + 1])
        #     if not ascending and not ascending_unsafe_detected:
        #         ascending_unsafe_detected = True
        #         if i + 2 < nlevels: # if there are more pairs left to the right
        #             ascending = pair_asc_check(levels[i], levels[i + 2])
        #             i += 1 # skip 1 level
        #         else: # This is the last pair which happens to be unsafe. Take it as safe because no more pairs remain to be checked.
        #             ascending = True
                
        #     i += 1


        # i = 0
        # while descending and i < nlevels - 1:
        #     descending = pair_asc_check(levels[i + 1], levels[i])
        #     if not descending and not descending_unsafe_detected:
        #         descending_unsafe_detected = True
        #         if i + 2 < nlevels:
        #             descending = pair_asc_check(levels[i + 2], levels[i])
        #             i += 1 # skip 1 level
        #         else:
        #             descending = True
            
        #     i += 1

        # after checking all levels
        if ascending or descending:
            safe_reports += 1
        
        print(f"Report result: {ascending or descending}")
        print(f"Number of safe reports: {safe_reports}") # Answer: 613 (wrong)
        # input("Press enter to continue... ")

    file.close()

def report_asc_check(report) -> bool:
    nlevels = len(report)
    ascending = True # whether or not to keep checking for ascending and descending order. Keeps track of order so far.
    ascending_unsafe_detected = False # whether or not an unsafe level has been detected so far
    i = 0
    while ascending and i < nlevels - 1: # check all pairs of levels
        ascending = pair_asc_check(report[i], report[i + 1])
        
        if not ascending and not ascending_unsafe_detected:
            ascending_unsafe_detected = True # first unsafe level detected
            if i + 2 < nlevels: # if there are more pairs left to check
                ascending = pair_asc_check(report[i], report[i + 2])
                i += 1 # skip 1 level
            else: # This is the last pair which happens to be unsafe. Take it as safe because no more pairs remain to be checked.
                ascending = True
            
        i += 1
    
    return ascending


def pair_asc_check(a: int, b: int) -> bool: # check for ascending order only
    return a < b and b - a <= 3

if __name__ == '__main__':
    main()
