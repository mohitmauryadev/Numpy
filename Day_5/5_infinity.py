import numpy as np

arr = np.array([10, 20, np.inf, 30, -np.inf, 40])

result = np.isinf(arr)
print(result)