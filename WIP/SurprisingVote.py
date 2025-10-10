"""SuprisingVote"""
def main():
    '''main'''
    total = float(input())
    max_num = float(input())
    total -= max_num

    def get_min_num():
        """ get min """
        if total >= max_num:
            return total - max_num
        return 0

    max_num = get_min_num()

    if max_num - max_num > 2:
        print("Surprising")
    else:
        print("Not surprising")

if __name__ == "__main__":
    main()
