#!/usr/bin/env python
# coding: utf-8

# In[14]:


## Julian Date calculator

D1 = float(input("Input the first Day:"))
M1 = float(input("Input the first Month:"))
Y1 = float(input("Input the first Year:"))

JD1 = 367*Y1 -7*(Y1+(M1+9)/12)/4 - 3*((Y1+(M1-9)/7)/100 + 1)/4 + (275*M1)/9 + D1 + 1721029-0.5

D2 = float(input("Input the second Day:"))
M2 = float(input("Input the second Month:"))
Y2 = float(input("Input the second Year:"))

JD2 = 367*Y2 -7*(Y2+(M2+9)/12)/4 - 3*((Y2+(M2-9)/7)/100 + 1)/4 + (275*M2)/9 + D2 + 1721029-0.5

print(f"The difference is: {abs(JD2-JD1)} days")


# In[ ]:




