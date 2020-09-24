#!/usr/bin/env python
# coding: utf-8

# In[19]:


inputNumber = int(input())
inputNumberBinaryWidth=len(str(bin(inputNumber))[2:])+1

for i in range(1,inputNumber):
    print(str(i).rjust(inputNumberBinaryWidth)+str(oct(i))[2:].rjust(inputNumberBinaryWidth)+str(hex(i))[2:].rjust(inputNumberBinaryWidth).swapcase()+str(bin(i))[2:].rjust(inputNumberBinaryWidth))


# In[17]:





# In[ ]:




