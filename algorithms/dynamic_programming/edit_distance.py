#Bottom-up iterative implementation 

def editDistance(str1,str2,delCost,insCost,editCost):
    memo = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]
    for i in range(0,len(str1)+1):
        for j in range(0,len(str2)+1):
            if j == 0:
                memo[i][j] = delCost*i
            elif i == 0:
                memo[i][j] = insCost*j
            else:
                memo[i][j] = min(memo[i-1][j-1]+(0 if str1[i-1] == str2[j-1] else editCost),memo[i-1][j]+delCost,memo[i][j-1]+insCost)
    return memo[-1][-1]

#No entra en spoj, preguntar
#Preguntar como se guardaria el recorrido

tc = int(input())
for t in range(tc):
    print(editDistance(input(),input(),1,1,1))
