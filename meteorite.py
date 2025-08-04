'''
Meteorite
'''

def nuke_meteorite(size, split_into, safe):
    '''
    Nuke the meteorite till its safe size
    '''
    if size < safe:
        return 0

    fragment_size = size / split_into

    return 1 + split_into * nuke_meteorite(fragment_size, split_into, safe)

def main():
    '''
    main
    '''
    meteorite_size = float(input())
    split_into = int(input())
    safe_size = float(input())

    print(nuke_meteorite(meteorite_size, split_into, safe_size))
if __name__ == "__main__":
    main()
