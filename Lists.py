#!/usr/bin/env python
# coding: utf-8

# In[5]:


n=int(input())
inputList=[]


for i in range(n):
    inputCommand=input()
    inputCommandList=inputCommand.split(" ")
    if(inputCommandList[0]=='append'):
        inputList.append(int(inputCommandList[1]))
    elif(inputCommandList[0]=='insert'):
        inputList.insert(int(inputCommandList[1]),int(inputCommandList[2]))
    elif(inputCommandList[0]=='print'):
        print(inputList)
    elif(inputCommandList[0]=='remove'):
        inputList.remove(int(inputCommandList[1]))
    elif(inputCommandList[0]=='sort'):
        inputList.sort()
    elif(inputCommandList[0]=='pop'):
        inputList.pop()
    elif(inputCommandList[0]=='reverse'):
        inputList.reverse()


# In[ ]:




