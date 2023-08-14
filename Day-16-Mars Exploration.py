#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Letters in some of the SOS messages are altered by cosmic radiation during transmission. 
# Given the signal received by Earth as a string, , determine how many letters of the SOS message have been changed by radiation.


# In[2]:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    sos='SOS'
    j=0
    count=0
    for i in s:
        if(i!=sos[j]):
            count+=1
        j+=1
        if(j%3==0):
            j=0
    return count
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()


# In[ ]:




