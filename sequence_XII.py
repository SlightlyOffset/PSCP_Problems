'''Sequence XII'''
def main():
    '''main'''
    n = int(input().strip())
    size = 2 * n -1
    center = n - 1
    for i in range(size):
        row = []
        di = abs(i - center)
        for j in range(size):
            dj = abs(j - center)
            val = n - abs(di - dj)
            row.append(f"{val:02d}")
        print(' '.join(row))
if __name__ == "__main__":
    main()
