'''Key'''
def main():
    '''main'''
    id_num = input()
    sum_id = 0

    # 1. Find sum of all 13 digits number
    sum_id = sum(int(digit) for digit in id_num)

    # 2. Multiply last 3 digits by 10
    last_three = id_num[10:13]
    multiple_product = int(last_three) * 10

    # 3. Find sum of 1. and 2. to get key.
    #    if key larger than 9999 use only in the 9999 range
    #    if key smaller than 1000(less than 4 digits long) add 1000
    sum_product = sum_id + multiple_product
    if sum_product > 9999:
        key = sum_product % 10000
    elif sum_product < 1000:
        key = sum_product + 1000
    else:
        key = sum_product

    print(f"{key:04d}")
if __name__ == '__main__':
    main()
