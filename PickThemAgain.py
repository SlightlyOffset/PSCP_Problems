'''PickThemAgain'''
def main():
    '''main'''
    number_list = input().split()
    valid_list = [number for number in number_list if not int(number) % 3 or not int(number) % 5]
    valid_list.reverse()
    print('\n'.join(valid_list) if valid_list else 'Nope')
if __name__ == '__main__':
    main()
