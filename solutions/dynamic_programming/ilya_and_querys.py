from sys import stdin, stdout

def CargarArreglo():
    caracteres = stdin.readline()
    acumulador = [0]*len(caracteres)
    for i in range(1,len(caracteres)):
        if caracteres[i-1] == caracteres[i]:
            acumulador[i] = acumulador[i-1] + 1
        else:
            acumulador[i] = acumulador[i-1]
    return acumulador

def consulta(acumulador, indice):
    return acumulador[int(indice[1])-1] - acumulador[int(indice[0])-1]

acu = CargarArreglo()
for i in range(0, int(stdin.readline())):
    print(consulta(acu, stdin.readline().split(' ')))
