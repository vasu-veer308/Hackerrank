#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    count = len(arr)
    plus = 0
    minus = 0
    zero = 0
    if count > 0: 
        for i in arr:
            if i>0:
                plus=plus+1
            if i<0: 
                minus = minus+1
            if i == 0:
                zero = zero+1
        
    print (plus/count)
    print(minus/count)
    print(zero/count)
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

