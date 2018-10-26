def convertToNode(char):
    return ord(char) - 65

def dfs(graph, visitados, actual):
	visitados[actual] = True
	for i in range(len(graph[actual])):
		if not visitados[graph[actual][i]]:
			dfs(graph, visitados, graph[actual][i])

def cantidadComponentesConexas(graph):
	visitados = [False for i in graph]
	cant = 0
	for i in range(len(graph)):
		if not visitados[i]:
			cant+=1
			dfs(graph, visitados, i)
	return cant


testCases = int(input())
input()
for i in range(testCases):
	cant = convertToNode(input())
	graph = [[] for i in range(cant+1)]
	try:
		entrada = input()
		while not entrada == '':
			arista = list(map(convertToNode, str(entrada)))
			graph[arista[0]].append(arista[1])
			graph[arista[1]].append(arista[0])
			entrada = input()
	except:
		pass
	print(cantidadComponentesConexas(graph))
	if not i == (testCases - 1):
		print()
