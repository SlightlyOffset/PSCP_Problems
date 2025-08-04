'''
sequence V
'''
def main():
    n = int(input())
    total = n * n
    grid = [
        " ".join(str(total - (i * n + j)) for j in range(n))
        for i in range(n)
    ]
    print("\n".join(grid))

if __name__ == "__main__":
    main()

