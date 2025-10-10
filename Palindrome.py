"""Palindrome"""
def is_palindrome(word:str):
    """check if palindrome"""
    return word == word[::-1]

def main():
    """main"""
    count_goal = int(input())
    count = 0
    start_time = input()
    hour = int(start_time[0:2] if len(start_time) >= 5 else start_time[0:1])
    mn = int(start_time[-2:])

    while True:
        if mn + 1 >= 60:
            mn = 0
            if hour + 1 >= 24:
                hour = 0
            else:
                hour += 1
        else:
            mn += 1

        if is_palindrome(f"{hour}{mn:02}"):
            print(f"{hour}:{mn:02}")
            count += 1
            if count >= count_goal:
                return

if __name__ == "__main__":
    main()
