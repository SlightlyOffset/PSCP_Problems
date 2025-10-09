'''HorizontalHistogram'''
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

    # for char in sorted(existed.keys(), key=lambda x: (x.lower(), -ord(x))):
    #     for char, count in existed:
    #         print(f"{char} : {count * '-'}")
    existed = sorted(existed.items(), key=lambda x: (x[0].lower(), -ord(x[0])))
    for char, count in existed:
        print(f"{char} : {count * '-'}")
if __name__ == '__main__':
    main()
