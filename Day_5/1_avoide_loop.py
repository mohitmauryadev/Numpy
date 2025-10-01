import numpy as np

arr_prices = np.array([100,200,400,523,61])
print(arr_prices)
discount = 10
final_prices = arr_prices - (arr_prices*discount/100)
print(final_prices)