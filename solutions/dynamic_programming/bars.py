def knapsackBU(elems,maxWeight):
    memo = [[0 for _ in range(maxWeight + 1)]for _ in range(len(elems)+1)]
    for i in range(1,len(memo)):
        for j in range(1,len(memo[i])):
            memo[i][j] = max(memo[i-1][j],elems[i-1][1]+memo[i-1][j-elems[i-1][0]] if elems[i-1][0] <= j else 0)
    return memo[len(memo)-1][len(memo[0])-1]

tcs = int(input())
for tc in range(tcs):
    final = int(input())
    cant = int(input())
    elems = list(map(lambda bar : (int(bar),int(bar)),input().split(' ')))
    print('YES' if knapsackBU(elems,final) == final else 'NO')