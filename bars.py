def conformarBarra(barraActual, largoActual):
    if memo[barraActual][largoActual] == -1:
        if largoActual == largoBarra:
            act = True
        elif cantidadBarras == barraActual:
            act = False
        elif largoActual > largoBarra:
            act = False
        else:
            act = (conformarBarra((barraActual + 1), largoActual)) or (conformarBarra((barraActual + 1), (largoActual + barras[barraActual])))
        memo[barraActual][largoActual] = act
    return memo[barraActual][largoActual]

testCases = int(input())
for i in range (0, testCases):
    largoBarra = int(input())
    cantidadBarras = int(input())
    barras = list(map(int, input().split(' ')))
    sumaBarras = sum(barras)
    memo = [[-1]*(sumaBarras+1) for m in range(cantidadBarras + 1)]
    if(conformarBarra(0, 0)):
        print('YES')
    else:
        print('NO')
