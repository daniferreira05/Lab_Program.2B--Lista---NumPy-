#27.Crie uma matriz 2×2 para representar uma transformação linear e um vetor
#v=[1,2]. Aplique a transformação ao vetor v multiplicando-o pela matriz.

import numpy as np


matriz = np.array([[2, 1], [1, 3]])
#Vetor:
v = np.array([1, 2])

resultado = np.dot(matriz, v)

print("Matriz de transformação:")
print(matriz)
print("\nVetor v:")
print(v)
print("\nResultado da transformação (matriz * vetor):")
print(resultado)


