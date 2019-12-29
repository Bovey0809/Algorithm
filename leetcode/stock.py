#%%
import operator
from functools import reduce
prices = [29, 30, 50, 46, 31, 35, 32]
diff = []
for i in range(1, len(prices)):
    diff.append(prices[i] - prices[i-1])
print(diff)
# %%
money = 100
for i in range(len(prices)-1):
    if diff[i] > 0:
        while diff[i] > 0:
            i += 1
        stock = money // prices[i]
        left = money - stock * prices[i]
        money = stock * prices[i+1] 
        money += left
        i += 1
print(money)
