'''
GCD_N
'''
from math import gcd
from functools import reduce
def find_gcd(numbers):
    '''
    find gcd
    '''
    return reduce(gcd, numbers)

def main():
    '''
    main
    '''
    numbers = [int(input()) for _ in range(int(input()))]
    print(find_gcd(numbers))
if __name__ == "__main__":
    main()
