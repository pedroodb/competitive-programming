def lugaresComunes(lugares1, lugares2):
    memo = [[0]*(len(lugares2)+1) for m in range(len(lugares1)+1)]
    for i in range(1,(len(lugares1) + 1)):
        for j in range(1, (len(lugares2) + 1)):
            if lugares1[i-1] == lugares2[j-1]:
                memo[i][j] = memo[i-1][j-1] + 1
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])
    return memo[len(lugares1)][len(lugares2)]

casos = 0
lugares1 = str(input())
while not lugares1 == "#":
    lugares2 = str(input())
    casos+=1
    print("Case #" + str(casos) + ": you can visit at most " + str(lugaresComunes(lugares1, lugares2)) + " cities.")
    lugares1 = input()
