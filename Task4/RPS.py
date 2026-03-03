#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
hand = str(input("Wanna play a little game?! Rock(R), Paper(P), Scissors(S):"))

Hands = ['R', 'P', 'S']
Saw = np.random.choice(Hands)

print(f"You played {hand} and Saw played {Saw}")

if hand == Saw:
    print("Its a tie")
elif (hand == 'R' and Saw == 'S') or (hand == 'P' and Saw == 'R') or (hand == 'S' and Saw == 'P'):
    print("CONGRACHULASJONS! U WON!")
else: 
    print("COMPUTER WILL SELF DESTRUCT IN 5...4...3...2..1...")

