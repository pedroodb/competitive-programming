#Top-down recursive implementation

def auxKnapsackTD(weightLeft,value,idx,l,memo):
    if weightLeft <= 0 or idx == len(l):
        return value
    if not memo[weightLeft][idx] is None:
        memo[weightLeft][idx] = max(auxKnapsackTD(weightLeft-l[idx][0],value+l[idx][1],idx+1,l,memo) if weightLeft-l[idx][0] > 0 else value,auxKnapsack(weightLeft,value,idx+1,l,memo))
    return memo[weightLeft][idx]

def knapsackTD(elems,maxWeight):
    memo = [[[None] for _ in range(len(elems))]for i in range(maxWeight + 1)]
    return auxKnapsackTD(maxWeight,0,0,elems,memo)

#Bottom-up iterative implementation 

def knapsackBU(elems,maxWeight):
    memo = [[0 for _ in range(maxWeight + 1)]for _ in range(len(elems)+1)]
    for i in range(1,len(memo)):
        for j in range(1,len(memo[i])):
            memo[i][j] = max(memo[i-1][j],elems[i-1][1]+memo[i-1][j-elems[i-1][0]] if elems[i-1][0] <= j else 0)
    return memo[len(memo)-1][len(memo[0])-1]

#Expects an element list (elems) as a couple (weight,value)

#Input format example
'''maxWeight,n = list(map(int,input().split(' ')))
elems = []
for i in range(n):
    elems.append(list(map(int,input().split(' '))))
print(knapsackBU(elems,maxWeight))'''
