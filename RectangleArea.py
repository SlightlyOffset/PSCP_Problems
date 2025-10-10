'''rectyangle'''
def main():
    '''main'''
    recA = input().split()
    recB = input().split()
    x1 = int(recA[0]) + int(recA[2])
    x2 = int(recB[0]) + int(recB[2])
    y1 = int(recA[1]) + int(recA[3])
    y2 = int(recB[1]) + int(recB[3])
    over_x = min(x1,x2) - max(int(recA[0]),int(recB[0]))
    over_y = min(y1,y2) - max(int(recA[1]),int(recB[1]))
    if over_x > 0 and over_y > 0:
        print(over_x * over_y)
    else:
        print("no overlapping")

if __name__ == "__main__":
    main()
