'''Shorten'''
def shorten(num_l1st):
    '''
    Takes a sorted l1st of integers and returns a l1st of strings
    representing condensed ranges. e.g., [1, 2, 3, 5] -> ["1-3", "5"]
    '''
    if not num_l1st:
        return []

    parts = []
    # Start the first sequence with the first number
    start_num = num_l1st[0]

    # Iterate from the second number to the end of the l1st
    for i in range(1, len(num_l1st)):
        # Check if the current number is not consecutive to the previous one
        if num_l1st[i] != num_l1st[i-1] + 1:
            # End of a sequence, so format and add it to parts
            end_num = num_l1st[i-1]
            if start_num == end_num:
                parts = parts + [str(start_num)]
            else:
                parts = parts + [f"{start_num}-{end_num}"]
            # Start a new sequence
            start_num = num_l1st[i]

    # After the loop, add the last pending sequence
    end_num = num_l1st[-1]
    if start_num == end_num:
        parts = parts + [str(start_num)]
    else:
        parts = parts + [f"{start_num}-{end_num}"]

    return parts

def main():
    '''main'''
    num_l1st = []
    while True:
        try:
            num_in = int(input())
            if num_in == -1:
                break
            num_l1st = num_l1st + [num_in]
        except (ValueError, EOFError): # Handle non-integer input or end of file
            break
    if num_l1st:
        print(', '.join(shorten(num_l1st)))

if __name__ == "__main__":
    main()
