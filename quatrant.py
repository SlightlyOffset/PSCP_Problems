'''
quadrant
'''

def main():
    '''
    main
    '''
    x = int(input())
    y = int(input())

    if not x and not y:
        print("O")
    elif not x:
        print("Y")
    elif not y:
        print("X")
    elif x > 0:
        print("Q1" if y > 0 else "Q4")
    else:
        print("Q2" if y > 0 else "Q3")

if __name__ == "__main__":
    main()
