#2. Crie dois arrays de tamanho 10 contendo números aleatórios entre 1 e 100.
#Some, subtraia, multiplique e divida os dois arrays.

import numpy as np


array1 = np.random.randint(1, 101, 10)
array2 = np.random.randint(1, 101, 10)


s = array1 + array2
sub = array1 - array2
m = array1 * array2
d = array1 / array2  # Resultado em ponto flutuante

print("Array 1:", array1)
print("Array 2:", array2)
print("\nSoma:", s)
print("Subtração:", sub)
print("Multiplicação:", m)
print("Divisão:", d)


