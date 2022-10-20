#!/usr/bin/env python
# coding: utf-8

# Crea una llista que agrupi els mesos de l’any en trimestres (1T: gener, febrer i març; 2T: abril, maig, juny...), és a dir, una llista amb 4 llistes dins.

# In[7]:


# creem les llistes Trimestr
T1 = ["Gener","Febrer","Març"]
T2 = ["Abril","Maig","Juny"]
T3 = ["Juliol","Agost","Setembre"]
T4 = ["Octubre","Novembre", "Desembre"]
Any = [T1,T2,T3,T4]
print(Any)


# In[8]:


print(Any[0][1])


# In[9]:


print(Any[0])


# In[16]:


print(Any[2][2],"i", Any[3][0])

