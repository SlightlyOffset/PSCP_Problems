"""leap"""
def main():
    """year"""
    year = int(input())
    if not year % 100:
        if not year % 4 and not year % 400:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    elif not year % 4:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
main()
