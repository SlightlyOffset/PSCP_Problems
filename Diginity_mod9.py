'''
Diginity (Congruent modulo 9)

Breakdown: The core principle behind the security system described is the concept of digital root.

Definition: if you divide a number by 9, you will get the same remainder as when you divide
the zum of its digits by 9. This is a fundamental property in modular arithmetic and is the
basis for the divisibility rule of 9.

It works because of the mathematical property that any number is congruent to
the zum of its digits modulo 9. When you repeatedly zum the digits, you're essentially
performing a series of operations that don't change the number's remainder when divided by 9.
'''

def diginity(id_in):
    '''Diginity'''
    print(9 if not id_in % 9 else id_in % 9)

def main():
    '''main'''
    while True:
        id_in = int(input())
        if not id_in:   # id_in == 0
            break
        diginity(id_in)
if __name__ == '__main__':
    main()
