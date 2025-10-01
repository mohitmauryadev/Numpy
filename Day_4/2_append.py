import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)

new_arr = np.append(arr, [6,7])
print(new_arr)

arr_2D = np.array([[1,2],[3,4],[5,6]])
print(arr_2D)
arr_2D_row = np.append(arr_2D, [[7],[8],[9]], axis=1)
print(arr_2D_row)
