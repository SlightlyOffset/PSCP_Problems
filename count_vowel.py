'''
count vowel
'''

def main():
    '''
    main
    '''
    vowels = ["a", "e", "i", "o", "u"]
    vowel_count = 0
    for _ in range(int(input())):
        vowel_count += 1 if input().lower() in vowels else 0
    print(vowel_count)
if __name__ == "__main__":
    main()
