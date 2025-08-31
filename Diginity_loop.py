'''
Diginity (loop)
'''

def diginity(id_in):
    '''Diginity'''
    n = id_in
    while n > 9:
        n = sum(int(d) for d in str(n))
    print(n)

def main():
    '''main'''
    while True:
        id_in = int(input())
        if not id_in:   # id_in == 0
            break
        diginity(id_in)
if __name__ == '__main__':
    main()
