'''
Name of Card
'''
def processing(pre, suf):
    '''
    formatting into readable string
    '''
    scores = {
        "A" : "Ace",
        "J" : "Jack",
        "K" : "King",
        "Q" : "Queen",
        "2" : "2",
        "3" : "3",
        "4" : "4",
        "5" : "5",
        "6" : "6",
        "7" : "7",
        "8" : "8",
        "9" : "9",
        "10" : "10"
    }

    shapes = {
        "D" : "Diamonds",
        "H" : "Hearts",
        "S" : "Spades",
        "C" : "Clubs"
    }
    return f"{scores.get(pre, "")} of {shapes.get(suf, "")}"

def separation(name):
    '''
    separating Q from QC(Queen of Clubs) or 10 from 10S(10 of Spades)
    '''
    if len(name) == 2:
        pre = name[0]
        suf = name[1]
    else:
        pre = name[0:2]
        suf = name[2]
    return pre, suf

def main():
    '''
    main
    '''
    name = input().upper().strip()
    pre, suf = separation(name)
    print(processing(pre, suf))
if __name__ == "__main__":
    main()
