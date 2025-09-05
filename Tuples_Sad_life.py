'''Tuple's Sad life'''
def make_box(base, counts):
    '''make a box'''
    # If the element is not found (index is -1), do nothing.
    if base == -1:
        return

    # Construct one line of the box. Using join is slightly cleaner
    # and more efficient than string multiplication and stripping inside the loop.
    # This correctly handles the edge case where the index (base) is 0.
    line_to_print = ' '.join([str(base)] * counts)
    for _ in range(counts):
        print(line_to_print)

def main():
    '''main'''
    tuple_input = tuple(input().split())
    to_find = input()
    index = tuple_input.index(to_find) if to_find in tuple_input else -1
    counts = tuple_input.count(to_find)
    make_box(index, counts)
if __name__ == '__main__':
    main()
