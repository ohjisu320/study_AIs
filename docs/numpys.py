py_list = [[1,2]
           ,[3,4]
           ,[5,6]]  # list
import numpy as np
np_array = np.array([[7, 8]
                    ,[9,10]
                    ,[11,12]])  # 행렬 = array

# 구분 위한 type 확인
type(py_list)
# <class 'list'>
type(np_array)
# <class 'numpy.ndarray'>

# class type에 따른 편리성
# py_list.sum()
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# AttributeError: 'list' object has no attribute 'sum'
np_array.sum()
# 57
# axis=0은 row 단위, axis=1은 column 단위
np_array.sum(axis=0) 
# array([27, 30])
np.sum(np_array, axis=0)
# array([27, 30])
np_array.sum(axis=1)
# array([15, 19, 23])
np.sum(np_array, axis=1)
# array([15, 19, 23])

np.array(py_list)
# array([[1, 2],
#        [3, 4],
#        [5, 6]])
np_array_second = np.array(py_list)
type(np_array_second)
# <class 'numpy.ndarray'>
np.concatenate((np_array, np_array_second), axis=0)
# array([[ 7,  8],
#        [ 9, 10],
#        [11, 12],
#        [ 1,  2],
#        [ 3,  4],
#        [ 5,  6]])
np.concatenate((np_array, np_array_second), axis=1)
# array([[ 7,  8,  1,  2],
#        [ 9, 10,  3,  4],
#        [11, 12,  5,  6]])
pass

# reshape(): 기존 배열을 재배열
# 1차원 배열 생성
arr = np.arange(10)
print("원본 1차원 배열:")
print(arr)

arr.reshape(5,2) # arr에 바로 저장되지는 않음.
# array([[0, 1],
#        [2, 3],
#        [4, 5],
#        [6, 7],
#        [8, 9]])
arr 
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr.reshape(5,3) # error: 원소의 개수와 맞지 않음
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# ValueError: cannot reshape array of size 10 into shape (5,3)
arr.reshape(-1,2) # -1: 행 또는 열에 맞게 계산해서 열 또는 행을 배정해줌
# array([[0, 1],
#        [2, 3],
#        [4, 5],
#        [6, 7],
#        [8, 9]])
arr.reshape(-1,1)
# array([[0],
#        [1],
#        [2],
#        [3],
#        [4],
#        [5],
#        [6],
#        [7],
#        [8],
#        [9]])
pass