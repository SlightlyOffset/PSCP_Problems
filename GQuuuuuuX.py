"""GQuuuuuuX"""
def main():
    '''main'''
    word = input().strip()
    size = len(word)
    i = 0
    max_u = 0
    found = False

    while i < size:
        if i + 1 < size and word[i].lower() == 'g' and word[i+1].lower() == 'q':
            i += 2
            count_u = 0
            while i < size and word[i].lower() == 'u':
                count_u += 1
                i += 1
            if i < size and word[i].lower() == 'x' and count_u > 0:
                found = True
                if count_u > max_u:
                    max_u = count_u
        else:
            i += 1
    print(max_u if found else "None")

if __name__ == "__main__":
    main()
