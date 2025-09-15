'''Dart'''
from math import sqrt

def calculate_score(x, y):
    '''Calculates and returns the score for a single dart throw.'''
    # Calculate distance from origin(0,0)
    distance = sqrt(x**2 + y**2)
    if distance <= 2:
        return 5
    if distance <= 4:
        return 4
    if distance <= 6:
        return 3
    if distance <= 8:
        return 2
    if distance <= 10:
        return 1
    return 0

def main():
    '''main'''
    n = int(input())
    total_score = 0
    for _ in range(n):
        x, y = input().split()
        x = int(x)
        y = int(y)
        total_score += calculate_score(x, y)
    print(total_score)

if __name__ == "__main__":
    main()
