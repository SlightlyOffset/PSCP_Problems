'''MissingNumber'''
def main():
    '''main'''
    original_set = set()
    set_max_range = int(input())
    compare_set = set(range(1, set_max_range + 1))
    while True:
        number_input = int(input())
        if not number_input:
            break
        original_set.add(number_input)
    print(*sorted(compare_set - original_set), sep="\n")

if __name__ == '__main__':
    main()
