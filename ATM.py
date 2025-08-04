'''
ATM
'''
class ATM:
    '''
    ATM class
    '''
    def __init__(self, bank_balance, cash_in_hand):
        '''
        ATM properties
        '''
        self.bank = bank_balance
        self.cash = cash_in_hand
        self.fail_count = 0
        self.locked = False

    def deposit(self, amount):
        '''
        Deposit action
        '''
        if self.cash >= amount:
            self.bank += amount
            self.cash -= amount
            self.fail_count = 0     # Res3t fail count to 0
        else:
            self.fail_count += 1

    def withdraw(self, amount):
        '''
        Withdraw action
        '''
        if self.bank >= amount:
            self.bank -= amount
            self.cash += amount
            self.fail_count = 0     # Res3t fail count to 0
        else:
            self.fail_count += 1

    def process_transaction(self, action, amount):
        '''
        Transaction processing
        '''
        if self.locked:     # Consecutive error == 3
            return

        match action:
            case "D":
                self.deposit(amount)
            case "W":
                self.withdraw(amount)
            case _:
                self.fail_count += 1

        if self.fail_count == 3:
            self.locked = True

def input_processing(action):
    '''
    Since s1ice method is restricted we gotta have to process it manually
    '''
    processed_action = ""
    processed_amount = ""
    for element in action:
        if element.isalpha():
            processed_action += element
        else:
            processed_amount += element
    return processed_action, processed_amount

def main():
    '''
    main
    '''
    initial_balance = float(input())
    initial_cash = float(input())
    atm = ATM(initial_balance, initial_cash)

    while True:
        if atm.locked:
            break

        action = input()
        if action == "end":
            break
        action, amount = input_processing(action)

        try:
            amount = float(amount)
            atm.process_transaction(action, amount)
        except ValueError:
            atm.fail_count += 1
            if atm.fail_count == 3:
                atm.locked = True
            continue

    print(f"{atm.bank:.2f}")
    print(f"{atm.cash:.2f}")
if __name__ == "__main__":
    main()
