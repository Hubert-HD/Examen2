matriz = None

def mochila(numElementos, capacidad, valoresElementos, costosElementos):
  for x in range(numElementos):
    matriz.append([])
    for y in range(capacidad + 1):
      matriz[x].append(0)

  for i in range(numElementos):
    for j in range(capacidad + 1):
      if costosElementos[i] <= j:
        matriz[i][j] = max(matriz[i - 1][j], valoresElementos[i] + matriz[i - 1][j - costosElementos[i]])
      else:
        matriz[i][j] = matriz[i - 1][j]

  return matriz[numElementos - 1][capacidad]


numCasosPrueba = 2
caso1 = {
  "numElementos": 4,
  "capacidad": 6,
  "valoresElementos": [5, 2, 4, 1],
  "costosElementos": [6, 2, 1, 2]
}
caso2 = {
  "numElementos": 10,
  "capacidad": 5,
  "valoresElementos": [1, 3, 2, 3, 1, 1, 3, 2, 4, 2],
  "costosElementos": [1, 2, 2, 1, 1, 2, 3, 1, 2, 2]
}
matriz = []
resultado1 = mochila(caso1["numElementos"], caso1["capacidad"], caso1["valoresElementos"], caso1["costosElementos"])
print(resultado1)
matriz = []
resultado2 = mochila(caso2["numElementos"], caso2["capacidad"], caso2["valoresElementos"], caso2["costosElementos"])
print(resultado2)
