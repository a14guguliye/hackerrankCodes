#!/usr/bin/env python
# coding: utf-8

# In[38]:


def convertToFloat(Inputlist):
    for i in range(len(Inputlist)):
        Inputlist[i]=float(Inputlist[i])
    
    return Inputlist

def findAverage(InputList):
    return float(sum(InputList)/len(InputList))

n=int(input())
inputDictList=[]
for i in range(n):
    inputValues=input()
    dictionaryInput=inputValues.split(" ")
    dictionaryKey=dictionaryInput[0]
    dictionaryValues=(dictionaryInput[1:])
    inputDict={
        dictionaryKey:convertToFloat(dictionaryValues)
    }
    inputDictList.append(inputDict)

inputName=str(input())
for i in inputDictList:
    if(i.get(inputName)!=None):
        outputList=(i.get(inputName))
        averageAnswer=findAverage(outputList)
        print("%.2f" % averageAnswer)


# In[ ]:




