'''Diamond_I'''
def main():
    '''main'''
    depth = int(input())
    width = int(input())
    mine = []
    for _ in range(depth):
        mine.append(list(map(int, input().split())))

    column_vain = list(zip(*mine))

    max_sum = float('-inf')
    for column in range(width):
        current_sum = sum(column_vain[column])
        if current_sum > max_sum:
            max_sum = current_sum
    print(max_sum)

if __name__ == "__main__":
    main()
