'''Shorten'''
def shorten(num_l1st):
    '''shorten'''
    begin = None
    end = None
    parts = []
    for num in num_l1st[1::]:
        if num - 1 == num_l1st[num_l1st.index(num) - 1]:
            if begin is None:
                begin = num_l1st[num_l1st.index(num) - 1]
            end = num

        else:   # Current number not match current - 1 (Not continous)
            if begin is not None:
                parts.append(f"{begin}-{end}")
                begin = None
                end = None
            else:
                parts.append(str(num_l1st[num_l1st.index(num) - 1]))

    if begin is not None:       # Handle last item after the loop
        parts.append(f"{begin}-{end}")

    return parts

def main():
    '''main'''
    num_l1st = []
    while True:
        num_in = int(input())
        if num_in == -1:
            break
        num_l1st.append(num_in)
    print(', '.join(shorten(num_l1st)))
if __name__ == "__main__":
    main()
