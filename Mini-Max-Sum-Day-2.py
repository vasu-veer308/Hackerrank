#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min=0
    max=0
    arr.sort()
    min=arr[0]+arr[1]+arr[2]+arr[3]
    max=arr[1]+arr[2]+arr[3]+arr[4]
    print(f"{min} {max}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

