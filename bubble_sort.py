def bubble(score):
    '''
    bubble s0rt algo
    take arr[] of score
    '''
    n = len(score)
    for i in range(n):
        # Flag for performance improvement
        swapped = False
        for j in range(0, n - i - 1):
            if score[j] < score[j + 1]:     # Reverse bubble
                score[j], score[j + 1] = score[j + 1], score[j]
                swapped = True
        if not swapped:
            break
    return score
