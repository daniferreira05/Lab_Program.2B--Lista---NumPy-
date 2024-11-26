#24.Crie uma matriz 5×5 contendo os números inteiros de 1 a 25. Extraia a
#submatriz formada pelas linhas 2 a 4 e pelas colunas 2 a 4.

import numpy as np


matriz = np.arange(1, 26).reshape(5, 5)

# Extraindo a submatriz das linhas 2 a 4 e colunas 2 a 4
submatriz = matriz[1:4, 1:4]

print("Matriz original:")
print(matriz)
print("\nSubmatriz (linhas 2 a 4 e colunas 2 a 4):")
print(submatriz)


