'''
Cyan's password generator
'''

def main():
    '''
    main
    '''
    fname = input()
    lname = input()
    age = input()

    password = ""
    if len(fname) >= 5 and len(lname) >= 5:
        password += fname[0:2]
        password += lname[-1]
        password += age[-1]
    else:
        password += fname[0]
        password += age
        password += lname[-1]
    print(password)
if __name__ == "__main__":
    main()
