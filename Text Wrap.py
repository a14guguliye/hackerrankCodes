#!/usr/bin/env python
# coding: utf-8

# In[15]:


import textwrap
def wrap(string, max_width):
    result=""
    while(len(string)>=max_width):
        result+=string[0:max_width]
        string=string[max_width:]
        result+="\n"
    result+=string;
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# In[12]:





# In[13]:





# In[ ]:




