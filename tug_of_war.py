'''
tug of war
'''

def main():
    '''
    main
    '''
    A = 0
    B = 0
    for _ in range(10):
        A += int(input())
    for _ in range(10):
        B += int(input())

    if A == B:
        print("AB")
    elif A > B:
        print("B")
    else:
        print("A")
if __name__ == "__main__":
    main()
