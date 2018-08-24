def jolly(lista):
    res = [False]*(int(lista[0])-1)
    for i in range(1,len(lista)-1):
        try:
            res[abs(int(lista[i])-int(lista[i+1]))-1] = True
        except:
            return False
    for i in res:
        if not i:
            return False
    return True

while True:
    lista = input()
    if lista:
        lista = lista.split(" ")
        if(jolly(lista)):
            print("Jolly")
        else:
            print("Not jolly")
    else:
        break
