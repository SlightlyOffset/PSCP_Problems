"""pong"""
def main():
    """ya"""
    num = int(input())
    buf = ""
    if (not num % 3) or str(num)[-1] == "3":
        buf = "PONG"
        print(buf)
    else:
        print(num)
    # num = str(num)
    # if num[-1] == "3":
        # buf = "PONG"
    # else:
        # buf = num
    # print(buf)
main()
