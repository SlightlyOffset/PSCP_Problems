""" T-score """
import math
def main():
    """ T-score """
    n = int(input())
    m = int(input())
    all_score = 0
    all_score_2 = 0
    list_score = []
    _ = m
    for _ in range(n):
        score = int(input())
        list_score.append(score)
        all_score+=score
        all_score_2+= score**2
    sd = math.sqrt((n*all_score_2 - (all_score**2)) / (n*(n-1)))
    mean = all_score / n
    for i in list_score:
        z = (i-mean)/sd
        if not sd:
            t_score = 50.00
            print(f"{t_score:.2f}")
        else:
            t_score = 50+10*z
            print(f"{t_score:.2f}")

if __name__ == "__main__":
    main()
