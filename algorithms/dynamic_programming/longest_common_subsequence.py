#Bottom-up iterative implementation 

def lcs(str1,str2):
    memo = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            memo[i][j] = memo[i-1][j-1] + 1 if str2[j-1] == str1[i-1] else max(memo[i-1][j],memo[i][j-1])
    return memo[-1][-1]