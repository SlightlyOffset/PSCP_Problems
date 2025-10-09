'''Sequence XI'''
def main():
    '''main'''
    n = int(input().strip())
    size = 2 * n - 1
    center = n - 1

    for i in range(size):
        row = []
        for j in range(size):
            val = n - max(abs(i - center), abs(j - center))
            row.append(f"{val:02d}")
        print(' '.join(row))
if __name__ == "__main__":
    main()
