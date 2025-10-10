""" US Interstate Number System """
def main():
    """ main """
    num = int(input().strip())

    def is_major(num):
        """ check if is major highway """
        return 1 <= num <= 99 and (not num % 5)

    if 1 <= num <= 99:
        if not num % 10:
            print("Horizontal Major Interstate")
            print(f"I-{num}")
        elif not num % 5:
            print("Vertical Major Interstate")
            print(f"I-{num}")
        else:
            print("Others")
    elif 100 <= num <= 999:
        first_digit = num // 100
        parent = num % 100
        if is_major(parent):
            if not first_digit % 2:
                print("Even Minor Interstate")
            else:
                print("Odd Minor Interstate")
            print(f"I-{parent}")
        else:
            print("Others")
    else:
        print("Others")

if __name__ == "__main__":
    main()
