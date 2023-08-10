#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    alphabets={'A':0,'B':0,'C':0,'D':0,'E':0,
          'F':0,'G':0,'H':0,'I':0,'J':0,
          'K':0,'L':0,'N':0,'O':0,'P':0,
          'Q':0,'R':0,'S':0,'T':0,'U':0,
          'V':0,'W':0,'X':0,'Y':0,'Z':0,'M':0}
    pan_string='not pangram'
    s=s.upper()
    for i in s:
        if i in alphabets:
            print("found ",i)
            alphabets[i]=1
        if(all(value == 1 for value in alphabets.values())):
            pan_string='pangram'
            print(alphabets)
            return pan_string
    print(alphabets)
    return pan_string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()

