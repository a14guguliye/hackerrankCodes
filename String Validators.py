#!/usr/bin/env python
# coding: utf-8

# In[11]:


inputString=input()
found=False
for i in inputString:
    if(i.isalnum()==True):
        found=True
        print(found)
        break
if(found==False):
    print(found)

found=False
for i in inputString:
    if(i.isalpha()==True):
        found=True
        print(found)
        break
if(found==False):
    print(found)

    
found=False
for i in inputString:
    if(i.isdigit()==True):
        found=True
        print(found)
        break
if(found==False):
    print(found)

    
found=False
for i in inputString:
    if(i.islower()==True):
        found=True
        print(found)
        break
if(found==False):
    print(found)

found=False
for i in inputString:
    if(i.isupper()==True):
        found=True
        print(found)
        break
if(found==False):
    print(found)


# In[ ]:




