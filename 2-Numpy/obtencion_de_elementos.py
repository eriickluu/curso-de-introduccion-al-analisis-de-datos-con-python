import numpy as np 

lista = [10, 20, 30, 40, 50, 60]

a = np.array(lista)

print(a[0])

print(a[5])

print(a[a.size-1])

print(a[1:5])

print(a[1:5:2])

print(a[::-1])

lista_indices = [0, 3, 4, 5]

print(a[lista_indices])

print(a[[0, 3, 4, 5]])

print(a * 10)

print(((a * 10) -10) / 2)