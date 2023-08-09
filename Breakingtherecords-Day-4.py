#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    min =0
    max=0
    cmin=0
    cmax=0
    count=0
    for i in scores:
        if(count==0):
            min = i
            max=i
            count+=1
            continue
        if(i>max):
            max=i
            cmax += 1
            count+=1
            continue
        if(i<min):
            min=i
            cmin += 1
            count+=1
            continue
       
    Rscore=[cmax,cmin]
    return Rscore
    
         
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

