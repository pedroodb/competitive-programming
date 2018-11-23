def modpow(x, y, n):
    res = 1 
    while not y == 0:
        if y % 2 == 1:
            aux = (res * x) % n
            res =  aux
        x = (x*x) % n
        y = y // 2  
    return res

testCases = int(input())
for case in range(testCases):
    entrada = list(map(int, input().split(" ")))
    print(modpow(entrada[0], entrada[1], entrada[2]))
input()