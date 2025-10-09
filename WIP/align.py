'''
align
'''
def main():
    '''
    main
    '''
    space = int(input())
    align = input().lower().strip()
    text = input()
    match align:
        case "left":
            print(f"{text}{" " * (space - len(text))}")
        case "right":
            print(f"{" " * (space - len(text))}{text}")
        case "center":
            mid_space = (space - len(text)) // 2
            mod = (space - len(text)) % 2
            print(f"{" " * (mid_space + mod)}{text}{" " * mid_space}")
if __name__ == "__main__":
    main()
