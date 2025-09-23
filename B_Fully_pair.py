'''B - Fully pair?'''
def main():
    '''main'''
    string = input()
    alpha_count = {}
    for char in string:
        if char not in alpha_count:
            alpha_count[char] = 1
        else:
            alpha_count[char] += 1

    stray = ''
    for char, count in alpha_count.items():
        if count % 2:
            stray += char
        else:
            continue

    print("fully paired" if not stray else stray)
if __name__ == "__main__":
    main()
