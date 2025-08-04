'''
sequence II
'''

def main():
    '''
    main
    '''
    m = int(input())
    grid = [
        " ".join(str(i * m + j) for i in range(m))
        for j in range(m)
    ]
    print("\n".join(grid))

if __name__ == "__main__":
    main()
