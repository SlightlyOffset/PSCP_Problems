'''
cal
'''

def main():
    '''
    main
    '''
    # input_to = int(input())
    # operand_pushed = input_to
    # operator_pushed = input_to - 1
    # final_equal = 1

    # if input_to == 1:
        # print(input_to)
    # else:
        # print(abs(operand_pushed + operator_pushed + final_equal))
    # ----------------------------
    # operand = int(input())
    # operator = operand      # + for each operand plus final equal(=)
    # print(operand + operator if operand != 1 else operand)
    
    operand = int(input())
    print(1 if operand == 1 else 2 * operand)
if __name__ == "__main__":
    main()
