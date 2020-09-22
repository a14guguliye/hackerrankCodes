#!/usr/bin/env python
# coding: utf-8

# In[17]:


def count_substring(string, sub_string):
    n=0
    for i in range(len(string)-1):
        if(string[i]==sub_string[0]):
            partialFound=True
            passed=0
            for j in range(len(sub_string)):
                if((i+j)>len(string)-1):
                    break
                if(string[i+j]==sub_string[j]):
                    passed=passed+1;
            if(passed==len(sub_string)):
                n=n+1
    return n

print(count_substring("TestCaseTestCase","CaseT"))


# In[ ]:




