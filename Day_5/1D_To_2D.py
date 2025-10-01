import numpy as np

arr_2D = np.array([[1,2,3],[4,5,6]])
arr_1D = np.array([10,20,30])

result = arr_1D + arr_2D
print(result)



# It will shows error because first is 2x3 matrix and second is 1D matrix with 2 column


# arr_2D = np.array([[1,2,3],[4,5,6]])
# arr_1D = np.array([10,20])
# result = arr_1D + arr_2D