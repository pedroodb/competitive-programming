#Calculates LIS until a given position pos of a list l USING the element at pos

def auxiliarLis(pos,l,memo):
    if memo[pos] != -1:
        return memo[pos]
    memo[pos] = 1
    for i in range(pos):
        if l[pos] > l[i] and auxiliarLis(i,l,memo) >= memo[pos]:
            memo[pos] = memo[i]+1
    return memo[pos]

#Calculates LIS of entire list

def lis(l):
    memo = [-1]*len(l)
    for i in range(len(l)):
        memo[i] = auxiliarLis(i,l,memo)
    return max(memo)
