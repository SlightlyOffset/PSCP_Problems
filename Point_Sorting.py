'''Point Sorting'''
def output(points_list):
    '''output'''
    for points in points_list:
        for point in points:
            print(f"{point[0]} {point[1]}")

def sorting(points):
    '''sorting'''
    # 1. Primary sort by the sum of coordinates (x+y) in ascending order.
    # 2. Secondary sort (tie-breaker): if sums are equal, sort by the y-coordinate
    #    in descending order.
    return sorted(points, key=lambda point: (point[0] + point[1], point[1]), reverse=False)

def main():
    '''main'''
    point_set = int(input())
    holder = []
    for _ in range(point_set):
        point_pair = int(input())
        points = []
        for _ in range(point_pair):
            points.append(tuple(map(int, input().split())))
        holder.append(sorting(points))
    output(holder)

if __name__ == '__main__':
    main()
