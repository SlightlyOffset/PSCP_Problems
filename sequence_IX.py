'''Sequence IX'''
def main():
    '''main'''
    n = int(input())
    for i in range(1, n+1):
        # Generate the palindromic sequence for the current row
        up_seq = range(1, i + 1)
        down_seq = range(i - 1, 0, -1)
        full_seq = list(up_seq) + list(down_seq)

        # Format all numbers in the sequence to have two digits
        formatted_seq = [f"{num:02d}" for num in full_seq]

        # Print leading spaces for alignment, then join and print the sequence
        print(' ' * (n - i) * 3, end='')
        print(' '.join(formatted_seq))
if __name__ == "__main__":
    main()
