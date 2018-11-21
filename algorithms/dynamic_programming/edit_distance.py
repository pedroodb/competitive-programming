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

#Bottom-up iterative implementation including path

def editDistanceWithPath(str1,str2,delCost,insCost,editCost):
    memo = [[[0, []] for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]
    for i in range(0,len(str1)+1):
        for j in range(0,len(str2)+1):
            if j == 0:
                memo[i][j] = [delCost*i, memo[i][j][1] + [("d", str1[i-1])]]
            elif i == 0:
                memo[i][j] = [insCost*j, memo[i][j][1] + [("a", str2[j-1])]]
            else:
                mincost = memo[i-1][j-1]
                if not str1[i-1] == str2[j-1]:
                    mincost[0] += editCost
                    mincost[1] += [("m", str1[i-1], str2[j-1])]
                if memo[i-1][j][0]+delCost < mincost[0]:
                    mincost[0] = memo[i-1][j][0]+delCost
                    mincost[1] += [("d", str1[i-1])]
                if memo[i][j-1][0]+insCost < mincost[0]:
                    mincost[0] = memo[i][j-1][0]+insCost
                    mincost[1] += [("a", str2[j-1])]
    return memo[-1][-1]


#No entra en spoj, preguntar
#Preguntar como se guardaria el recorrido

tc = int(input())
for t in range(tc):
    print(editDistanceWithPath(input(),input(),1,1,1))
