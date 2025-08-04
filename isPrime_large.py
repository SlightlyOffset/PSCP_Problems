'''
is prime?
'''
from math import ceil, sqrt
def is_prime(number):
    '''
    return True if the number is prime else False
    '''
    if number <= 1:
        return False
    if number == 2:
        return True

    limit = ceil(sqrt(number))
    for divisor in range(2, limit + 1, 1):
        if not number % divisor:
            return False
    return True

def main():
    '''
    main
    '''
    print("YES" if is_prime(int(input())) else "NO")
if __name__ == "__main__":
    main()
