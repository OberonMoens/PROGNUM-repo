#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#question 3.1
from math import *


masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e22]

newMasses = []
#finding all masses larger than the moon and adding them to a new list
for i in masses:
    if i > 7.349e+22:
        newMasses.append(i)
print(newMasses)
print(f"The average mass of the last 5 moons = {sum(masses[6:])/5}")

