def calcular(cantidades):
    cantidad = 0
    set1 = set()
    for i in range(1,int(cantidades[0])+1):
        set1.add(int(input()))
    for i in range(1,int(cantidades[1])+1):
        if int(input()) in set1:
            cantidad +=1
    print(cantidad)

try:
    cantidades = input().split(" ")
    while True:
        if not ((int(cantidades[0]) == 0) and (int(cantidades[1]) == 0)):
            calcular(cantidades)
        else:
            break
        cantidades = input().split(" ")
except EOFError:
    pass
