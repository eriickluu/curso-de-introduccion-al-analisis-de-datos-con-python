import numpy as np 

a = np.array([1, 2, 3, 4, 5])

print(a)
print('-----------------------------')

a = np.array([1, 2, 3, 4, 5], dtype='f')

print(a)
print('-----------------------------')

a = np.array([1, 2, 3, 4, 5], dtype=np.float32)

print(a)
print('-----------------------------')

a = np.array([1, 2.3, 3, 4, 5.7, 6.8, 7.2], dtype=np.float32)

print(a)
print('-----------------------------')

a = np.array([1, 2.3, 3, 4, 5.7, 6.8, 7.2], dtype='i')

print(a)
print('-----------------------------')

a = np.array([1, 2.3, 3, 4, 5.7, 6.8, 7.2], dtype=np.integer)

print(a)
print('-----------------------------')

a = np.array([1, 0, 0, 1, 0, 1], dtype='?')

print(a)
print('-----------------------------')

a = np.array([1, 0, 0, 1, 0, 1], dtype=np.bool)

print(a)
print('-----------------------------')