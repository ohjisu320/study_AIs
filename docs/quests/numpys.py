import numpy as np

# 1번
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
pass
np.concatenate((a,b), axis=0)
# array([1, 2, 3, 4, 5, 6])

# 2번
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

np.concatenate((a,b), axis=0)
# array([[1, 2],
#        [3, 4],
#        [5, 6],
#        [7, 8]])

# 3번
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
np.concatenate((a,b), axis=1)
# array([[1, 2, 5, 6],
#        [3, 4, 7, 8]])

# 4번
a = np.array([1, 2, 3])
b = np.array([[4, 5, 6], [7, 8, 9]])
a = a[np.newaxis]
np.concatenate((a,b), axis=0)

# 5번
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([[7, 8, 9], [10, 11, 12]])
a = a[np.newaxis]
b = b[np.newaxis]
np.concatenate((a,b,c), axis=0)