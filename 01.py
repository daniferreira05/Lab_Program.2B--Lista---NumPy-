#1. Crie um array NumPy contendo os números de 1 a 10. Em seguida,
#transforme-o em um array bidimensional com 2 linhas e 5 colunas.

import numpy as np

array = np.arange(1, 11)

array_2d = array.reshape(2, 5)

print("Array original:", array)
print("\nArray 2D (2 linhas e 5 colunas):")
print(array_2d)

