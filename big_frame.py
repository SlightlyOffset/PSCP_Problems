'''
big frame
'''

def main():
    '''
    main
    '''
    words = [input().strip() for _ in range(5)]
    frame_length = len(max(words, key=len))

    print(f"*{'*' * (frame_length + 2)}*")
    for word in words:
        print(f"* {word:<{frame_length}} *")
    print(f"*{'*' * (frame_length + 2)}*")
if __name__ == "__main__":
    main()
