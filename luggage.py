casos = int(input())

def knapsack(peso,goal,posicion,elementos):
    if not memo[peso][posicion] == -1:
        return memo[peso][posicion]
    if posicion<len(elementos):
        if peso < goal:
            return (knapsack(peso,goal,posicion+1,elementos) or knapsack(peso+elementos[posicion],goal,posicion+1,elementos))
        elif peso == goal:
            return True
    return False

for caso in range(0,casos):
    elementos = list(map(int,input().split(' ')))
    peso = sum(elementos)
    memo = [[-1]*(len(elementos)+1)]*(peso+1)
    print('YES') if knapsack(0,peso/2,0,elementos) else print('NO')
