import numpy as np

x = np.random.random_integers(1, 20, size=15)
x = x.reshape((3, 5))
print(x)

# print(a)
print(np.max(x, axis=1))
print(np.max(x, axis=1, keepdims=True))
a = np.where(x == np.max(x, axis=1, keepdims= True), 0, x)
print(a)