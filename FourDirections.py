'''FourDirections'''
def main():
    '''main'''
    # init direction lists
    up = [
        "  *   ",
        " ***  ",
        "* * * ",
        "  *   ",
        "  *   "
    ]
    down = [
        "  *   ",
        "  *   ",
        "* * * ",
        " ***  ",
        "  *   "
    ]
    left = [
        "  *   ",
        " *    ",
        "***** ",
        " *    ",
        "  *   "
    ]
    right = [
        "  *   ",
        "   *  ",
        "***** ",
        "   *  ",
        "  *   "
    ]

    # direction dict
    directions = {
        "U": up,
        "D": down,
        "L": left,
        "R": right
    }
    direction_seq = input().strip()
    for i in range(5):
        line = ''.join(directions[char][i] for char in direction_seq)
        print(line)

if __name__ == '__main__':
    main()
