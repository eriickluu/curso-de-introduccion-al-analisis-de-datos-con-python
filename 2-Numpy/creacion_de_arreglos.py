import numpy as np 

a = np.arange(0, 10)

print(a)
print('-----------------------------')

a = np.arange(0, 20, 2)

print(a)
print('-----------------------------')

a = np.zeros(10)

print(a)
print('-----------------------------')

a = np.zeros(10, dtype=np.integer)

print(a)
print('-----------------------------')

a = np.ones(10, dtype=np.integer)

print(a)
print('-----------------------------')

a = np.full(10, 5)

print(a)
print('-----------------------------')

a = np.full(10, 2.5)

print(a)
print('-----------------------------')

a = np.random.random(15)

print(a)
print('-----------------------------')

a = np.random.random(15 * 10)

print(a)
print('-----------------------------')

a = np.random.randint(0, 25, 10)

print(a)
print('-----------------------------')

a = np.random.randint(0, 50, 200)

print(a)
print('-----------------------------')

a = np.linspace(0, 10, 10)

print(a)
print('-----------------------------')