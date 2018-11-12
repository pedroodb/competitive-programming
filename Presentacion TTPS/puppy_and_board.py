from functools import reduce

def movimientos(i,j):
    movs = [(movsI,j) for movsI in range(0,i)]
    movs.extend([(i,movsJ) for movsJ in range(0,j)])
    return movs

def posicionGanadora(i,j,memo):
    if memo[i][j] is None:
        memo[i][j] = not reduce(lambda res, sigMov: res and posicionGanadora(sigMov[0],sigMov[1],memo), movimientos(i,j), True)
    return memo[i][j]

testCases = int(input())
memo = [[False if i == 0 and j == 0 else None for i in range(3)] for j in range(4)]
for tc in range(testCases):
    n,m = list(map(int,input().split(' ')))
    print('Tuzik' if posicionGanadora((n-1) % 4, (m-1) % 3, memo) else 'Vanya')