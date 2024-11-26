#28.Dado o array x=[0,1,2,3,4] e y=[1,2,0,2,1], crie novos valores para xxx em
#passos de 0.1 usando numpy.interp. Plote os valores interpolados (se
#necessário, use Matplotlib para exibir).

import numpy as np


x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 2, 0, 2, 1])

x_interp = np.arange(0, 4.1, 0.1)
y_interp = np.interp(x_interp, x, y)

for xi, yi in zip(x_interp, y_interp):
    print(f"x = {xi:.1f}, y_interp = {yi:.2f}")

