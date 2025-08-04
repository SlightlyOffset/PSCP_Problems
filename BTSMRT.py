'''
BTSMRT
'''

def main():
    '''
    main
    '''
    date = input()
    age = float(input())
    height = float(input())

    must_pay = True
    if age < 14 and height < 90:
        must_pay = False
    match date:
        case "Children Day":
            if age < 14 and height <= 140:
                must_pay = False
        case "Senior Day":
            if age >= 60:
                must_pay = False
        case _: # Normal Day
            if age < 14 and height < 90:
                must_pay = False

    print("PAY" if must_pay else "FREE")
if __name__ == "__main__":
    main()
