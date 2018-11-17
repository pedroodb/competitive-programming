#Implementacion recursiva top-down

def auxKnapsackTD(weightLeft,value,idx,l,memo):
    if weightLeft <= 0 or idx == len(l):
        return value
    if not memo[weightLeft][idx] is None:
        memo[weightLeft][idx] = max(auxKnapsack(weightLeft-l[idx][0],value+l[idx][1],idx+1,l,memo) if weightLeft-l[idx][0] > 0 else value,auxKnapsack(weightLeft,value,idx+1,l,memo))
    return memo[weightLeft][idx]

def knapsackTD(elems,maxWeight):
    memo = [[[None] for _ in range(len(elems))]for i in range(maxWeight + 1)]
    return auxKnapsack(maxWeight,0,0,elems,memo)

#Implementacion iterativa bottom-up

def knapsackBU(elems,maxWeight):
    memo = [[[0] for _ in range(len(elems)+1)]for i in range(maxWeight + 1)]
    for i in range(1,len(memo)):
        for j in range(1,len(memo[i])):
            memo[i][j] = max(memo[i-1][j],elems[j][1]+memo[i-1][j-elems[j][0]] if elems[j][0] <= j else 0)
    return memo
    
ms,n = list(map(int,input().split(' ')))
elems = []
for i in range(n):
    elems.append(list(map(int,input().split(' '))))
print(knapsack(elems,ms))

#Todavia no funciona no se xq xq xq xqxqxqxxq