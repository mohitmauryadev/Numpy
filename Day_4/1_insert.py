import numpy as np

arr = np.array([1,2,3,4,5])

print(arr)
new_arr = np.insert(arr, 0,0, axis=None)
   #axis = None means we are working with 1 D array and if we will working with 2D array then axis = 0 for row and axis = 1 is use for collumn

print(new_arr)

arr_2D = np.array([[1,2],[3,4],[5,6]])
print("2D array")
print(arr_2D)

new_2D_arr = np.insert(arr_2D, 1, [9,2], axis=0)    # for row
print("New 2D array")
print(new_2D_arr)


new_2D_arr_cl = np.insert(arr_2D, 1, [9,2,0], axis=1)    # for Collumn
print("New 2D array")
print(new_2D_arr_cl)
