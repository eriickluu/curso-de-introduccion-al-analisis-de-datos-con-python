import numpy as np 

a = np.arange(0, 10)

print(a)
print('-----------------------------')

a[5] = 100

print(a)
print('-----------------------------')

a[0:4] = 20

print(a)
print('-----------------------------')

a[[4, 6, 7]] = 10

print(a)
print('-----------------------------')

np.append(a, 50)

# mejor practica
a = np.append(a, 50)

print(a)
print('-----------------------------')

np.delete(a, 5)

a = np.delete(a, 5)

print(a)
print('-----------------------------')

np.append(a, [500, 500]])

a = np.append(a, [500, 500]])

print(a)
print('-----------------------------')