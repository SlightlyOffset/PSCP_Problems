'''Easy_Histogram'''
def main():
    '''main'''
    existed = {}
    string_in = input().strip()
    for char in string_in:
        if char == " ":
            continue
        if char not in existed:
            existed[char] = 1
        else:
            existed[char] += 1

    # Need further edit
    for char in sorted(existed.keys()):
        print(f"{char} = {existed[char]}")

if __name__ == '__main__':
    main()
