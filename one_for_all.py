'''
One For All
'''

def main():
    '''
    main
    '''
    gen = int(input())
    members = [input() for _ in range(gen)]

    decorated_string = ""
    for index, member in enumerate(members):
        if index == (gen - 1):        # Last member of the list
            decorated_string += f"{member}_{gen}"
            continue        # Do the same as break in this case

        if not index % 2:       # Index is odd (index + 1)
            decorated_string += f"{member}{'*' * (index + 1)}"
        else:       # Index is even (index + 1)
            decorated_string += f"{member}{'-' * (index + 1)}"

    print(decorated_string)
if __name__ == "__main__":
    main()
