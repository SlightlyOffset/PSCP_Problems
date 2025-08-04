'''doc'''
def main():
    '''doc'''
    a = abs(int(input()))
    b = abs(int(input()))
    c = abs(int(input()))
    a_2 = a
    b_2 = b
    c_2 = c

    count_loop1 = 0
    count_loop2 = 0
    while  0 <= a < b < c <= 10000000:

        a += 1
        b += 1
        count_loop1 += 1
        if a + 1 == b:
            break
        if b + 1 == c:
            break

    while  0 <= a_2 < b_2 < c_2 <= 10000000:
        count_loop2 += 1
        a_2 -= 1
        b_2 -= 1

        if a_2 - 1 == b:
            break
        if b_2 - 1 == c:
            break
    if count_loop1 >= count_loop2:
        print(count_loop1)
    if count_loop2 >= count_loop1:
        print(count_loop2-1)
main()
