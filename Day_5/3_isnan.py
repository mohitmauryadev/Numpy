import numpy as np

arr = np.array([10,2, np.nan, 20, np.nan,30,10])
print(arr)

result = np.isnan(arr)
print(result)