#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

#Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
#- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hr24=''
    if(s[-2:]=='AM' and s[:2]=='12'):
        hr24='00'+s[2:-2];
    elif(s[-2:]=='AM'):
        print('enter here')
        hr24=s[:-2];
    elif(s[-2:]=='PM' and s[:2]=='12'):
        hr24=s[:-2];
    else:
        hr24=str(int(s[:2])+12)+s[2:-2]
    return hr24
        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

