#!/usr/bin/env python
# coding: utf-8

# In[12]:


def convertToInt(inputList):
    for i in range(len(inputList)):
        inputList[i]=int(inputList[i])
    
    return inputList


x=int(input())
runnerScore=[]


# In[ ]:


scores=input().split(" ")
scores=convertToInt(scores)
scores.sort()
maxNumber=scores[len(scores)-1]
for i in range(len(scores)-1,-1,-1):
    if(scores[i]<maxNumber):
        maxNumber=scores[i]
        break
print(maxNumber)


# In[62]:





# In[63]:





# In[ ]:




