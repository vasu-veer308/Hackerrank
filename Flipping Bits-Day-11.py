#!/usr/bin/env python
# coding: utf-8

# In[1]:


#You will be given a list of 32 bit unsigned integers. Flip all the bits ( and ) and return the result as an unsigned integer.


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    binlist=[]
    a=n
    print(f"n={n}")
    if n==0:
        binlist=[0]*32
    while(a>0):
        binlist.insert(0,a%2)
        a=a//2
    print(binlist)
    
    rem=32-len(binlist)
    if(rem>0):
        while(rem!=0):
            binlist.insert(0,0)
            rem-=1
    print(f"binlist={binlist}")
    for i in range(len(binlist)):
        if (binlist[i]==0):
            binlist[i]=1
        else:
            binlist[i]=0
    ind=31
    final=0
    print(f"length of result={binlist}")
    for i in binlist:
        if i==1:
            final+=(2**ind)
        ind-=1
    print(f"finl={final}")
    return final
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

