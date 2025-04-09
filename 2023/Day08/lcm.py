from functools import reduce
import math

def lcm(numbers: list[int]) -> int:
    numbers = list(set(numbers))
    # dict of int to dicts
    # 45 = 3 * 3 * 5 => {45: {3: 2, 5: 1}, ...}
    factor_counts: dict[int, dict[int, int]] = {}
    for number in numbers:
        factors: list[int] = factorize(number) # now a list
        for f in factors:
            if not factor_counts.get(number): # check if key exists
                factor_counts[number] = {}

            if factor_counts[number].get(f):
                factor_counts[number][f] += 1
            else:
                factor_counts[number][f] = 1

    mult: dict[int, int] = {}
    for k1 in factor_counts.keys():
        for k2 in factor_counts[k1]:
            if mult.get(k2):
                if mult[k2] < factor_counts[k1][k2]:
                    mult[k2] = factor_counts[k1][k2]
            else:
                mult[k2] = factor_counts[k1][k2]
    
    lcm_result: int = 1
    for m in mult:
        lcm_result *= m ** mult[m]
    print(f'My lcm of {numbers}: {lcm_result:,}')
    print(f'math.lcm(): {math.lcm(*numbers):,}')
    return lcm_result


# https://stackoverflow.com/a/6800214/5747214
def pasta_factorize(n: int):
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def factorize(number: int) -> list[int]:
    denominator: int = 2 # start dividing by 2
    number_copy: int = number
    factors: list[int] = []
    while denominator < number_copy:
        if number_copy % denominator == 0:
            number_copy = number_copy // denominator
            factors.append(denominator)
            denominator = 2
        else:
            denominator += 1

    factors.append(number_copy)
    return factors

    
def main():
    while True:
        entry = input('Please enter an integer: ')

        if entry == '':
            return

        try:
            entry = int(entry)
            factorize(entry)
        except ValueError as ve:
            print(f"'{entry}' is not a number. Please enter a number.")

if __name__ == '__main__':
    lcm([19631, 17287, 12599, 23147, 13771, 20803])