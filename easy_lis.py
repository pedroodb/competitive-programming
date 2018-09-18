size = int(input())
lista = input().split(' ')
memo = [-1]*size
prev = [-1]*size
memo[0] = 1

def lis(pos):
    if memo[pos]==-1:
        memo[pos] = 1
        for i in range(0,pos):
            if int(lista[i])<int(lista[pos]):
                if  lis(i)+1 > memo[pos]:
                    memo[pos] = lis(i)+1
            elif lis(i) > memo[pos]:
                memo[pos] = lis(i)
    return memo[pos]



print(lis(size-1))
print(memo)
