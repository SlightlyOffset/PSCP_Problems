'''
sequence VI
'''
def main():
    '''
    main
    '''
    m = int(input())
    grid = [
        " ".join(str(i * m + j + 1) for j in range(m))
        for i in range(m)
    ]
    print("\n".join(grid))

if __name__ == "__main__":
    main()
