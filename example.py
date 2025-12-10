import numpy as np

a = [0,1,2,1,2,0,3,0,1]
b = [0,1,2,2,1,0,3,0,0]
l = (np.unique(a)).size
c = np.zeros((l,l), dtype=int)

print(c)

for t, p in zip(a, b):
    c[t, p] += 1
    print(c)
