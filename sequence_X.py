'''Sequence X'''
def print_line(level, size):
    '''print line'''
    print(' ' * (3 *(size - level)), end='')

    first = True
    for i in range(1, level + 1):
        if not first:
            print(' ', end='')
        print(f"{i:02d}", end='')
        first = False

    for i in range(level - 1, 0, -1):
        print(' ', end='')
        print(f"{i:02d}", end='')

    print()

def main():
    '''main'''
    n = int(input())
    for i in range(1, n+1):
        print_line(i, n)

    for i in range(n-1, 0, -1):
        print_line(i, n)

if __name__ == "__main__":
    main()
