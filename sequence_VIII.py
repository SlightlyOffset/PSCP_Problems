'''Sequence VIII'''
def main():
    '''main'''
    n = int(input())
    spacing = n - 1
    num_list = []
    for i in range(1, n+1):
        if i < 10:
            num_list.append('0' + str(i)) # Add '0' prefix for single-digit numbers
        else:
            num_list.append(str(i)) # No '0' prefix for double-digit numbers

        print(' ' * (spacing * 3), end='') # Print leading spaces
        print(*num_list) # Print the current sequence
        spacing -= 1
if __name__ == "__main__":
    main()
