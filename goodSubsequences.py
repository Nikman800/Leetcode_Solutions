#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countGoodSubsequences' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING word as parameter.
#

def countGoodSubsequences(word):
    MOD = 10**9 + 7
    
    freq = {}
    for char in word:
        freq[char] = freq.get(char, 0) + 1
        
    result = 1
    
    for count in freq.values():
        result = (result * pow(2, count, MOD)) % MOD
        
    return (result - 1 + MOD) % MOD
            
        
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    word = input()

    result = countGoodSubsequences(word)

    fptr.write(str(result) + '\n')

    fptr.close()
