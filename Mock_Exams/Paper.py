'''Paper'''
# X is the size of the paper A0 - A10
# Y is the size of the paper A0 - A10
# X is always larger or equal to Y in size
# How many Y needed to make X size paper

def main():
    '''main'''
    paper_x = input()
    paper_y = input()
    paper_size = ['A0', 'A1', 'A2', 'A3',
                  'A4', 'A5', 'A6', 'A7',
                  'A8', 'A9', 'A10']

    index_size_x = paper_size.index(paper_x)
    index_size_y = paper_size.index(paper_y)
    delta = abs(index_size_x - index_size_y)
    paper_used = 2 ** delta     # apply exponential growth
    print(paper_used)
if __name__ == '__main__':
    main()
