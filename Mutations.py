#!/usr/bin/env python
# coding: utf-8

# In[1]:


def mutate_string(string, position, character):
    inputList=list(string)
    inputList[position]=character
    outputString="".join(inputList)
    return outputString

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# In[ ]:




