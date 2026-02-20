#!/usr/bin/env python
# coding: utf-8

# In[32]:


#quadratic formula
import math

a = int(input("Input value for a:"))
b = int(input("Input value for b:"))
c = int(input("Input value for c:"))

D = (b**2)-4*a*c

x1 = (-b + math.sqrt(abs(D)))/2*a
x2 = (-b - math.sqrt(abs(D)))/2*a

if (D < 0):
    print("This has no solution")
elif (D == 0):
    print(f"x equals {x1}")
else:
    print(f"x1 = {x1} and x2 = {x2}")

