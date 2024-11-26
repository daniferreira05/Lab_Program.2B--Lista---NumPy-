# 7- Crie um array bidimensional representando notas de 5 alunos em 4 provas.
#Calcule a média de cada aluno e a média de cada prova.

import numpy as np


notas = np.array([
    [7, 8, 9, 6],
    [5, 6, 7, 8],
    [9, 8, 7, 6],
    [6, 7, 8, 9],
    [8, 9, 7, 8]
])


media_alunos = np.mean(notas, axis=1)
media_provas = np.mean(notas, axis=0)

print("Média de cada aluno:", media_alunos)
print("Média de cada prova:", media_provas)

