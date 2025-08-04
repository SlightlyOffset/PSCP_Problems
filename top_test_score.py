'''
top test score
'''
def main():
    '''
    main
    '''
    score = [input() for _ in range(int(input()))]
    top_score = max(score)
    top_amount = score.count(top_score)
    print(top_score)
    print(top_amount)
if __name__ == "__main__":
    main()
