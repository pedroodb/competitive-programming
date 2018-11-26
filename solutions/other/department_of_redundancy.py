def actualizar(item, lista):
    for i in lista:
        if i[0]==item:
            i[1]+=1
            return True
    lista.append([item,1])

def imprimir(res):
    for i in res:
        print(i[0]," ",i[1])

list = input().split(" ")
res = []
for i in list:
    actualizar(i, res)
imprimir(res)
