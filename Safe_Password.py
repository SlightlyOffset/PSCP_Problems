"""Safe Password"""
def main():
    """main"""
    password = "H 4567"
    char_in = input()
    digit_in = input()
    if char_in in password or digit_in in password:
        if char_in in password and digit_in not in password:
            print("safe locked - change digit")
        elif char_in not in password and digit_in in password:
            print("safe locked - change char")
        else:
            print("safe unlocked")
    else:
        print("safe locked")
if __name__ == "__main__":
    main()
