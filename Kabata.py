""" PSCP - Kabata """
def is_kabata(word:str):
    """ use for check if its kabata """
    if "baka" in word:
        return "no"
    if "bakka" in word:
        word = word.replace("bakka", "")
    if "ba" in word:
        word = word.replace("ba", "")
    if "ka" in word:
        word = word.replace("ka", "")
    if "ta" in word:
        word = word.replace("ta", "")

    if word:
        return "no"
    return "yes"

def main():
    """ main """
    count = int(input())
    res = {}


    for i in range(count):
        word = str(input())
        res[f"{i}"] = is_kabata(word)

    for i in res.values():
        print(i)

if __name__ == "__main__":
    main()
