import numpy as np
arr_1 = np.array([1,2,3])
arr_2 = np.array([4,5,6])
print(arr_1)
print(arr_2)
print("Concatinated Array")
new_arr = np.concat((arr_1, arr_2))
print(new_arr)