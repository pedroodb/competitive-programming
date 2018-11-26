dic=dict()
linea = input()
while not (linea == ''):
    campos = linea.split(' ')
    dic[campos[1]] = campos[0]
    linea = input()
try:
    while True:
        linea = input()
        print(dic[linea])
except EOFError:
    pass
