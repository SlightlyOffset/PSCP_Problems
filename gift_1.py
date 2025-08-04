'''
gift
'''

def main():
    '''
    main
    '''
    avg_weight = float(input())
    the_me_box = float(input())

    # avg = (the_me_box + the_friend_box) / 2
    # 0 = ((the_me_box + the_friend_box) / 2) - avg
    # the_friend_box = (avg * 2) - the_me_box

    the_friend_box = (avg_weight * 2) - the_me_box
    print(the_friend_box)

if __name__ == "__main__":
    main()
