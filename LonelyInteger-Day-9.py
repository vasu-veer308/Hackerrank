#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Given an array of integers, where all elements but one occur twice, find the unique element.


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    i=0
    n=len(a)
    b=a.copy()
    flag=0
    if((n-1)==i):
        return b[i]
    while(i<(n-1)):   
        j=i+1    
        
        while(j<n):
            flag=0
            print(f"a[i]={b[i]} a[j]={b[j]}")
            if(b[i]!=b[j]):
                if j==(n-1):
                    return b[i]
    
                else:
                    j=j+1
                    continue
            else:
                flag=1
                b.pop(j)
                b.pop(i)
                n=n-2
                i=0
                if((n-1)==i):
                    
                    return b[i]
                break
        if flag==1:
            continue
        i+=1    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()

