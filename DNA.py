'''DNA'''
# Main goal is to find the longest continous sequnce of repeated dna
def validation(seq_1, seq_2):
    '''validate DNA sequence'''
    valid_nucleotide = "ATCG"
    for nucleotide in seq_1 + seq_2:
        if nucleotide not in valid_nucleotide:
            return False
    return True

def longest_common_substring(str1, str2):
    '''find longest common substring'''
    n, m = len(str1), len(str2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_len = 0
    end_index = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_index = i

    return str1[end_index - max_len:end_index] if max_len > 0 else "None"

def main():
    '''main'''
    dna_seq_1 = input()
    dna_seq_2 = input()
    valid = validation(dna_seq_1, dna_seq_2)
    print(longest_common_substring(dna_seq_1, dna_seq_2) if valid else "Error")
if __name__ == '__main__':
    main()
