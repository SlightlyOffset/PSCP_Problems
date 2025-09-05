'''Duplicate'''
def main():
    '''main'''
    m = int(input())
    n = int(input())
    set_m = set(input() for _ in range(m))
    set_n = set(input() for _ in range(n))
    print("Nope" if set_m.isdisjoint(set_n) \
          else '\n'.join(sorted(set_m.intersection(set_n), reverse=True)))
if __name__ == '__main__':
    main()
