def calcularLinea(linea, problemas):
    problema = False
    for i in problemas:
        if(linea[1] in i):
            problema = i
    if(problema and (not problema[2])):
        if(linea[2] == "wrong"):
            problema[0] += 20
        else:
            problema[2] = True
            problema[0] += int(linea[0])
    else:
        if(linea[2] == "wrong"):
            problemas.append([20,linea[1], False])
        else:
            problemas.append([int(linea[0]),linea[1],True])

def imprimirResultadoDeEquipo(problemas):
    penalizaciones = 0
    cantProblemas = 0
    for i in problemas:
        if(i[2]):
            penalizaciones += i[0]
            cantProblemas+=1
    print(cantProblemas, " ", penalizaciones)

while True:
    problemas = []
    linea = input()
    if not linea:
        break
    while (not linea == "-1"):
        linea = linea.split(" ")
        calcularLinea(linea, problemas)
        linea = input()
    imprimirResultadoDeEquipo(problemas)
