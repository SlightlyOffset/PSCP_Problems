'''PickThem'''
import json
def main():
    '''main'''
    # Guaranteed list format input e.g. [...]
    input_list = json.loads(input())
    even = [number for number in input_list if not number % 2]
    print('\n'.join(map(str, (x for x in even))) if even else 'Nope')
if __name__ == '__main__':
    main()
