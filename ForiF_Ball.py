"""For!F-Ball"""
def main():
    '''main'''
    pattern = str(input())

    cf = True
    cs = False
    ct = False

    for i in pattern:
        match i :
            case "A":
                cf, cs = cs, cf
                continue
            case "B":
                cs, ct = ct, cs
                continue
            case "C":
                ct, cf = cf, ct
                continue
            case _ :
                break

    if cf:
        print(1)
    elif cs:
        print(2)
    elif ct:
        print(3)

if __name__ == "__main__":
    main()
