'''
turnstile (OOP)
'''
class Turnstile:
    '''
    a turnstile
    '''
    def __init__(self):
        '''
        create a turnstile object
        '''
        self.state = "Locked"
        self.passes = 0

    def coin(self):
        '''
        inserted a coin
        '''
        self.state = "Unlocked"

    def push(self):
        '''
        pushed the turnstile arm
        '''
        if self.state == "Unlocked":
            self.state = "Locked"
            self.passes += 1

    def handle(self, action):
        '''
        handle actions
        '''
        match action:
            case "C":
                self.coin()
            case "P":
                self.push()

    def get_passes(self):
        '''
        return how many people walk past the turnstile
        '''
        return self.passes

def main():
    '''
    main
    '''
    turnstile_1 = Turnstile()
    while True:
        act = input().strip().upper()
        if act == "END":
            break
        turnstile_1.handle(act)
    print(turnstile_1.get_passes())
if __name__ == "__main__":
    main()
