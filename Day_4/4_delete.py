import numpy as np

arr = np.array([1,2,3,4,5,6,7])
print(arr)
new_arr = np.delete(arr, 3)
print(new_arr)

arr_2D = np.array([[1,2,3],[4,5,6],[1,8,3],[9,3,6]])
print("arr_2D")
print(arr_2D)
new_arr_2D = np.delete(arr_2D, 1, axis=0)
print("new_arr_2D")
print(new_arr_2D)