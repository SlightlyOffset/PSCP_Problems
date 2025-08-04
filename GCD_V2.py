'''
GCD V2
'''
def binary_gcd(a, b):
    '''
    find gcd using binary gcd algorithm
    '''
    if not a:
        return b
    if not b:
        return a

    # Count common factors of 2
    shift = 0
    while not (a | b) & 1:
        a >>= 1
        b >>= 1
        shift += 1

    # Remove remaining factors of 2 from a
    while not a & 1:
        a >>= 1

    while b:
        # Remove remaining factors of 2 from b
        while not b & 1:
            b >>= 1

        # Swap if necessary so a <= b
        if a > b:
            a, b = b, a

        b = b - a

    return a << shift

def main():
    '''
    main
    '''
    a = int(input())
    b = int(input())
    print(binary_gcd(a, b))
if __name__ == "__main__":
    main()
