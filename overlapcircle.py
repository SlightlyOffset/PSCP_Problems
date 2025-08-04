'''
Overlap circle
'''
from math import sqrt
def main():
    '''
    main
    '''
    x1 = int(input())
    y1 = int(input())
    r1 = int(input())
    x2 = int(input())
    y2 = int(input())
    r2 = int(input())

    dx = x1 - x2    # Find the distant from x1 to x2 (ignore -, +)
    dy = y1 - y2    # Find the distant from y1 to y2 (ignore -, +)
    sum_r = r1 + r2 # Find sum of radii for logic
    distance = sqrt(dx ** 2 + dy ** 2)      # Find distant between two circle center

    overlap = "overlapping" if distance <= sum_r else "no overlapping"
    print(overlap)
if __name__ == "__main__":
    main()
