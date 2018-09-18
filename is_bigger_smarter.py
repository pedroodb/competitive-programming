lista = []

def lis(idx, memo, prev):
    maxLis = 1
    for i in range(0, idx):
        if(lis(i)+1>maxLis and lista[i]>lista[idx]):
            maxLis = lis(i)+1

try:
    while True:
        lista.append(input().split(" "))
except:
    lista.sort()
    memo = []*len(lista)
    prev = []*len(lista)
    lis(len(lista), memo, prev)
