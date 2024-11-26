#17.Crie uma matriz quadrada 3×3 aleatória. Calcule o determinante e, se
#possível, a inversa dessa matriz.


import numpy as np


matriz = np.random.randint(1, 101, size=(3, 3))
determinante = np.linalg.det(matriz)

if determinante != 0:
    inversa = np.linalg.inv(matriz)
else:
    inversa = None  # Não existe inversa se o determinante for zero

print("Matriz 3x3 aleatória (inteiros):")
print(matriz)
print("\nDeterminante da matriz:", determinante)
if inversa is not None:
    print("\nInversa da matriz:")
    print(inversa)
else:
    print("\nA matriz não tem inversa (determinante é zero).")
