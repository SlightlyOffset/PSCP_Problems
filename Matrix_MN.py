'''Matrix_MN'''
def construct_matrix():
    '''make a matrix of given size m*n'''
    m = int(input())
    n = int(input())
    matrix = []
    row = []
    for _ in range(m):
        for _ in range(n):
            row.append(input())
        matrix.append(row)
        row = []
    print('\n'.join([' '.join(cell for cell in row) for row in matrix]))

def main():
    '''main'''
    construct_matrix()
if __name__ == '__main__':
    main()
