'''LastStand'''
import json
def main():
    '''main'''
    # Main goal is to just take list input [...] and print last letter or digit of each element
    input_list = json.loads(input())
    for element in input_list:
        print(str(element)[-1])
if __name__ == '__main__':
    main()
