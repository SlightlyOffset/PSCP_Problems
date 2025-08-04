'''
sequence I
'''

def main():
    '''
    main
    '''
    m = int(input())
    grid = [
        " ".join(str(i + j) for i in range(2, m + 2))
        for j in range(m)
    ]
    print("\n".join(grid))

if __name__ == "__main__":
    main()
