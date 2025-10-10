"""Giraffee"""
def main():
    """ main """
    nums = int(input())
    giraffee = []

    for _ in range(nums):
        giraffee.append(int(input()))

    count = 0
    if len(giraffee) == 1:
        print(1)
        return

    for index, g in enumerate(giraffee):
        if not index and g > giraffee[index + 1]:
            count += 1
            continue
        if index == len(giraffee) - 1 and g > giraffee[index - 1]:
            count += 1
            continue
        if ((len(giraffee) - 1)>index > 0) and  g> giraffee[index+1] and g>giraffee[index-1] :
            count += 1
    print(count)

if __name__ == "__main__":
    main()
