#!/usr/bin/env python
# coding: utf-8

# In[54]:


n=int(input())
inputNumberSlot=n
outputList=[]
outputListContainer=[]
outputListContainerOutputContainer=[]
alphabetList=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



while(n>=1):
    if(n==inputNumberSlot):
        outputList.append(str(n))
    else:
        outputList.append(str(n))
        for i in range(n+1,inputNumberSlot+1):
            outputList.append(str(i))
            outputList.insert(0,str(i))
    outputListContainer.append(outputList)
    outputList=[]
    n=n-1

myrequiredLength=(len(outputListContainer[len(outputListContainer)-1]))+len(outputListContainer[len(outputListContainer)-1])-1


for j in range(len(outputListContainer)):
    for l in range(len(outputListContainer[j])):
        outputListContainer[j][l]=alphabetList[int(outputListContainer[j][l])-1]

for outputStr in outputListContainer:
    outputStr="-".join(outputStr).center(myrequiredLength,"-")
    print(outputStr)
    
for i in range(len(outputListContainer)-2,-1,-1):
    outputStr="-".join(outputListContainer[i]).center(myrequiredLength,"-")
    print(outputStr)


# In[ ]:





# ## 3
# 
