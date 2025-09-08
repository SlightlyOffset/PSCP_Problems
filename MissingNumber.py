'''MissingNumber'''
def main():
    '''main'''
    set_max_range = int(input())
    provided_numbers = set()

    while True:
        number_input = int(input())
        if not number_input:
            break
        provided_numbers.add(number_input)

    # Use a generator expression to find missing numbers without creating a large set in memory.
    # This is much more memory-efficient for a large set_max_range.
    missing_numbers = (i for i in range(1, set_max_range + 1) if i not in provided_numbers)
    print(*sorted(missing_numbers), sep="\n")

if __name__ == '__main__':
    main()
