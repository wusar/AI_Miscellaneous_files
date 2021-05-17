import numpy as np

t=np.array([[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5],[0, 1, 2, 3, 4, 5],[0, 1, 2, 3, 4, 5],[0, 1, 2, 3, 4, 5],[0, 1, 2, 3, 4, 5],])
#print(t)

#t = t.reshape([6, 3, 2])
print(t)
a = np.mean(t, axis=1)
print(t)
print(a)
print(a.shape)
print(t.shape)
norm=t-a
print(norm)
# t = t.reshape([3, 2, 3])
# print(t)
# np.mean(t, axis=1)
# print(t)