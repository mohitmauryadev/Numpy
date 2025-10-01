import numpy as np

arr = np.array([10,2, np.nan, 20, np.nan,30,10])
print(arr)

result = np.nan_to_num(arr, nan=10)
print(result)

# if we write 
#     result = np.nan_to_num(arr)
#     then by default it place the value of nan is 0 (zero)

result_2 = np.nan_to_num(arr)
print(result_2)