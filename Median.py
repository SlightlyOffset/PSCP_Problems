'''Median'''
from statistics import median
def get_median(data):
    '''find the median'''
    return median(data)

def process_data(data_input):
    '''process the data input and return'''
    processed_data = []
    for data in data_input.split(', '):
        processed_data.append(float(data))
    return processed_data

def main():
    '''main'''
    data_input = input()
    processed_data = process_data(data_input)
    print(f"{get_median(processed_data):.2f}")
if __name__ == '__main__':
    main()
