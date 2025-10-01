import numpy as np

arr = np.array([10, 20, np.inf, 30, -np.inf, 40])
print(arr)

result = np.nan_to_num(arr, posinf=50, neginf=-100)
print(result)

