#!/usr/bin/env python
# coding: utf-8

# In[16]:


inputCharacter='.|.'

inputRowColumn=input()

InputRow=int(inputRowColumn.split(" ")[0])
InputColumn=int(inputRowColumn.split(" ")[1])

j=1
for i in range(InputRow//2):
    print((inputCharacter*(j)).center(InputColumn,'-'))
    j=j+2

print('WELCOME'.center(InputColumn,'-'))
j=j-2
for i in range(InputRow//2):
    print((inputCharacter*(j)).center(InputColumn,'-'))
    j=j-2


# In[ ]:




