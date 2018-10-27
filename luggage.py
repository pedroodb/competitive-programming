casos = int(input())

traductor={1:True,0:False}

def knapsack(peso,goal,posicion,elementos):
    global memo
    if memo[peso][posicion] == -1:
        if posicion<len(elementos):
            if peso < goal:
                if (traductor[knapsack(peso+elementos[posicion],goal,posicion+1,elementos)] or traductor[knapsack(peso,goal,posicion+1,elementos)]):
                    memo[peso][posicion] = 1
                else:
                    memo[peso][posicion] = 0
            elif peso == goal:
                memo[peso][posicion] = 1
            else:
                memo[peso][posicion] = 0
        else:
            memo[peso][posicion] = 0
    return memo[peso][posicion]

for caso in range(0,casos):
    elementos = list(map(int,input().split(' ')))
    peso = sum(elementos)
    memo = [[-1]*(len(elementos)+1) for _ in range(peso+1)]
    print('YES') if knapsack(0,peso/2,0,elementos) else print('NO')
