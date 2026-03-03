#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

func = input("Input a function:")
lowerBound = float(input("Input the lower bound:"))
upperBound = float(input("Input the upper bound:"))

def integral(func, lowerBound, upperBound):
    x = np.random.uniform(lowerBound, upperBound, 100000)
    
    # Evaluate function (vectorized)
    y = eval(func)
    
    # Monte Carlo estimate
    result = (upperBound - lowerBound) * np.mean(y)
    
    return result

result = integral(func, lowerBound, upperBound)

print(f"Estimated integral = {result}")

