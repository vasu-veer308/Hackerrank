#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Camel Case is a naming style common in many programming languages. In Java, method and variable names typically start with a lowercase letter, with all subsequent words starting with a capital letter (example: startThread). Names of classes follow the same pattern, except that they start with a capital letter (example: BlueCar).

#Your task is to write a program that creates or splits Camel Case variable, method, and class names.


# In[ ]:


import re
while True:
    try:
        s = input().rstrip()    
        sc, mcv, op = s.split(";")
        if sc == "S":
            if mcv == "M":
                cap = op[:-2]                                   
                
            if mcv == "C" or mcv == "V":
                cap = op
            
            s = re.sub ("(\w)([A-Z])", r"\1 \2", cap)
            print (s.lower())
                
        if sc == "C":
            cap = op.title ()
            s = re.sub (r" ", r"", cap)
            q = s[:1].lower() + s[1:]                
            
            if mcv == "M":                                
                print (q+"()")
                
            if mcv == "C":
                print (s)
              
            if mcv == "V":
                print (q)
            
    except EOFError:
        break

