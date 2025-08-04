'''
sequence I
'''
def main():
    '''
    main
    '''
    m = int(input())
    n = int(input())
    grid = [
        " ".join(str(i * n + j + 1) for j in range(n))
        for i in range(m)
    ]
    print("\n".join(grid))

if __name__ == "__main__":
    main()
